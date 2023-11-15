import re
from typing import Any

from pydantic import SecretStr, field_serializer, field_validator

from .. import InfectionMonkeyBaseModel
from .encoding import get_plaintext
from .validators import ntlm_hash_regex


class LMHash(InfectionMonkeyBaseModel):
    lm_hash: SecretStr

    def __hash__(self) -> int:
        return hash(self.lm_hash)

    @field_validator("lm_hash")
    @classmethod
    def validate_hash_format(cls, lm_hash: Any) -> str:
        plaintext = get_plaintext(lm_hash)

        if not isinstance(plaintext, str):
            raise TypeError("LM hash must be a string")

        if not re.match(ntlm_hash_regex, plaintext):
            raise ValueError("Invalid LM hash provided")

        return lm_hash

    @field_serializer("lm_hash", when_used="json")
    def dump_secret(self, v):
        return get_plaintext(v)
