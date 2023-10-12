from typing import Optional

from pydantic import SecretStr, field_serializer

from .. import InfectionMonkeyBaseModel
from .encoding import get_plaintext


class SSHKeypair(InfectionMonkeyBaseModel):
    private_key: SecretStr
    public_key: Optional[str]

    def __hash__(self) -> int:
        return hash((self.private_key, self.public_key))

    @field_serializer("private_key", when_used="json")
    def dump_secret(self, v):
        return get_plaintext(v)
