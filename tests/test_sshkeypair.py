from pydantic import SecretStr

from monkeytypes import SSHKeypair

PLAIN_PRIVATE_KEY = "some_secret_private_key"
PRIVATE_KEY = SecretStr(PLAIN_PRIVATE_KEY)
SSH_KEYPAIR_OBJECT = SSHKeypair(public_key="some_simple_public_key", private_key=PRIVATE_KEY)
SSH_KEYPAIR_DICT = {
    "public_key": "some_simple_public_key",
    "private_key": PLAIN_PRIVATE_KEY,
}


def test_ssh_keypair__serialization():
    assert SSH_KEYPAIR_OBJECT.to_json_dict() == SSH_KEYPAIR_DICT


def test_ssh_keypair__deserialization():
    assert SSHKeypair(**SSH_KEYPAIR_DICT) == SSH_KEYPAIR_OBJECT
