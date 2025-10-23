import os, yaml
from pathlib import Path
from dotenv import load_dotenv

BASE = Path(__file__).parent.parent
ENV_PATH = BASE / ".env"
YAML_PATH = BASE / "secrets" / "secrets.yaml"

def load_api_key():
    api_key = None

    # 1. Intentar con .env
    if ENV_PATH.exists():
        load_dotenv(ENV_PATH)
        api_key = os.getenv("LITELLM_KEY")

    # 2. Si no existe, probar con secrets.yaml
    if not api_key and YAML_PATH.exists():
        with open(YAML_PATH, "r") as f:
            secrets = yaml.safe_load(f)
            api_key = secrets.get("openai", {}).get("api_key")

    if not api_key:
        raise ValueError("API key does not exist.")

    return api_key
