from app.parser.body import extract_body
from app.parser.attachments import save_attachments
from app.models.email_model import Email

def parse_email(msg):
    subject = msg.get("subject")
    sender = msg.get("from")

    body = extract_body(msg)
    attachments = save_attachments(msg)

    return Email(
        subject=subject,
        sender=sender,
        body=body,
        attachments=attachments
    )