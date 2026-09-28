"""Logical identity + segment containment + immutable bytes + classification.

No directory trust, glob expansion, source access or environment substitution.
The resolver is injectable only as a test dependency; all results pass the same
production final-containment and opened-handle checks.
"""
import ctypes
import hashlib
import ntpath
import os
from pathlib import Path
import re
import stat
import sys
import unicodedata

BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'vendor'))
import context_engine as context
VERSION='phase4bc-path-containment-v1.0.0'
class Rejected(ValueError):pass
def require(v,reason):
    if not v:raise Rejected(reason)
def key(p):
    parts=tuple(unicodedata.normalize('NFC',x) for x in Path(p).parts)
    return tuple(x.casefold() for x in parts) if os.name=='nt' else parts
def portable_key(p):return tuple(unicodedata.normalize('NFC',x).casefold() for x in Path(p).parts)
def contained(p,root):
    a,b=key(p),key(root)
    return len(a)>len(b) and a[:len(b)]==b
def lexical(candidate,root):
    require(isinstance(candidate,str) and candidate,'EMPTY_PATH')
    s=unicodedata.normalize('NFC',candidate).replace('\\','/')
    require(not any(ord(c)<32 for c in s) and not any(c in s for c in '*?$%<>|"'),'EXPANSION_OR_CONTROL')
    require(not s.startswith('//'),'UNC_OR_DEVICE_PATH')
    parts=s.split('/')
    require('..' not in parts,'TRAVERSAL_EVEN_IF_REENTERING')
    drive,tail=ntpath.splitdrive(s)
    if drive:
        require(os.name=='nt' and len(drive)==2 and drive[1]==':' and tail.startswith('/'),'DRIVE_RELATIVE_OR_FOREIGN_ROOT')
        require(drive.casefold()==Path(root).drive.casefold(),'ALTERNATE_DRIVE')
    elif s.startswith('/'):
        require(os.name!='nt','ROOT_RELATIVE_WINDOWS_PATH')
    stripped=[p for p in parts if p not in ('','.')]
    reserved={'con','prn','aux','nul','conin$','conout$',*[f'com{i}' for i in range(10)],*[f'lpt{i}' for i in range(10)]}
    for i,p in enumerate(stripped):
        if i==0 and drive and p==drive:continue
        require(not p.endswith(('.', ' ')) and ':' not in p,'AMBIGUOUS_COMPONENT')
        require(p.split('.')[0].casefold() not in reserved,'DEVICE_NAME')
    p=Path(s)
    if not p.is_absolute():p=Path(root)/p
    # absolute() doesn't resolve links. Dot components already disappear in Path.
    p=p.absolute()
    require(contained(p,root),'LEXICAL_ROOT_ESCAPE')
    return p
def no_links(p,root):
    current=Path(root)
    for part in [None,*p.relative_to(root).parts]:
        if part is not None:current=current/part
        st=current.lstat()
        require(not stat.S_ISLNK(st.st_mode) and not (getattr(st,'st_file_attributes',0)&0x400),'LINK_OR_REPARSE_POINT')
        if current!=p:
            names=[unicodedata.normalize('NFC',x.name).casefold() for x in current.iterdir()]
            require(len(names)==len(set(names)),'CASE_OR_UNICODE_AMBIGUITY')
def handle_path(f,fallback):
    if os.name=='nt':
        import msvcrt
        k=ctypes.WinDLL('kernel32',use_last_error=True)
        fn=k.GetFinalPathNameByHandleW
        fn.argtypes=[ctypes.c_void_p,ctypes.c_wchar_p,ctypes.c_uint32,ctypes.c_uint32];fn.restype=ctypes.c_uint32
        buf=ctypes.create_unicode_buffer(32768)
        n=fn(msvcrt.get_osfhandle(f.fileno()),buf,len(buf),0)
        require(0<n<len(buf),'FINAL_HANDLE_PATH_UNAVAILABLE')
        value=buf.value
        if value.startswith('\\\\?\\'):value=value[4:]
        require(not value.startswith('UNC\\'),'UNEXPECTED_UNC_HANDLE')
        return Path(value)
    proc=Path('/proc/self/fd')/str(f.fileno())
    if proc.exists():return proc.resolve(strict=True)
    # Portable fallback uses strict resolution plus fstat/lstat matching below.
    return Path(fallback).resolve(strict=True)

class Guard:
    FIELDS={'artifact_id','path','root_id','sha256','content_class','packet_types','immutable','dependencies','layer','role'}
    ALLOWED={'GENERIC_METHODOLOGY','FROZEN_POLICY','PACKET_TEMPLATE'}
    def __init__(self,roots,registry,allowlists,resolver=None):
        self.roots={k:Path(v).absolute() for k,v in roots.items()}
        require(self.roots,'NO_APPROVED_ROOTS')
        for r in self.roots.values():
            require(r.is_dir() and key(r.resolve(strict=True))==key(r),'ROOT_ALIAS')
            for ancestor in [r,*r.parents]:
                require(not ancestor.is_symlink() and not (getattr(ancestor.lstat(),'st_file_attributes',0)&0x400),'ROOT_OR_ANCESTOR_REPARSE')
        require(len({key(r) for r in self.roots.values()})==len(self.roots),'DUPLICATE_ROOT')
        self.resolver=resolver or (lambda p:p.resolve(strict=True))
        self.records={};self.identities=set();self.allowlists=context.loads(context.canonical(allowlists))
        require(set(allowlists)=={'primary','verifier'},'ALLOWLIST_SHAPE')
        for e in registry:
            require(set(e)==self.FIELDS,'REGISTRY_SHAPE')
            require(re.fullmatch(r'[A-Za-z0-9_.-]+',e['artifact_id']) is not None,'ARTIFACT_ID')
            require(e['artifact_id'] not in self.records and e['root_id'] in self.roots,'REGISTRY_IDENTITY')
            require(re.fullmatch('[0-9a-f]{64}',e['sha256']) is not None,'HASH_FORMAT')
            require(type(e['immutable']) is bool and isinstance(e['dependencies'],list) and all(isinstance(x,str) for x in e['dependencies']),'REGISTRY_TYPES')
            require(isinstance(e['packet_types'],list) and set(e['packet_types'])<=set(allowlists),'PACKET_TYPES')
            root=self.roots[e['root_id']];p=lexical(e['path'],root);identity=(e['root_id'],portable_key(p))
            require(identity not in self.identities,'DUPLICATE_LOGICAL_PATH')
            self.identities.add(identity);self.records[e['artifact_id']]=context.loads(context.canonical(e))
        for role,ids in allowlists.items():
            require(isinstance(ids,list) and len(ids)==len(set(ids)) and all(i in self.records for i in ids),'ALLOWLIST_IDS')
    def read(self,artifact_id,role,candidate_path=None):
        require(artifact_id in self.records and artifact_id in self.allowlists[role],'UNREGISTERED_OR_NOT_ALLOWLISTED')
        e=self.records[artifact_id];root=self.roots[e['root_id']]
        require(e['content_class'] in self.ALLOWED and e['layer'] in ['A','B'] and e['immutable'],'CONTENT_CLASS_DENIED')
        require(role in e['packet_types'] and e['role'] in [role,'both','template_'+role],'ROLE_DENIED')
        registered=lexical(e['path'],root);p=lexical(candidate_path or e['path'],root)
        require(key(p)==key(registered),'UNREGISTERED_LOCATION')
        no_links(p,root)
        resolved=Path(self.resolver(p)).absolute()
        require(contained(resolved,root),'RESOLVER_ESCAPE')
        require(key(resolved)==key(p),'INDIRECT_UNREGISTERED_IDENTITY')
        no_links(resolved,root)
        before=resolved.stat()
        require(stat.S_ISREG(before.st_mode),'NOT_REGULAR')
        with resolved.open('rb') as f:
            opened=handle_path(f,resolved)
            require(contained(opened,root) and key(opened)==key(registered),'OPEN_HANDLE_ESCAPE')
            a=os.fstat(f.fileno());data=f.read();b=os.fstat(f.fileno())
        no_links(resolved,root);after=resolved.stat()
        signature=lambda s:(s.st_dev,s.st_ino,s.st_size,s.st_mtime_ns)
        require(signature(before)==signature(a)==signature(b)==signature(after),'READ_RACE')
        require(context.digest(data)==e['sha256'],'CONTENT_HASH_MISMATCH')
        return data,{'artifact_id':artifact_id,'root_id':e['root_id'],'canonical_path':str(opened),'sha256':e['sha256'],'size_bytes':len(data),'content_class':e['content_class']}
    def packet(self,binding,role):
        context.validate_binding(binding);require(role in self.allowlists,'ROLE')
        ids=self.allowlists[role];require(ids,'EMPTY_PACKET')
        visited=set();active=set();records=[];content=[]
        def visit(i):
            require(i in ids,'DEPENDENCY_NOT_ALLOWLISTED');require(i not in active,'DEPENDENCY_CYCLE')
            if i in visited:return
            active.add(i);e=self.records[i]
            for dep in e['dependencies']:visit(dep)
            data,info=self.read(i,role);text=data.decode('utf-8')
            # Retain the parent's undeclared/import/reference controls.
            parent_records={k:{**v,'path':Path(v['path']).as_posix()} for k,v in self.records.items()}
            context._check_references(text,parent_records[i],parent_records)
            content.append({'artifact_id':i,'layer':e['layer'],'content':text});records.append(info)
            active.remove(i);visited.add(i)
        for i in sorted(ids):visit(i)
        content.sort(key=lambda x:x['artifact_id'])
        payload={'context_protocol_version':context.VERSION,'role':role,'binding':binding,'context':content,'fork_history':'none','previous_holdout_scientific_content_included':False,'coordinator_summary_included':False,'source_release':'DRY_RUN_ONLY'}
        packet=context.canonical(payload);context.validate_packet(packet)
        return packet,{'version':VERSION,'packet_sha256':context.digest(packet),'binding_sha256':context.fingerprint(binding),'registry_sha256':context.fingerprint(list(self.records.values())),'transitive_inventory':sorted(records,key=lambda x:x['artifact_id'])}
