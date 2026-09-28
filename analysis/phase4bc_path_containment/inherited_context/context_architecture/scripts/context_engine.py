"""Phase 4BC deterministic packets. Only synthetic sources can ever be delivered.

Library inputs: registry={artifacts:[artifact_id,path,sha256,layer,role,reason,
permitted_content_category,dependencies]}, allowlists={primary:[ids],verifier:[ids]}.
Registry paths are relative to the supplied context_architecture root. Templates are
ordinary registered artifacts included explicitly in the corresponding allowlist.
No source paths, freeform coordinator narrative, glob expansion or ambient files
are accepted. Semantic-review identity provenance remains an orchestration duty;
this module checks exact digest bindings, not reviewer authentication.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import html
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import stat
import unicodedata

VERSION = "phase4bc-context-v1.0.0"
BINDING_KEYS = {"phase", "holdout_id", "paper_id", "source_sha256", "methodology_sha256", "context_protocol_version", "current_report_source"}
ENTRY_KEYS = {"artifact_id", "path", "sha256", "layer", "role", "reason", "permitted_content_category", "dependencies"}
HEX = re.compile(r"^[0-9a-f]{64}$")

class GuardError(ValueError):
    pass

def require(condition, reason):
    if not condition:
        raise GuardError(reason)

def _normal(value):
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, dict):
        require(all(isinstance(k, str) for k in value), "non-string key")
        keys = [_normal(k) for k in value]
        require(len(set(keys)) == len(keys), "normalized duplicate key")
        return {_normal(k): _normal(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_normal(v) for v in value]
    require(value is None or type(value) in (bool, int, float), "unsupported representation")
    if type(value) is float:
        require(math.isfinite(value), "non-finite number")
    return value

def canonical(value):
    return json.dumps(_normal(value), ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")

def digest(data):
    return hashlib.sha256(data).hexdigest()

def fingerprint(value):
    return digest(canonical(value))

def now():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def _pairs(pairs):
    result = {}
    for k, v in pairs:
        require(k not in result, "duplicate JSON key")
        result[k] = v
    return result

def loads(data):
    if isinstance(data, bytes):
        data = data.decode("utf-8", errors="strict")
    return _normal(json.loads(data, object_pairs_hook=_pairs, parse_constant=lambda s: (_ for _ in ()).throw(GuardError("non-finite number"))))

def load(path):
    return loads(Path(path).read_bytes())

def _safe_path(root, relative):
    require(isinstance(relative, str) and relative, "missing relative path")
    require("\\" not in relative and not any(x in relative for x in ("*", "?", "$", "%", "\x00", ":")), "path expansion or unsafe path")
    pieces = relative.split("/")
    require(all(x not in ("", ".", "..") for x in pieces), "path traversal")
    require(not PurePosixPath(relative).is_absolute(), "absolute path")
    root = Path(root).absolute()
    p = root
    for part in pieces:
        p = p / part
        s = p.lstat()
        require(not stat.S_ISLNK(s.st_mode) and not (getattr(s, "st_file_attributes", 0) & 0x400), "symlink/reparse point")
    require(p.resolve().is_relative_to(root.resolve()), "root escape")
    require(p.is_file(), "not a file")
    return p

def validate_binding(binding):
    require(isinstance(binding, dict) and set(binding) == BINDING_KEYS, "binding keys")
    require(all(isinstance(v, str) and v and "\x00" not in v for v in binding.values()), "binding value")
    require(HEX.fullmatch(binding["source_sha256"]) and HEX.fullmatch(binding["methodology_sha256"]), "binding digest")
    require(binding["context_protocol_version"] == VERSION, "context version")
    require(binding["current_report_source"] == "NOT_YET_OPENED", "source already exposed")
    for key in ("phase", "holdout_id", "paper_id"):
        require(re.fullmatch(r"[A-Za-z0-9_.:-]{1,100}", binding[key]), "identifier format")
    return _normal(binding)

def verify_immutable(root, entries):
    """Rehash an explicitly pinned execution manifest. Never regenerate a pin.

    Root must be a dedicated immutable code/config tree, not a mixed runtime tree.
    Any extra file is rejected. Dependency trees must receive a separate manifest.
    """
    require(isinstance(entries, list) and entries, "immutable manifest empty")
    expected = {}
    for entry in entries:
        require(set(entry) == {"relative_path", "size_bytes", "sha256"}, "immutable entry shape")
        rel = entry["relative_path"]
        require(rel.casefold() not in {x.casefold() for x in expected}, "immutable duplicate")
        p = _safe_path(root, rel)
        data = p.read_bytes()
        require(type(entry["size_bytes"]) is int and len(data) == entry["size_bytes"] and digest(data) == entry["sha256"], "immutable drift")
        expected[rel] = entry
    observed = set()
    for base, directories, files in os.walk(root, followlinks=False):
        for name in directories:
            p = Path(base) / name
            s = p.lstat()
            require(not stat.S_ISLNK(s.st_mode) and not (getattr(s, "st_file_attributes", 0) & 0x400), "immutable reparse directory")
        for name in files:
            observed.add((Path(base) / name).relative_to(root).as_posix())
    require(observed == set(expected), "unexpected immutable file")
    return fingerprint(sorted(entries, key=lambda x: x["relative_path"]))

def validate_packet(packet):
    body = loads(packet)
    require(isinstance(body, dict) and set(body) == {"context_protocol_version", "role", "binding", "context", "fork_history",
        "previous_holdout_scientific_content_included", "coordinator_summary_included", "source_release"}, "packet shape")
    require(body["context_protocol_version"] == VERSION and body["role"] in ("primary", "verifier"), "packet version/role")
    validate_binding(body["binding"])
    require(body["fork_history"] == "none" and body["previous_holdout_scientific_content_included"] is False
        and body["coordinator_summary_included"] is False and body["source_release"] == "DRY_RUN_ONLY", "packet context isolation")
    require(isinstance(body["context"], list) and body["context"], "context empty")
    ids = set()
    for c in body["context"]:
        require(isinstance(c, dict) and set(c) == {"artifact_id", "layer", "content"}, "nested context shape")
        require(isinstance(c["artifact_id"], str) and c["artifact_id"] not in ids and c["layer"] in ("A", "B") and isinstance(c["content"], str), "nested context fields")
        ids.add(c["artifact_id"])
    require(canonical(body) == packet, "packet must be exact canonical bytes")
    return body

def _check_references(text, entry, by_id):
    require(not re.search(r"\$\{|%[A-Za-z_][A-Za-z0-9_]*%|\{\{\s*(?:include|import)|{%\s*(?:include|import)|^\s*(?:!include|@include|#include|import |from \S+ import )", text, re.M | re.I), "context import/expansion")
    references = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
    allowed_paths = {by_id[i]["path"] for i in entry["dependencies"]}
    parent = PurePosixPath(entry["path"]).parent
    if entry["path"].lower().endswith(".json"):
        def walk(value):
            if isinstance(value, dict):
                for key, item in value.items():
                    require(key.casefold() not in ("include", "includes", "import", "imports", "runtime_include", "context_path", "context_paths"), "nested context include")
                    if key in ("$ref", "$dynamicRef"):
                        require(isinstance(item, str) and item.startswith("#"), "external JSON schema reference")
                    walk(item)
            elif isinstance(value, list):
                for item in value:
                    walk(item)
        walk(loads(text))
    for reference in references:
        target = reference.split("#", 1)[0].strip("<>")
        if not target:
            continue
        require(not re.match(r"[a-z]+:", target, re.I), "external context link")
        require(".." not in target.split("/") and not any(c in target for c in "*?$%\\"), "unsafe context reference")
        resolved = str(parent / target)
        require(resolved in allowed_paths, "undeclared context reference")

def build_packet(root, registry, allowlists, binding, role):
    """Returns exact bytes plus metadata. Entire bytes constitute task wrapper."""
    binding = validate_binding(binding)
    require(role in ("primary", "verifier"), "role")
    require(set(registry) == {"artifacts"} and isinstance(registry["artifacts"], list), "registry shape")
    require(set(allowlists) == {"primary", "verifier"}, "allowlist shape")
    entries = registry["artifacts"]
    by_id = {}
    paths = set()
    for e in entries:
        require(isinstance(e, dict) and set(e) == ENTRY_KEYS, "registry entry shape")
        require(isinstance(e["artifact_id"], str) and re.fullmatch(r"[a-zA-Z0-9_.-]+", e["artifact_id"]), "artifact identifier")
        require(e["artifact_id"] not in by_id, "duplicate artifact")
        require(isinstance(e["path"], str) and e["path"].casefold() not in paths, "duplicate/case path")
        require(isinstance(e["dependencies"], list) and len(set(e["dependencies"])) == len(e["dependencies"]), "dependency shape")
        require(isinstance(e["sha256"], str) and HEX.fullmatch(e["sha256"]), "artifact hash")
        for key in ("role", "reason", "permitted_content_category"):
            require(isinstance(e[key], str) and e[key], "registry metadata")
        paths.add(e["path"].casefold())
        by_id[e["artifact_id"]] = e
    ids = allowlists[role]
    require(isinstance(ids, list) and ids and len(ids) == len(set(ids)), "empty/duplicate allowlist")
    require(all(i in by_id for i in ids), "unknown artifact")
    visited, active = set(), set()
    def visit(i):
        require(i not in active, "dependency cycle")
        if i in visited:
            return
        active.add(i)
        for dep in by_id[i]["dependencies"]:
            require(dep in ids, "dependency not explicitly allowlisted")
            visit(dep)
        active.remove(i)
        visited.add(i)
    for i in ids:
        visit(i)
    contents, inventory = [], []
    for i in sorted(ids):
        e = by_id[i]
        require(e["layer"] in ("A", "B"), "historical/current source content cannot be generic asset")
        require(e["role"] in (role, "both", "template_" + role), "artifact role mismatch")
        p = _safe_path(root, e["path"])
        data = p.read_bytes()
        require(digest(data) == e["sha256"], "artifact content changed")
        text = data.decode("utf-8", errors="strict")
        _check_references(text, e, by_id)
        contents.append({"artifact_id": i, "layer": e["layer"], "content": text})
        inventory.append({"artifact_id": i, "relative_path": e["path"], "size_bytes": len(data), "sha256": e["sha256"], "layer": e["layer"]})
    payload = {"context_protocol_version": VERSION, "role": role, "binding": binding, "context": contents,
               "fork_history": "none", "previous_holdout_scientific_content_included": False,
               "coordinator_summary_included": False, "source_release": "DRY_RUN_ONLY"}
    packet = canonical(payload)
    metadata = {"packet_sha256": digest(packet), "task_wrapper_sha256": digest(packet), "binding_sha256": fingerprint(binding),
                "generic_methodology_sha256": fingerprint([e for e in inventory if e["layer"] == "A"]),
                "frozen_policy_sha256": fingerprint([e for e in inventory if e["layer"] == "B"]),
                "registry_sha256": fingerprint(registry), "allowlists_sha256": fingerprint(allowlists), "included": inventory,
                "excluded_artifact_ids": sorted(set(by_id) - set(ids)), "builder_version": VERSION}
    return packet, metadata

def _scan_normal(text):
    text = html.unescape(text)
    for _ in range(3):
        text = re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m[1], 16)), text)
        text = re.sub(r"\\x([0-9a-fA-F]{2})", lambda m: chr(int(m[1], 16)), text)
        text = text.replace("\\n", " ").replace("\\t", " ").replace("\\r", " ")
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())

def scan_packet(packet, deny):
    require(set(deny) == {"version", "patterns"}, "deny shape")
    text = _scan_normal(packet.decode("utf-8", errors="strict"))
    hits = []
    for p in deny["patterns"]:
        require(set(p) == {"id", "text", "category"} and all(isinstance(v, str) and v for v in p.values()), "deny entry")
        needle = _scan_normal(p["text"])
        require(needle, "empty deny pattern")
        at = text.find(needle)
        if at >= 0:
            hits.append({"pattern_id": p["id"], "category": p["category"], "normalized_offset": at})
    return {"packet_sha256": digest(packet), "scanner_version": VERSION, "deny_sha256": fingerprint(deny),
            "status": "STATIC_CONTEXT_CONTAMINATED" if hits else "STATIC_CONTEXT_CLEAN", "hits": hits}

def review_record(packet, *, reviewer_context_id, status, rationale, review_protocol_sha256):
    require(status in ("SEMANTIC_CONTEXT_CLEAN", "SEMANTIC_CONTEXT_CONTAMINATED", "SEMANTIC_CONTEXT_UNRESOLVED"), "review status")
    require(reviewer_context_id and rationale and HEX.fullmatch(review_protocol_sha256), "review metadata")
    return {"packet_sha256": digest(packet), "reviewer_context_id": reviewer_context_id, "status": status,
            "rationale": rationale, "review_protocol_sha256": review_protocol_sha256, "review_mode": "SEPARATE_CONTEXT_MODEL_VERIFICATION"}

def release(packet, deny, static_record, semantic_record, *, builder_context_id, expected_binding, expected_packet_sha256, expected_review_protocol_sha256):
    """Rechecks exact bytes; never trusts a builder-provided clean flag."""
    body = validate_packet(packet)
    require(digest(packet) == expected_packet_sha256, "packet differs from frozen approval inventory")
    require(body["binding"] == validate_binding(expected_binding), "wrong binding")
    actual = scan_packet(packet, deny)
    require(actual == static_record, "stale/forged static result")
    require(actual["status"] == "STATIC_CONTEXT_CLEAN", "static contamination")
    require(semantic_record.get("packet_sha256") == digest(packet), "stale semantic result")
    require(semantic_record.get("status") == "SEMANTIC_CONTEXT_CLEAN", "semantic review unavailable/unclean")
    require(set(semantic_record) == {"packet_sha256", "reviewer_context_id", "status", "rationale", "review_protocol_sha256", "review_mode"}, "review record shape")
    require(semantic_record.get("reviewer_context_id") and semantic_record["reviewer_context_id"] != builder_context_id, "self review")
    require(semantic_record.get("review_mode") == "SEPARATE_CONTEXT_MODEL_VERIFICATION", "wrong review mode")
    require(HEX.fullmatch(semantic_record.get("review_protocol_sha256", "")), "review protocol")
    require(HEX.fullmatch(expected_review_protocol_sha256) and semantic_record["review_protocol_sha256"] == expected_review_protocol_sha256, "review protocol differs from frozen protocol")
    require(isinstance(semantic_record.get("rationale"), str) and semantic_record["rationale"].strip(), "empty semantic review rationale")
    return {"packet_sha256": digest(packet), "binding_sha256": fingerprint(expected_binding),
            "static_review_sha256": fingerprint(static_record), "semantic_review_sha256": fingerprint(semantic_record),
            "static_status": static_record["status"], "semantic_status": semantic_record["status"],
            "status": "PACKET_DRY_RUN_APPROVED", "production_source_release_available": False}

def _write_exclusive(path, obj):
    data = canonical(obj)
    with Path(path).open("xb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    require(Path(path).read_bytes() == data, "durable readback mismatch")
    return digest(data)

class SyntheticSession:
    """Receipt mechanics exclusively for synthetic fixtures; never holdout access.

    Caller supplies exact synthetic bytes, not a source path. Persistent exclusive
    records allow crashes/recovery to fail closed. Directory fsync support is
    platform-dependent and these tests are not arbitrary power-loss guarantees.
    """
    def __init__(self, directory, binding):
        self.directory = Path(directory)
        self.binding = validate_binding(binding)
        require(binding["phase"] == "SYNTHETIC_TEST" and binding["holdout_id"].startswith("SYNTHETIC_")
                and binding["paper_id"].startswith("SYNTHETIC_"), "REAL_SOURCE_RELEASE_DISABLED")
        require(self.directory.is_dir(), "explicit test directory required")

    def receipt(self, packet, decision, immutable_sha256, policy_sha256, template_sha256):
        require(validate_packet(packet)["binding"] == self.binding, "wrong receipt binding")
        require(decision["packet_sha256"] == digest(packet) and decision["status"] == "PACKET_DRY_RUN_APPROVED", "release mismatch")
        require(decision.get("static_status") == "STATIC_CONTEXT_CLEAN" and decision.get("semantic_status") == "SEMANTIC_CONTEXT_CLEAN", "receipt reviews not clean")
        require(all(HEX.fullmatch(x) for x in (immutable_sha256, policy_sha256, template_sha256)), "receipt fingerprint")
        event = {"sequence": 1, "type": "PRE_ACCESS_RECEIPT", "binding": self.binding, "packet_sha256": digest(packet),
                 "release_sha256": fingerprint(decision), "immutable_code_sha256": immutable_sha256,
                 "policy_sha256": policy_sha256, "template_sha256": template_sha256, "previous_sha256": None,
                 "methodology_sha256": self.binding["methodology_sha256"], "source_sha256": self.binding["source_sha256"],
                 "context_protocol_version": VERSION, "static_status": decision["static_status"], "semantic_status": decision["semantic_status"],
                 "created_at": now(), "source_access_began": False, "namespace": "TEST_FIXTURE_NOT_A_HUMAN"}
        return _write_exclusive(self.directory / "01_PRE_ACCESS_RECEIPT.json", event)

    def acknowledge(self, context_id, packet):
        receipt = load(self.directory / "01_PRE_ACCESS_RECEIPT.json")
        require(context_id and digest(packet) == receipt["packet_sha256"], "ack packet mismatch")
        require(validate_packet(packet)["binding"] == self.binding, "ack binding")
        return _write_exclusive(self.directory / "02_CONTEXT_ACK.json", {"sequence": 2, "type": "CONTEXT_ACK", "context_id": context_id,
            "packet_sha256": digest(packet), "previous_sha256": fingerprint(receipt), "fork_history": "none", "created_at": now()})

    def deliver(self, source_bytes, packet, decision):
        receipt = load(self.directory / "01_PRE_ACCESS_RECEIPT.json")
        ack = load(self.directory / "02_CONTEXT_ACK.json")
        require(ack["previous_sha256"] == fingerprint(receipt), "receipt chain")
        require(receipt["binding"] == self.binding and validate_packet(packet)["binding"] == self.binding, "source binding changed")
        require(receipt["packet_sha256"] == ack["packet_sha256"] == digest(packet), "packet changed")
        require(receipt["release_sha256"] == fingerprint(decision), "review approval changed")
        require(digest(source_bytes) == self.binding["source_sha256"], "source hash mismatch")
        _write_exclusive(self.directory / "03_SOURCE_ACCESS_BEGAN.json", {"sequence": 3, "type": "SOURCE_ACCESS_BEGAN",
            "previous_sha256": fingerprint(ack), "source_sha256": digest(source_bytes), "namespace": "SYNTHETIC_TEST_ONLY", "created_at": now()})
        return source_bytes

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build")
    for arg in ("root", "registry", "allowlists", "binding", "role", "output", "metadata"):
        b.add_argument("--" + arg, required=True)
    s = sub.add_parser("scan")
    for arg in ("packet", "deny", "output"):
        s.add_argument("--" + arg, required=True)
    args = parser.parse_args()
    if args.command == "build":
        packet, meta = build_packet(args.root, load(args.registry), load(args.allowlists), load(args.binding), args.role)
        with Path(args.output).open("xb") as f:
            f.write(packet)
        _write_exclusive(args.metadata, meta)
    else:
        _write_exclusive(args.output, scan_packet(Path(args.packet).read_bytes(), load(args.deny)))

if __name__ == "__main__":
    main()
