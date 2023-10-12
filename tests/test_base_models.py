from typing import Optional

import pytest

from monkeytypes import (
    InfectionMonkeyBaseModel,
    InfectionMonkeyModelConfig,
    MutableInfectionMonkeyBaseModel,
    MutableInfectionMonkeyModelConfig,
)


class FloatModel(MutableInfectionMonkeyBaseModel):
    number: float


class MutableModel(MutableInfectionMonkeyBaseModel):
    float_model: Optional[FloatModel]


METHODS_DICT = {"example_field": 42.0}
METHODS_JSON = '{"example_field":42.0}'
METHODS_NOT_VALID_JSON = '{"example_field": "not_an_int"}'


class MethodsModel(InfectionMonkeyBaseModel):
    example_field: float


@pytest.fixture
def methods_model():
    return MethodsModel(example_field=42.0)


def test_set_value_error():
    ValueFloatModel = FloatModel(number=4.1)
    with pytest.raises(ValueError):
        ValueFloatModel.number = "adsfasdfa"


def test_set_type_error():
    Test2Model = MutableModel(float_model=None)
    with pytest.raises(TypeError):
        Test2Model.float_model = "adsfasdfa"


def test_immutable_base_model_config_update():
    class MutableConfigModel(MutableInfectionMonkeyBaseModel):
        model_config = {"title": "GreatTitle"}

    assert all(
        MutableConfigModel.model_config.get(key) == value
        for key, value in MutableInfectionMonkeyModelConfig.items()
    )


def test_mutable_base_model_config_update():
    class ImmutableMutableConfigModel(InfectionMonkeyBaseModel):
        model_config = {"title": "AnotherGreatTitle"}

    assert all(
        ImmutableMutableConfigModel.model_config.get(key) == value
        for key, value in InfectionMonkeyModelConfig.items()
    )


def test_base_model_to_json_dict(methods_model):
    assert methods_model.to_json_dict() == METHODS_DICT


def test_base_model_to_dict(methods_model):
    assert methods_model.to_dict() == METHODS_DICT


def test_base_model_to_json(methods_model):
    assert methods_model.to_json() == METHODS_JSON


def test_base_model_from_json(methods_model):
    assert methods_model == methods_model.from_json(METHODS_JSON)


def test_base_model_from_json_invalid(methods_model):
    with pytest.raises(ValueError):
        methods_model.from_json(METHODS_NOT_VALID_JSON)


def test_base_model_copy(methods_model):
    assert methods_model == methods_model.copy()


def test_base_model_deep_copy(methods_model):
    assert methods_model == methods_model.deep_copy()
