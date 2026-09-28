"""Reconstruct pre-repair bytecode exactly if its source timestamp can be proven."""
import hashlib
import importlib.util
import marshal
import pathlib
import struct
from datetime import datetime,timezone

here=pathlib.Path(__file__).resolve().parent
root=here.parents[1]
src=root/'scripts'/'summary_state.py'
pyc=root/'scripts'/'__pycache__'/'summary_state.cpython-312.pyc'
raw=src.read_text(encoding='utf-8')
block='''# The corpus is stored in these twelve research-source trees. Operational
# artifacts elsewhere in the repository may contain PDF copies or fixtures.
CORPUS_SOURCE_ROOTS = (
    "01_Core_Web_Agent_Architectures",
    "02_Web_Agent_Benchmarks_Environments",
    "03_Agentic_Search_Scraping_Info_Seeking",
    "04_Adversarial_Web_Prompt_Injection_Content_Manipulation",
    "05_Agentic_Traps_Persistence_Adaptive_Attacks",
    "06_Resource_Exhaustion_Availability_Denial_of_Wallet",
    "07_Security_Benchmarks_Evaluation",
    "08_Defenses_Guards_Containment",
    "09_Progress_Long_Horizon_Benign_Controls",
    "10_Traditional_Crawling_Crawler_Traps",
    "11_Surveys_Taxonomies_SoK",
    "12_Contextual_Borderline",
)
DUPLICATE_ROOT = "99_Duplicates"
'''
func='''def discover_corpus_pdfs():
    canonical = sorted(
        path for name in CORPUS_SOURCE_ROOTS
        for path in (ROOT / name).rglob("*.pdf")
    )
    duplicates = sorted((ROOT / DUPLICATE_ROOT).rglob("*.pdf"))
    return canonical, duplicates


'''
new='''    canonical, duplicates = discover_corpus_pdfs()
    all_pdfs = canonical + duplicates
    mapped = [resolve(row["Pdf"]) for row in manifest]
    outside = [relative(path) for path in mapped
               if path.relative_to(ROOT).parts[0] not in CORPUS_SOURCE_ROOTS]
    if outside:
        raise ValueError(f"Manifest source outside approved corpus roots: {outside}")
'''
old='''    all_pdfs = sorted(ROOT.rglob("*.pdf"))
    canonical = [p for p in all_pdfs if "99_Duplicates" not in p.relative_to(ROOT).parts]
    duplicates = [p for p in all_pdfs if p not in canonical]
    mapped = [resolve(row["Pdf"]) for row in manifest]
'''
for needle in (block,func,new):
    assert raw.count(needle)==1,needle[:40]
raw=raw.replace(block,'').replace(func,'').replace(new,old)
orig=raw.encode('utf-8')
assert len(orig)==9614,(len(orig),hashlib.sha256(orig).hexdigest())
assert hashlib.sha256(orig).hexdigest()=='30eab772c1914c3f03538d10a27e224580a2dbf821e8d8cdc041b7a5693896c2'
(here/'forensic'/'ORIGINAL_SUMMARY_STATE_RECONSTRUCTED.py').write_bytes(orig)
current=pyc.read_bytes()
code=compile(orig,str(src),'exec')
payload=marshal.dumps(code)
assert current[:4]==importlib.util.MAGIC_NUMBER
def candidate(ts):
    return importlib.util.MAGIC_NUMBER+b'\0\0\0\0'+struct.pack('<II',ts,len(orig))+payload
expected='46ff962fc9c13014d0ef5099d3447fbdf1fd3fc6ca6ddcb0b96746dbe07f0f92'
target=[datetime(2026,9,7,15,19,22,tzinfo=timezone.utc).timestamp(),src.stat().st_ctime]
for value in target:
    ts=int(value)
    b=candidate(ts)
    print('timestamp_guess',datetime.fromtimestamp(ts,timezone.utc).isoformat(),len(b),hashlib.sha256(b).hexdigest(),flush=True)
    if hashlib.sha256(b).hexdigest()==expected:
        (here/'forensic'/'ORIGINAL_SUMMARY_STATE_RESTORED.pyc').write_bytes(b)
        print('MATCH',flush=True)
        break
