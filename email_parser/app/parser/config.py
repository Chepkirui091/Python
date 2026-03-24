import os 
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
IMAP_SERVER = os.getenv('IMAP_SERVER')