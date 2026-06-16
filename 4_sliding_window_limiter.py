import sys
import json
input_data = sys.stdin.read()
if input_data.endswith('\n'):
    input_data = input_data[:-1]
lines = input_data.split('\n')
user_history = {}
results = []
for line in lines:
    if not line.strip():
        continue
    parts = line.split()
    timestamp = int(parts[0])
    user = parts[1]
    history = user_history.get(user, [])
    history = [t for t in history if t > timestamp - 60]
    if len(history) < 3:
        results.append(True)
        history.append(timestamp)
    else:
        results.append(False)
    user_history[user] = history
print(json.dumps(results, separators=(',', ':')))