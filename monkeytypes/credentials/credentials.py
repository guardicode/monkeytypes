from __future__ import annotations

from typing import Annotated, Optional, Union

from pydantic import Discriminator, Tag, field_serializer

from .. import INVALID_UNION_MEMBER_ERROR, InfectionMonkeyBaseModel
from . import EmailAddress, LMHash, NTHash, Password, SSHKeypair, Username
from .encoding import get_plaintext

USERNAME_TAG = "username"
EMAIL_ADDRESS_TAG = "email_address"
PASSWORD_TAG = "password"
LM_HASH_TAG = "lm_hash"
NT_HASH_TAG = "nt_hash"
SSH_KEYPAIR_TAG = "ssh_keypair"

IDENTITY_TYPES_TO_TAGS = {
    Username: USERNAME_TAG,
    EmailAddress: EMAIL_ADDRESS_TAG,
}

SECRET_TYPES_TO_TAGS = {
    Password: PASSWORD_TAG,
    LMHash: LM_HASH_TAG,
    NTHash: NT_HASH_TAG,
    SSHKeypair: SSH_KEYPAIR_TAG,
}


def get_discriminator_value_identity(v) -> Optional[str]:
    if type(v) is dict:
        keys = list(v.keys())

        if len(keys) == 0:
            return None

        if keys[0] == "username":
            return USERNAME_TAG

        if keys[0] == "email_address":
            return EMAIL_ADDRESS_TAG

    else:
        return IDENTITY_TYPES_TO_TAGS.get(type(v), None)

    return None


def get_discriminator_value_secret(v) -> Optional[str]:
    if type(v) is dict:
        keys = list(v.keys())

        if len(keys) == 0:
            return None

        if "private_key" in keys:  # for an SSH keypair, there could be a `public_key` key too
            return SSH_KEYPAIR_TAG

        if keys[0] == "password":
            return PASSWORD_TAG

        if keys[0] == "lm_hash":
            return LM_HASH_TAG

        if keys[0] == "nt_hash":
            return NT_HASH_TAG

    else:
        return SECRET_TYPES_TO_TAGS.get(type(v), None)

    return None


Identity = Annotated[
    Union[Annotated[Username, Tag(USERNAME_TAG)], Annotated[EmailAddress, Tag(EMAIL_ADDRESS_TAG)]],
    Discriminator(
        get_discriminator_value_identity,
        custom_error_type=INVALID_UNION_MEMBER_ERROR,
        custom_error_message="Invalid identity. Expected username or email address.",
    ),
]

Secret = Annotated[
    Union[
        Annotated[Password, Tag(PASSWORD_TAG)],
        Annotated[LMHash, Tag(LM_HASH_TAG)],
        Annotated[NTHash, Tag(NT_HASH_TAG)],
        Annotated[SSHKeypair, Tag(SSH_KEYPAIR_TAG)],
    ],
    Discriminator(
        get_discriminator_value_secret,
        custom_error_type=INVALID_UNION_MEMBER_ERROR,
        custom_error_message="Invalid secret. Expected password, LM hash, NT hash, or SSH keypair.",
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
