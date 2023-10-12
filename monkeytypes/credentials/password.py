from pydantic import SecretStr, field_serializer

from .. import InfectionMonkeyBaseModel
from .encoding import get_plaintext


class Password(InfectionMonkeyBaseModel):
    password: SecretStr

    def __hash__(self) -> int:
        return hash(self.password)

    @field_serializer("password", when_used="json")
    def dump_secret(self, v):
        return get_plaintext(v)
