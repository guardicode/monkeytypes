import pytest
from pydantic import SecretStr

from monkeytypes import NTHash

NT_HASH = SecretStr("E520AC67419A9A224A3B108F3FA6CB6D")
NT_HASH_OBJECT = NTHash(nt_hash=NT_HASH)
NT_HASH_DICT = {"nt_hash": "E520AC67419A9A224A3B108F3FA6CB6D"}


def test_nt_hash__serialization():
    assert NT_HASH_OBJECT.model_dump(mode="json") == NT_HASH_DICT


def test_nt_hash__deserialization():
    assert NTHash(**NT_HASH_DICT) == NT_HASH_OBJECT


def test_construct_valid_nt_hash(valid_ntlm_hash):
    # This test will fail if an exception is raised
    NTHash(nt_hash=valid_ntlm_hash)


def test_construct_invalid_nt_hash_value(invalid_value_ntlm_hashes):
    for invalid_hash in invalid_value_ntlm_hashes:
        with pytest.raises(ValueError):
            NTHash(nt_hash=invalid_hash)


def test_construct_invalid_nt_hash_type(invalid_type_ntlm_hashes):
    for invalid_hash in invalid_type_ntlm_hashes:
        with pytest.raises(TypeError):
            NTHash(nt_hash=invalid_hash)
