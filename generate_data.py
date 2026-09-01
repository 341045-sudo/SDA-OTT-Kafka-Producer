import csv
import random
import time

event_types = ["PLAY", "PAUSE", "SEEK"]
content_ids = ["C001", "C002", "C003", "C004", "C005"]

with open("ott_clickstream_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "userId",
        "timestamp",
        "eventType",
        "contentId",
        "position_sec"
    ])

    for i in range(1, 51):
        user_id = f"U{random.randint(1, 15):03d}"
        timestamp = int(time.time()) + i
        event_type = random.choice(event_types)
        content_id = random.choice(content_ids)
        position_sec = random.randint(0, 3600)

        writer.writerow([
            user_id,
            timestamp,
            event_type,
            content_id,
            position_sec
        ])

print("50 OTT clickstream records generated successfully.")