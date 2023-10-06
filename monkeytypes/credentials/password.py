from pydantic import SecretStr, field_serializer

from .. import InfectionMonkeyBaseModel


class Password(InfectionMonkeyBaseModel):
    password: SecretStr

    def __hash__(self) -> int:
        return hash(self.password)

    @field_serializer("password", when_used="json")
    def dump_secret(self, v):
        return v.get_secret_value()
