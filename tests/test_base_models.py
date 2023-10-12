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
