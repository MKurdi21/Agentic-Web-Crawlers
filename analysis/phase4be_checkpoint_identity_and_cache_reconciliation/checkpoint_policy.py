"""Versioned checkpoint authority checks; excludes only top-level updated_at."""
import copy
import hashlib
import json
import re
from datetime import datetime

VERSION='phase4be-checkpoint-semantic-identity-v1.0.0'
def strict_loads(raw):
    def pairs(items):
        value={}
        for key,item in items:
            if key in value:raise ValueError('duplicate JSON key')
            value[key]=item
        return value
    return json.loads(raw,object_pairs_hook=pairs,parse_constant=lambda x:(_ for _ in ()).throw(ValueError('nonfinite JSON')))
def canonical_bytes(snapshot):
    if not isinstance(snapshot,dict) or 'updated_at' not in snapshot or not isinstance(snapshot['updated_at'],str):
        raise ValueError('invalid checkpoint root or timestamp')
    try:
        stamp=datetime.fromisoformat(snapshot['updated_at'])
    except ValueError as exc:
        raise ValueError('invalid checkpoint timestamp') from exc
    if stamp.tzinfo is None:raise ValueError('checkpoint timestamp lacks timezone')
    stable=copy.deepcopy(snapshot)
    del stable['updated_at']
    return json.dumps(stable,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
def semantic_sha256(snapshot):return hashlib.sha256(canonical_bytes(snapshot)).hexdigest()
def stable_markdown(markdown):
    if len(re.findall(r'(?m)^Updated: .*$',markdown))!=1:raise ValueError('missing or ambiguous Updated line')
    return re.sub(r'(?m)^Updated: .*$', 'Updated: <volatile>',markdown.replace('\r\n','\n'))
def accept(raw_json,markdown,baseline_hash,baseline_markdown,generator_hash,authorized_generator_hash):
    snapshot=strict_loads(raw_json)
    if generator_hash!=authorized_generator_hash:return False
    if semantic_sha256(snapshot)!=baseline_hash:return False
    if stable_markdown(markdown)!=stable_markdown(baseline_markdown):return False
    updated=[line for line in markdown.replace('\r\n','\n').splitlines() if line.startswith('Updated:')]
    if updated!=[f"Updated: {snapshot['updated_at']}"]:return False
    return True
