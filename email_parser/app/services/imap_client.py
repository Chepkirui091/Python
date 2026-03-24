import imaplib
import email
from config import EMAIL, PASSWORD, IMAP_SERVER

def fetch_emails(limit=5):
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")
    
    _,messages = mail.search(None, "ALL")
    email_ids = messages[0].split()[-limit:]
    
    emails = []
    
    for num in email_ids:
        _, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])
        emails.append(msg)
        
    mail.logout()
    return emails