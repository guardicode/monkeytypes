import pytest
from typing import Optional
from monkeytypes import MutableInfectionMonkeyBaseModel


class FloatModel(MutableInfectionMonkeyBaseModel):
    number: float


class MutableModel(MutableInfectionMonkeyBaseModel):
    float_model: Optional[FloatModel]


def test_base_model__set_value_error():
    ValueFloatModel = FloatModel(number=4.1)
    with pytest.raises(ValueError):
        ValueFloatModel.number = "adsfasdfa"


def test_base_model__set_type_error():
    Test2Model = MutableModel(float_model=None)
    with pytest.raises(TypeError):
        Test2Model.float_model = "adsfasdfa"
