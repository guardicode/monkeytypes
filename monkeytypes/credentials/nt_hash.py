import re

from pydantic import SecretStr, field_serializer, field_validator

from .. import InfectionMonkeyBaseModel
from .validators import ntlm_hash_regex


class NTHash(InfectionMonkeyBaseModel):
    nt_hash: SecretStr

    def __hash__(self) -> int:
        return hash(self.nt_hash)

    @field_validator("nt_hash")
    @classmethod
    def validate_hash_format(cls, nt_hash):
        if not re.match(ntlm_hash_regex, nt_hash.get_secret_value()):
            raise ValueError("Invalid NT hash provided")
        return nt_hash

    @field_serializer("nt_hash", when_used="json")
    def dump_secret(self, v):
        return v.get_secret_value()
