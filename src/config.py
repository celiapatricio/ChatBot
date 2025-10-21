import yaml
from pathlib import Path


SECRETS_PATH = Path(__file__).parent.parent / "secrets" / "secrets.yaml"

def load_api_key():
    with open(SECRETS_PATH, "r") as f:
        secrets = yaml.safe_load(f)
    return secrets["openai"]["api_key"]
