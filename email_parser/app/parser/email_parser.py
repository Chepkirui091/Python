def parse_email(message):
    try:
        from_address = message.get("From", "")
        subject = message.get("Subject", "")
        date = message.get("Date", "")
        body = ""

        if message.is_multipart():
            for part in message.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition", ""))
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    payload = part.get_payload(decode=True)
                    if payload:
                        body = payload.decode(errors="replace")
                    break
        else:
            payload = message.get_payload(decode=True)
            if payload:
                body = payload.decode(errors="replace")

        return {
            "from": from_address,
            "subject": subject,
            "date": date,
            "body": body.strip(),
        }
    except Exception:
        return {
            "from": "",
            "subject": "",
            "date": "",
            "body": "",
        }
