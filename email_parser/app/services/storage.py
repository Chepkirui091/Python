import json
import os

OUTPUT_FILE = "data/parsed_emails.json"

def save_email(email_obj):
    data = {
        "subject": email_obj.subject,
        "sender": email_obj.sender,
        "body": email_obj.body,
        "attachments": email_obj.attachments
    }

    if not os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "w") as f:
            json.dump([], f)

    with open(OUTPUT_FILE, "r+") as f:
        content = json.load(f)
        content.append(data)
        f.seek(0)
        json.dump(content, f, indent=4)