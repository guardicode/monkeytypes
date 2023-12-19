from __future__ import annotations

from typing import Annotated, Optional, Union

from pydantic import Discriminator, Tag, field_serializer

from .. import INVALID_UNION_MEMBER_ERROR, InfectionMonkeyBaseModel
from . import EmailAddress, LMHash, NTHash, Password, SSHKeypair, Username
from .encoding import get_plaintext


def get_discriminator_value_identity(v) -> Optional[str]:
    keys = list(v.keys())

    if len(keys) == 0:
        return None

    if keys[0] in ["username", "email_address"]:
        return keys[0]

    return None


def get_discriminator_value_secret(v) -> Optional[str]:
    keys = list(v.keys())

    if len(keys) == 0:
        return None

    if "private_key" in keys:
        return "ssh_keypair"

    if keys[0] in ["password", "lm_hash", "nt_hash"]:
        return keys[0]

    return None


Identity = Annotated[
    Union[Annotated[Username, Tag("username")], Annotated[EmailAddress, Tag("email_address")]],
    Discriminator(
        get_discriminator_value_identity,
        custom_error_type=INVALID_UNION_MEMBER_ERROR,
        custom_error_message='Invalid identity, expected "username" or "email_address" key',
    ),
]

Secret = Annotated[
    Union[
        Annotated[Password, Tag("password")],
        Annotated[LMHash, Tag("lm_hash")],
        Annotated[NTHash, Tag("nt_hash")],
        Annotated[SSHKeypair, Tag("ssh_keypair")],
    ],
    Discriminator(
        get_discriminator_value_secret,
        custom_error_type=INVALID_UNION_MEMBER_ERROR,
        custom_error_message='Invalid secret, expected "password", "lm_hash", "nt_hash", '
        'or "private_key" key',
    ),
]

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
