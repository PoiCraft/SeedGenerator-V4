import random
import uuid
from datetime import datetime

# noinspection SpellCheckingInspection
seed_keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ1234567890"

server_name = input("Server Name:")
server_date = datetime.utcnow()

key1 = str(uuid.uuid5(uuid.NAMESPACE_DNS, server_name)).replace('-', '')
key2 = list(
    f"{server_date.year}{server_date.month}{server_date.day}{server_date.hour}{server_date.minute}{server_date.second}")

for k in range(len(key1) - 1):
    v1 = key1[k]
    if v1.isdigit():
        while k >= len(key2):
            d = random.randint(1, 10)
            if d >= k:
                continue
            else:
                k = k - d
        key2[k] = v1

key3 = 0
for v in key2:
    key3 += int(v)

key4 = []
for _ in range(key3):
    key4.append(''.join(random.sample(seed_keys, len(server_name))))

key5 = []
for v in key2:
    key5.append(key4[int(v)])

key6 = ""
for v in key5:
    key6 += list(v)[random.randint(0, len(server_name) - 1)]

print(key6)
