import os
from typing import Any

from dotenv import load_dotenv


def from_env(param: str, required: bool = True) -> Any:
    if required:
        return os.environ[param]
    else:
        return os.environ.get(param, None)


dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
