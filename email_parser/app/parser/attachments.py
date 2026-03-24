import os

ATTACHMENT_DIR = "data/attachments"

def save_attachments(msg):
    saved_files = []

    for part in msg.walk():
        if part.get_content_disposition() == "attachment":
            filename = part.get_filename()

            if filename:
                filepath = os.path.join(ATTACHMENT_DIR, filename)

                with open(filepath, "wb") as f:
                    f.write(part.get_payload(decode=True))

                saved_files.append(filepath)

    return saved_files