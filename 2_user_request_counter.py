import sys
import json
input_data = sys.stdin.read().strip()
user_counts = {}
for line in input_data.split('\n'):
    if not line.strip():
        continue
    parts = line.split()
    if len(parts) >= 2:
        user = parts[1]
        user_counts[user] = user_counts.get(user, 0) + 1
print(json.dumps(user_counts, separators=(',', ':')))