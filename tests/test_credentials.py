import logging
from pathlib import Path

import pytest
from pydantic import SecretBytes
from pydantic.types import SecretStr

from monkeytypes import Credentials, InfectionMonkeyBaseModel, Password, Username, get_plaintext

from .propagation_credentials import (
    CREDENTIALS,
    CREDENTIALS_DICTS,
    LM_HASH,
    PASSWORD_1,
    PLAINTEXT_LM_HASH,
    PLAINTEXT_PASSWORD,
    PLAINTEXT_PRIVATE_KEY_1,
    PRIVATE_KEY_1,
)


@pytest.mark.parametrize(
    "credentials, expected_credentials_dict", zip(CREDENTIALS, CREDENTIALS_DICTS)
)
def test_credentials_serialization_json(credentials, expected_credentials_dict):
    serialized_credentials = credentials.to_json_dict()
    deserialized_credentials = Credentials.model_validate(serialized_credentials)
    assert credentials == deserialized_credentials


logger = logging.getLogger()
logger.level = logging.DEBUG


def test_credentials_secrets_not_logged(caplog):
    class TestSecret(InfectionMonkeyBaseModel):
        some_secret: SecretStr
        some_secret_in_bytes: SecretBytes

    class TestCredentials(Credentials):
        secret: TestSecret

    sensitive = "super_secret"
    creds = TestCredentials(
        identity=None,
        secret=TestSecret(some_secret=sensitive, some_secret_in_bytes=sensitive.encode()),
    )

    logging.getLogger().info(
        f"{creds.secret.some_secret} and" f" {creds.secret.some_secret_in_bytes}"
    )

    assert sensitive not in caplog.text


_plaintext = [
    PLAINTEXT_PASSWORD,
    PLAINTEXT_PRIVATE_KEY_1,
    PLAINTEXT_LM_HASH,
    "",
    "already_plaintext",
    Path("C:\\jolly_fella"),
    None,
]
_hidden = [
    PASSWORD_1,
    PRIVATE_KEY_1,
    LM_HASH,
    "",
    "already_plaintext",
    Path("C:\\jolly_fella"),
    None,
]


@pytest.mark.parametrize("expected, hidden", list(zip(_plaintext, _hidden)))
def test_get_plain_text(expected, hidden):
    assert expected == get_plaintext(hidden)


@pytest.mark.parametrize(
    "input_, expected_error_message",
    [
        ({"identity": {}, "secret": None}, "Invalid identity. Expected username or email address."),
        (
            {
                "identity": {
                    "unrecognised_key": "test",
                },
                "secret": None,
            },
            "Invalid identity. Expected username or email address.",
        ),
        (
            {
                "identity": {
                    "email_address": "invalid email address",
                },
                "secret": None,
            },
            "Value error, value is not a valid email address: The email address is not valid. "
            "It must have exactly one @-sign.",
        ),
        (
            {
                "identity": {
                    "email_address": [],
                },
                "secret": None,
            },
            "Input should be a valid string, got `list` in ('email_address',)",
        ),
        (
            {
                "identity": {"email_address": "test@test.com", "username": "extra field"},
                "secret": None,
            },
            "Value error, Extra inputs are not permitted",
        ),
        ({"identity": {}, "secret": None}, "Invalid identity. Expected username or email address."),
        (
            {
                "identity": Password(password="not identity"),
                "secret": None,
            },
            "Invalid identity. Expected username or email address.",
        ),
    ],
)
def test_error_messages__identity(input_, expected_error_message):
    with pytest.raises(Exception) as ex:
        Credentials(**input_)

    assert str(ex.value) == expected_error_message


@pytest.mark.parametrize(
    "input_, expected_error_message",
    [
        (
            {"identity": None, "secret": {}},
            "Invalid secret. Expected password, LM hash, NT hash, or SSH keypair.",
        ),
        (
            {
                "identity": None,
                "secret": {
                    "unrecognised_key": "299BD128C1101FD6299BD128C1101FD6",
                },
            },
            "Invalid secret. Expected password, LM hash, NT hash, or SSH keypair.",
        ),
        (
            {
                "identity": None,
                "secret": {"lm_hash": "invalid"},
            },
            "Value error, Value error, Invalid LM hash provided",
        ),
        (
            {
                "identity": None,
                "secret": {"lm_hash": {}},
            },
            "Input should be a valid string, got `dict` in ('lm_hash',)",
        ),
        (
            {
                "identity": None,
                "secret": {"lm_hash": "299BD128C1101FD6299BD128C1101FD6", "password": "extra"},
            },
            "Value error, Extra inputs are not permitted",
        ),
        (
            {"identity": None, "secret": {}},
            "Invalid secret. Expected password, LM hash, NT hash, or SSH keypair.",
        ),
        (
            {
                "identity": None,
                "secret": Username(username="not secret"),
            },
            "Invalid secret. Expected password, LM hash, NT hash, or SSH keypair.",
        ),
    ],
)
def test_error_messages__secret(input_, expected_error_message):
    with pytest.raises(Exception) as ex:
        Credentials(**input_)

    assert str(ex.value) == expected_error_message
