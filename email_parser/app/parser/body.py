def extract_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            
            if content_type == "text/plain":
                return part.get_payload(decode=True).decode(errors="ignore")
            else:
                return msg.get_payload(decode=True).decode(errors="ignore")
            
            return ""