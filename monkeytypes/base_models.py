import re
from typing import Any
from pydantic import BaseModel, ValidationError

TYPE_ERROR_LIST = [r"\w+_type", "int_from_float", "is_instance_of", "is_subcass_of"]
ILLEGAL_MUTATION_LIST = ["frozen_field", "frozen_instance"]


class IllegalMutationError(RuntimeError):
    """
    Raised when an error occurs during illegal mutation of fields

    """

    pass


InfectionMonkeyModelConfig = {"frozen": True, "extra": "forbid"}

MutableInfectionMonkeyModelConfig = {
    **InfectionMonkeyModelConfig,
    "frozen": False,
    "validate_assignment": True,
}


class InfectionMonkeyBaseModel(BaseModel):
    model_config = InfectionMonkeyModelConfig

    def __init__(self, **kwargs):
        try:
            super().__init__(**kwargs)
        except ValidationError as err:
            # TLDR: This exception handler allows users of this class to be decoupled from pydantic.
            #
            # From version 2, Pydantic doesn't offer any way to decouple from ValidationError
            # but it offers certain type names from which we can choose what errors should we
            # raise to decouple from ValidationError.
            # This may not be needed if pydantic fix and merge this:
            # https://github.com/pydantic/pydantic/issues/6498
            e = err.errors()[0]
            for pattern in TYPE_ERROR_LIST:
                if re.match(pattern, e["type"]):
                    raise TypeError(e["msg"]) from err

            raise ValueError(e["msg"]) from err

    def __setattr__(self, name: str, value: Any):
        try:
            super().__setattr__(name, value)
        except ValidationError as err:
            e = err.errors()[0]
            if e["type"] in ILLEGAL_MUTATION_LIST:
                raise IllegalMutationError(e["msg"]) from err

            for pattern in TYPE_ERROR_LIST:
                if re.match(pattern, e["type"]):
                    raise TypeError(e["msg"]) from err

            raise ValueError(e["msg"]) from err


class MutableInfectionMonkeyBaseModel(InfectionMonkeyBaseModel):
    model_config = MutableInfectionMonkeyModelConfig
