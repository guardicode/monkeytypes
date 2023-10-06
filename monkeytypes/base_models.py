from collections.abc import Sequence

from pydantic import BaseModel, ValidationError, ConfigDict


InfectionMonkeyModelConfig = ConfigDict(frozen=True, extra="forbid")

MutableInfectionMonkeyModelConfig = ConfigDict(froze=False, validate_assignment=True)


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
            # `pydantic.ValueError` to be raised would couple other modules to pydantic, which is
            # undesirable. This exception handler re-raises the first validation error that pydantic
            # encountered. This allows users of these models to `except` `TypeError` or `ValueError`
            # and handle them. Pydantic-specific errors are still raised, but they inherit from
            # `TypeError` or `ValueError`.
            e = err.raw_errors[0]
            while isinstance(e, Sequence):
                e = e[0]
            error = e.exc
            if hasattr(e, "_loc"):
                error.args = (f"{e._loc} {error}",)
            raise error


class MutableInfectionMonkeyBaseModel(InfectionMonkeyBaseModel):
    model_config = MutableInfectionMonkeyModelConfig
