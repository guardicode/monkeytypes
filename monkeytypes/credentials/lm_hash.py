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
        if not re.match(ntlm_hash_regex, get_plaintext(lm_hash)):
            raise ValueError("Invalid LM hash provided")
        return lm_hash

    @field_serializer("lm_hash", when_used="json")
    def dump_secret(self, v):
        return get_plaintext(v)
