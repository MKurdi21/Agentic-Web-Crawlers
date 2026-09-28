"""Independent Phase 3 archive validator. It never calls the package builder."""
import hashlib,json,pathlib,re,zipfile
R=pathlib.Path(__file__).resolve().parent;ARCHIVE=R.parent/'phase3_calibration_package.zip'
manifest=json.loads((R/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
lookup={r['path']:r for r in manifest['payload_inventory']};expected=set(lookup)|{'phase3_calibration/PACKAGE_MANIFEST.json'};errors=[]
forbidden={'private','private_source_material','shadow','_deps','holdout_lane','__pycache__','uv_cache','deps'}
suffixes={'.pdf','.sqlite','.sqlite3','.db','.tmp','.zip','.7z','.png','.jpg','.jpeg','.pyc','.pyd'}
with zipfile.ZipFile(ARCHIVE) as z:
 infos=z.infolist();names=[i.filename for i in infos]
 if set(names)!=expected:errors.append('EXACT_MEMBERSHIP')
 if len(names)!=len(set(names)):errors.append('DUPLICATE_MEMBERS')
 if len(names)!=len({x.casefold() for x in names}):errors.append('CASE_COLLISION')
 if z.testzip() is not None:errors.append('CRC')
 embedded=json.loads(z.read('phase3_calibration/PACKAGE_MANIFEST.json'))
 if embedded!=manifest:errors.append('MANIFEST_MISMATCH')
 for name in names:
  p=pathlib.PurePosixPath(name)
  if p.is_absolute() or '..' in p.parts or '\\' in name or ':' in name:errors.append('PATH:'+name)
  if set(p.parts)&forbidden or p.suffix.lower() in suffixes:errors.append('FORBIDDEN_PATH:'+name)
  data=z.read(name)
  if data.startswith((b'%PDF-',b'SQLite format 3',b'PK\x03\x04')) or re.search(rb'JVBERi0[0-9A-Za-z+/=]{80,}',data):errors.append('FORBIDDEN_SIGNATURE:'+name)
  if name in lookup:
   row=lookup[name]
   if len(data)!=row['size'] or hashlib.sha256(data).hexdigest()!=row['sha256']:errors.append('CONTENT:'+name)
result={'validator':'independent_archive_validator_v1','archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),'archive_size':ARCHIVE.stat().st_size,'member_count':len(expected),'crc_ok':'CRC' not in errors,'exact_allowlist_match':'EXACT_MEMBERSHIP' not in errors,'private_or_forbidden_content_found':any(x.startswith('FORBIDDEN') for x in errors),'errors':errors,'passed':not errors}
(R/'test_results/INDEPENDENT_PACKAGE_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
raise SystemExit(bool(errors))
