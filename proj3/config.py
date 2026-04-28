import vertexai
from google.oauth2 import service_account

PROJECT_ID = "ace-axon-487016-t5"
LOCATION = "us-central1"
KEY_PATH = "vertex-key.json"
MODEL_NAME = "gemini-2.5-pro"

credentials = service_account.Credentials.from_service_account_file(KEY_PATH)

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    credentials=credentials
)
