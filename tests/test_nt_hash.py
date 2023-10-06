import pytest

from monkeytypes import NTHash


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
