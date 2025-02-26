# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...core.pydantic_utilities import pydantic_v1


class ProblemDescriptionBoard_Html(pydantic_v1.BaseModel):
    type: typing.Literal["html"] = "html"
    value: str


class ProblemDescriptionBoard_Variable(pydantic_v1.BaseModel):
    type: typing.Literal["variable"] = "variable"
    value: VariableValue


class ProblemDescriptionBoard_TestCaseId(pydantic_v1.BaseModel):
    type: typing.Literal["testCaseId"] = "testCaseId"
    value: str


ProblemDescriptionBoard = typing.Union[
    ProblemDescriptionBoard_Html, ProblemDescriptionBoard_Variable, ProblemDescriptionBoard_TestCaseId
]
from ..commons.variable_value import VariableValue  # noqa: E402
