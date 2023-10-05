from base64 import b64decode
from typing import Any
from pydantic_core import core_schema
from pydantic import GetCoreSchemaHandler


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
            raise BytesError("Failed to decode b64 string to bytes") from e
    raise BytesError()


class B64Bytes(bytes):
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type: Any,
        handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            b64_bytes_validator,
            handler(source_type),
        )
