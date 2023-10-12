from pydantic import SecretStr

from monkeytypes import Password

PASSWORD = SecretStr("some_simple_password")
PASSWORD_OBJECT = Password(password=PASSWORD)
PASSWORD_DICT = {"password": "some_simple_password"}


def test_password__serialization():
    assert PASSWORD_OBJECT.to_json_dict() == PASSWORD_DICT


def test_password__deserialization():
    assert Password(**PASSWORD_DICT) == PASSWORD_OBJECT
