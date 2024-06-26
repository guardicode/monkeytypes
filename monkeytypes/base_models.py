import re
from typing import Any, Self, Union

from pydantic import BaseModel, ConfigDict, ValidationError

INVALID_UNION_MEMBER_ERROR = "invalid_union_member"

TYPE_ERROR_LIST = [r"\w+_type", "int_from_float", "is_instance_of", "is_subcass_of"]
ILLEGAL_MUTATION_LIST = ["frozen_field", "frozen_instance"]


class IllegalMutationError(RuntimeError):
    """
    Raised when an error occurs during illegal mutation of fields

    """


InfectionMonkeyModelConfig = ConfigDict(frozen=True, extra="forbid")

MutableInfectionMonkeyModelConfig = ConfigDict(
    **{
        **InfectionMonkeyModelConfig,
        "frozen": False,
        "validate_assignment": True,
    }
)


class InfectionMonkeyBaseModel(BaseModel):
    model_config = InfectionMonkeyModelConfig

    def __init__(self, **kwargs):
        try:
            super().__init__(**kwargs)
        except ValidationError as err:
            # TLDR: This exception handler allows users of this class to be decoupled from pydantic.
            #
            # When validation of a pydantic object fails, pydantic raises a `ValidationError`, which
            # is a `ValueError`, even if the real cause was a `TypeError`. Furthermore, allowing
            # `pydantic.ValidationError` to be raised would couple other modules to pydantic, which
            # is undesirable. This exception handler re-raises the first validation error that
            # pydantic encountered, allowing users of these models to `except` `TypeError` or
            # `ValueError` as appropriate.
            #
            # From version 2, Pydantic doesn't offer any way to decouple from ValidationError
            # but it offers certain type names from which we can choose which errors to
            # raise to decouple from ValidationError.
            # This may not be needed if pydantic fixes and merges this:
            # https://github.com/pydantic/pydantic/issues/6498
            self._raise_type_or_value_error(err)

    def __setattr__(self, name: str, value: Any):
        try:
            super().__setattr__(name, value)
        except ValidationError as err:
            e = err.errors()[0]
            if e["type"] in ILLEGAL_MUTATION_LIST:
                raise IllegalMutationError(e["msg"]) from err

            self._raise_type_or_value_error(err)

    @staticmethod
    def _raise_type_or_value_error(error: ValidationError):
        e = error.errors()[0]
        for pattern in TYPE_ERROR_LIST:
            if re.match(pattern, e["type"]):
                raise TypeError(
                    f"{e['msg']}, got `{type(e['input']).__name__}` in {e['loc']}"
                ) from error

        raise ValueError(e["msg"]) from error

    def to_json_dict(self) -> dict[str, Any]:
        return self.model_dump(mode="json", by_alias=True)

    def to_dict(self) -> dict[str, Any]:
        return self.model_dump()

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True)

    def from_json(self, json_data: Union[str, bytes, bytearray]) -> Self:
        return self.model_validate_json(json_data)

    # NOTE: The copy() method's signature is incompatible with the the
    #       supertype's definition (BaseModel). However, the supertype's
    #       `copy()` method is deprecated, so we'll ignore the issue as it will
    #       eventually resolve itself, and this is the interface we wish to
    #       provide.
    def copy(self) -> Self:  # type: ignore [override]
        return self.model_copy()

    def deep_copy(self) -> Self:
        return self.model_copy(deep=True)


class MutableInfectionMonkeyBaseModel(InfectionMonkeyBaseModel):
    model_config = MutableInfectionMonkeyModelConfig
