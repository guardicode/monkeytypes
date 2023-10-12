from __future__ import annotations

from typing import Optional, Union

from pydantic import field_serializer

from .. import InfectionMonkeyBaseModel
from . import EmailAddress, LMHash, NTHash, Password, SSHKeypair, Username
from .encoding import get_plaintext

Identity = Union[Username, EmailAddress]
Secret = Union[Password, LMHash, NTHash, SSHKeypair]
CredentialsComponent = Union[Identity, Secret]


class Credentials(InfectionMonkeyBaseModel):
    """Represents a credential pair (an identity and a secret)"""

    identity: Optional[Identity]
    """Identity part of credentials, like a username or an email"""

    secret: Optional[Secret]
    """Secret part of credentials, like a password or a hash"""

    @field_serializer("identity", "secret", when_used="json")
    def serialize(self, v):
        return get_plaintext(v)

    def __hash__(self) -> int:
        return hash((self.identity, self.secret))
