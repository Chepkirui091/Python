from app.services.imap_client import fetch_emails
from app.parser.email_parser import parse_email
from app.services.storage import save_email
from dotenv import load_dotenv


def main():
    try:
        # Load .env explicitly so terminal injection is not required.
        load_dotenv()
        emails, diagnostics = fetch_emails(limit=3)

        if not emails:
            print("No emails fetched.")
            print(f"Reason: {diagnostics.get('reason')}")
            print(f"Search query: {diagnostics.get('search_query')}")
            print(f"Inbox matches: {diagnostics.get('matched_inbox_count')}")
            print(f"Filtered out: {diagnostics.get('filtered_out_count')}")

            error_message = diagnostics.get("error")
            if error_message:
                print(f"Error: {error_message}")
            else:
                print("Tip: verify IMAP credentials and filters in .env.")
            return

        print(f"Fetched {len(emails)} email(s).")
        for msg in emails:
            parsed = parse_email(msg)
            print(parsed)
            save_email(parsed)
    except Exception as error:
        print(f"Failed to parse emails: {error}")

if __name__ == "__main__":
    main()