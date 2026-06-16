import sys
import json
input_data = sys.stdin.read()
if input_data.endswith('\n'):
    input_data = input_data[:-1]
lines = input_data.split('\n')
state = {}
results = []
for line in lines:
    if not line.strip():
        continue
    parts = line.split()
    timestamp = int(parts[0])
    user = parts[1]
    window_id = timestamp // 60
    key = (user, window_id)
    count = state.get(key, 0)
    if count < 2:
        results.append(True)
        state[key] = count + 1
    else:
        results.append(False)
print(json.dumps(results, separators=(',', ':')))