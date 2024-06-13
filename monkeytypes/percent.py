from typing import Annotated, Any, Self, TypeAlias

from annotated_types import Le
from pydantic import Field, GetCoreSchemaHandler
from pydantic import NonNegativeFloat as PydanticNonNegativeFloat
from pydantic_core import core_schema

NonNegativeFloat: TypeAlias = PydanticNonNegativeFloat


class Percent(NonNegativeFloat):
    """
    A percentage greater than 0.0

    Note that percentages can be greater than 100. For example, I may have consumed 120% of my quota
    (if quotas aren't strictly enforced).
    """

    # This __init__() is required so that instances of Percent can be created. If you try to create
    # an instance of NonNegativeFloat, no validation is performed.
    def __init__(self, v: Any):
        Percent._validate_range(v)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls.validate,
            handler(
                Annotated[NonNegativeFloat, Field(description="A percentage greater than 0.0")]
            ),
        )

    @classmethod
    def validate(cls, v: Any) -> Self:
        cls._validate_range(v)

        # This is required so that floats passed into pydantic models are converted to instances of
        # Percent objects.
        return cls(v)

    @staticmethod
    def _validate_range(v: Any):
        if v < 0:
            raise ValueError("value must be non-negative")

    def as_decimal_fraction(self) -> NonNegativeFloat:
        """
        Return the percentage as a decimal fraction

        Example: 50% -> 0.5

        return: The percentage as a decimal fraction
        """
        return self / 100.0


class PercentLimited(Percent):
    """
    A percentage between 0.0 and 100.0
    """

    def __init__(self, v: Any):
        PercentLimited._validate_range(v)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls.validate,
            handler(
                Annotated[
                    NonNegativeFloat,
                    Le(100),
                    Field(description="A percentage between 0.0 and 100.0"),
                ]
            ),
        )

    @staticmethod
    def _validate_range(v: Any):
        if not (0.0 <= v <= 100.0):
            raise ValueError("value must be between 0 and 100")
