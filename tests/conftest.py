from typing import Any, Union

import pytest


@pytest.fixture(scope="session")
def valid_ntlm_hash() -> str:
    return "E520AC67419A9A224A3B108F3FA6CB6D"


@pytest.fixture(scope="session")
def invalid_value_ntlm_hashes() -> list[str]:
    return [
        "invalid",
        "0123456789012345678901234568901",
        "E52GAC67419A9A224A3B108F3FA6CB6D",
    ]


@pytest.fixture(scope="session")
def invalid_type_ntlm_hashes() -> list[Union[int, Any]]:
    return [
        0,
        1,
        2.0,
        None,
        b"abc",
    ]
