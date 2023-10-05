import re

from pydantic import field_validator, SecretStr

from .. import InfectionMonkeyBaseModel
from .validators import ntlm_hash_regex


class LMHash(InfectionMonkeyBaseModel):
    lm_hash: SecretStr

    def __hash__(self) -> int:
        return hash(self.lm_hash)

    @field_validator("lm_hash")
    @classmethod
    def validate_hash_format(cls, lm_hash):
        if not re.match(ntlm_hash_regex, lm_hash.get_secret_value()):
            raise ValueError("Invalid LM hash provided")
        return lm_hash
