import json
from pathlib import Path


def save_email(parsed_email: dict):
    try:
        data_dir = Path(__file__).resolve().parents[2] / "data"
        data_dir.mkdir(parents=True, exist_ok=True)

        output_file = data_dir / "parsed_emails.jsonl"
        with output_file.open("a", encoding="utf-8") as file:
            file.write(json.dumps(parsed_email, ensure_ascii=False) + "\n")
        return str(output_file)
    except Exception:
        return None
