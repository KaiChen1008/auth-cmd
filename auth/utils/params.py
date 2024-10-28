from pathlib import Path

TOKEN_DIR = Path("~/.auth_cmd").expanduser()
TOKEN_PATH = TOKEN_DIR / "secret.csv"
