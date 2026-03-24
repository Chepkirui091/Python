class Email:
    def __init__(self, subject,sender, body, attachments=None):
        self.subject = subject
        self.sender = sender
        self.body = body
        self.attachments = attachments or []
        
        def __str__(self):
            return f"<Email subject={self.subject} from={self.sender}>"
    
# This class represents an email with its subject, sender, body, and any attachments. The __str__ method provides a string representation of the email for easy debugging and display purposes.