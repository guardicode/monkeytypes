import pytest
from pydantic import SecretStr

from monkeytypes import LMHash

LM_HASH = SecretStr("E520AC67419A9A224A3B108F3FA6CB6D")
LM_HASH_OBJECT = LMHash(lm_hash=LM_HASH)
LM_HASH_DICT = {"lm_hash": "E520AC67419A9A224A3B108F3FA6CB6D"}


def test_lm_hash__serialization():
    assert LM_HASH_OBJECT.to_json_dict() == LM_HASH_DICT


def test_lm_hash__deserialization():
    assert LMHash(**LM_HASH_DICT) == LM_HASH_OBJECT


def test_construct_valid_nt_hash(valid_ntlm_hash):
    # This test will fail if an exception is raised
    LMHash(lm_hash=valid_ntlm_hash)


def test_construct_invalid_nt_hash_value(invalid_value_ntlm_hashes):
    for invalid_hash in invalid_value_ntlm_hashes:
        with pytest.raises(ValueError):
            LMHash(lm_hash=invalid_hash)


def test_construct_invalid_nt_hash_type(invalid_type_ntlm_hashes):
    for invalid_hash in invalid_type_ntlm_hashes:
        with pytest.raises(TypeError):
            LMHash(lm_hash=invalid_hash)
