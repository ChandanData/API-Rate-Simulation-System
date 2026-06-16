import sys
import json
input_data = sys.stdin.read()
if input_data.endswith('\n'):
    input_data = input_data[:-1]
lines = input_data.split('\n')
results = []
for line in lines:
    if not line.strip():
        continue
    parts = line.split()
    result = {
        "time": int(parts[0]),
        "user": parts[1]
    }
    results.append(result)
print(json.dumps(results, separators=(',', ':')))