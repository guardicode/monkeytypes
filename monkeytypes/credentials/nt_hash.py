import re
from typing import Any

from pydantic import SecretStr, field_serializer, field_validator

from .. import InfectionMonkeyBaseModel
from .encoding import get_plaintext
from .validators import ntlm_hash_regex


class NTHash(InfectionMonkeyBaseModel):
    nt_hash: SecretStr

    def __hash__(self) -> int:
        return hash(self.nt_hash)

    @field_validator("nt_hash")
    @classmethod
    def validate_hash_format(cls, nt_hash: Any) -> str:
        plaintext = get_plaintext(nt_hash)

        if not isinstance(plaintext, str):
            raise TypeError("NT hash must be a string")

        if not re.match(ntlm_hash_regex, plaintext):
            raise ValueError("Invalid NT hash provided")

        return nt_hash

    @field_serializer("nt_hash", when_used="json")
    def dump_secret(self, v):
        return get_plaintext(v)
