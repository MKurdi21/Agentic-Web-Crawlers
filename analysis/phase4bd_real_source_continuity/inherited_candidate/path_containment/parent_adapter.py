"""Additive entry point for frozen Phase4BC registered generic packet assets."""
from pathlib import Path
from guard import Guard,context
def convert_registry(parent):
    records=[]
    for e in parent['artifacts']:
        if e['layer']=='D':cls='HISTORICAL_DEVELOPMENT_ONLY'
        elif e['role'].startswith('template_'):cls='PACKET_TEMPLATE'
        elif e['layer']=='A':cls='GENERIC_METHODOLOGY'
        elif e['layer']=='B':cls='FROZEN_POLICY'
        else:cls='RAW_SOURCE'
        role=e['role'];types=['primary','verifier'] if role=='both' else [role.removeprefix('template_')]
        records.append({'artifact_id':e['artifact_id'],'path':e['path'],'root_id':'parent_context','sha256':e['sha256'],'content_class':cls,'packet_types':types,'immutable':True,'dependencies':e['dependencies'],'layer':e['layer'],'role':role})
    return records
def build_parent_packet(root,registry,allowlists,binding,role):
    return Guard({'parent_context':Path(root)},convert_registry(registry),allowlists).packet(binding,role)
