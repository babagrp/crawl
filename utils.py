import json
import csv
import asyncio
import random
from datetime import datetime

async def delay():
    await asyncio.sleep(random.uniform(1.5, 4))


def save_json(data):
    name = f"output_{datetime.now().strftime('%H%M%S')}.json"
    with open(name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def save_csv(data):
    name = f"output_{datetime.now().strftime('%H%M%S')}.csv"

    keys = set()
    for d in data:
        keys.update(d.keys())

    with open(name, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(keys))
        writer.writeheader()
        writer.writerows(data)
