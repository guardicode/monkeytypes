from base64 import b64decode
from typing import Any
from collections.abc import Callable, Generator


class BytesError(Exception):
    """
    Raised when an exception occurs while decoding base64 string to bytes
    """


def b64_bytes_validator(val: Any) -> bytes:
    if isinstance(val, bytes):
        return val
    elif isinstance(val, bytearray):
        return bytes(val)
    elif isinstance(val, str):
        try:
            return b64decode(val)
        except Exception as e:
            new_error = BytesError()
            new_error.msg_template = "Failed to decode b64 string to bytes"
            raise new_error from e
    raise BytesError()


class B64Bytes(bytes):
    @classmethod
    # TODO[pydantic]: We couldn't refactor `__get_validators__`, please create the `__get_pydantic_core_schema__` manually.
    # Check https://docs.pydantic.dev/latest/migration/#defining-custom-types for more information.
    def __get_validators__(cls) -> Generator[Callable[..., Any], None, None]:
        yield b64_bytes_validator
