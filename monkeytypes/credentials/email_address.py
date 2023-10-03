from pydantic import EmailStr

from .. import InfectionMonkeyBaseModel


class EmailAddress(InfectionMonkeyBaseModel):
    email_address: EmailStr

    def __hash__(self) -> int:
        return hash(self.email_address)
