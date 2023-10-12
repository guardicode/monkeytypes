from base64 import b64decode
from typing import Any

from pydantic import BeforeValidator
from typing_extensions import Annotated


def b64_bytes_validator(val: Any) -> bytes:
    if isinstance(val, bytes):
        return val
    elif isinstance(val, bytearray):
        return bytes(val)
    elif isinstance(val, str):
        try:
            return b64decode(val)
        except Exception as e:
            raise ValueError("Failed to decode b64 string to bytes") from e
    raise ValueError()


B64Bytes = Annotated[bytes, BeforeValidator(b64_bytes_validator)]
