#!/usr/bin/env python3
import json, hashlib

def canon(e):
    return json.dumps(e, separators=(",", ":"), sort_keys=True, ensure_ascii=False).encode("utf-8")

feed=json.load(open("feed.json","r",encoding="utf-8"))
assert set(feed.keys())=={"version","feed_generated_at","events"}

allowed={"create","update","revoke","standard.initial_public_release","standard.version_update"}
events=feed["events"]
assert isinstance(events, list) and len(events)>=1

for i,e in enumerate(events):
    assert set(e.keys())=={"event_id","event_type","registry_id","version","proof_hash","timestamp","prev_hash","details"}
    assert e["event_type"] in allowed
    if e["event_type"].startswith("standard."):
        assert e["registry_id"] is None and e["version"] is None and e["proof_hash"] is None
    if i==0:
        assert e["prev_hash"] is None
    else:
        ph=hashlib.sha256(canon(events[i-1])).hexdigest()
        assert e["prev_hash"]==ph, (i, e["prev_hash"], ph)

print("OK: feed structure + prev_hash chain valid")
