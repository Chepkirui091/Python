import imaplib
import os
from email import message_from_bytes


def _parse_list_env(var_name: str):
    try:
        value = os.getenv(var_name, "")
        return [item.strip().lower() for item in value.split(",") if item.strip()]
    except Exception:
        return []


def _is_filtered(message, exclude_senders, exclude_subject_keywords):
    try:
        from_value = str(message.get("From", "")).lower()
        subject_value = str(message.get("Subject", "")).lower()

        sender_blocked = any(sender in from_value for sender in exclude_senders)
        subject_blocked = any(keyword in subject_value for keyword in exclude_subject_keywords)
        return sender_blocked or subject_blocked
    except Exception:
        return False


def fetch_emails(limit: int = 3):
    try:
        # Trim values in case the .env file has accidental surrounding whitespace.
        host = (os.getenv("IMAP_HOST") or "").strip()
        username = (os.getenv("IMAP_USER") or "").strip()
        password = (os.getenv("IMAP_PASS") or "").strip()
        search_query = (os.getenv("IMAP_SEARCH_QUERY", "ALL") or "ALL").strip()
        exclude_senders = _parse_list_env("IMAP_EXCLUDE_SENDERS")
        exclude_subject_keywords = _parse_list_env("IMAP_EXCLUDE_SUBJECT_KEYWORDS")

        # Return actionable diagnostics to explain empty results.
        diagnostics = {
            "success": False,
            "reason": "unknown",
            "error": "",
            "search_query": search_query,
            "matched_inbox_count": 0,
            "filtered_out_count": 0,
        }

        if not host or not username or not password:
            diagnostics["reason"] = "missing_env"
            return [], diagnostics

        with imaplib.IMAP4_SSL(host) as mail:
            mail.login(username, password)
            select_status, _ = mail.select("INBOX")
            if select_status != "OK":
                diagnostics["reason"] = "inbox_select_failed"
                return [], diagnostics

            status, data = mail.search(None, search_query)
            if status != "OK" or not data:
                diagnostics["reason"] = "search_failed"
                return [], diagnostics

            message_ids = data[0].split()
            diagnostics["matched_inbox_count"] = len(message_ids)
            selected_ids = message_ids[-limit:] if limit > 0 else message_ids

            messages = []
            filtered_out_count = 0
            for message_id in selected_ids:
                fetch_status, msg_data = mail.fetch(message_id, "(RFC822)")
                if fetch_status != "OK" or not msg_data:
                    continue

                raw_email = msg_data[0][1]
                message = message_from_bytes(raw_email)
                if _is_filtered(message, exclude_senders, exclude_subject_keywords):
                    filtered_out_count += 1
                    continue

                messages.append(message)

            diagnostics["filtered_out_count"] = filtered_out_count
            diagnostics["success"] = True
            diagnostics["reason"] = "ok"
            return messages, diagnostics
    except Exception as error:
        if isinstance(error, (bytes, bytearray)):
            error_text = error.decode("utf-8", errors="replace")
        else:
            error_text = str(error)
        return [], {
            "success": False,
            "reason": "exception",
            "error": error_text,
            "search_query": os.getenv("IMAP_SEARCH_QUERY", "ALL"),
            "matched_inbox_count": 0,
            "filtered_out_count": 0,
        }
