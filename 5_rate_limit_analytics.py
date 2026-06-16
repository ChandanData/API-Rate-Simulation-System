import sys
import json
input_data = sys.stdin.read()
if input_data.endswith('\n'):
    input_data = input_data[:-1]
lines = input_data.split('\n')
analytics = {}
windows = {}
for line in lines:
    if not line.strip():
        continue
    parts = line.split()
    timestamp = int(parts[0])
    user = parts[1]
    if user not in analytics:
        analytics[user] = {
            "total": 0,
            "allowed": 0,
            "blocked": 0
        }
    analytics[user]["total"] += 1
    window_id = timestamp // 10
    key = (user, window_id)
    count = windows.get(key, 0)
    if count < 1:
        analytics[user]["allowed"] += 1
        windows[key] = count + 1
    else:
        analytics[user]["blocked"] += 1
print(json.dumps(analytics, separators=(',', ':')))