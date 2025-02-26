# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...core.pydantic_utilities import pydantic_v1
from ..commons.variable_value import VariableValue
from .exception_v_2 import ExceptionV2


class TestCaseGrade_Hidden(pydantic_v1.BaseModel):
    type: typing.Literal["hidden"] = "hidden"
    passed: bool


class TestCaseGrade_NonHidden(pydantic_v1.BaseModel):
    type: typing.Literal["nonHidden"] = "nonHidden"
    passed: bool
    actual_result: typing.Optional[VariableValue] = pydantic_v1.Field(alias="actualResult")
    exception: typing.Optional[ExceptionV2]
    stdout: str

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


TestCaseGrade = typing.Union[TestCaseGrade_Hidden, TestCaseGrade_NonHidden]
