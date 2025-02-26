# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .....core.pydantic_utilities import pydantic_v1
from ....commons.variable_type import VariableType
from .parameter import Parameter


class FunctionSignature_Void(pydantic_v1.BaseModel):
    type: typing.Literal["void"] = "void"
    parameters: typing.List[Parameter]


class FunctionSignature_NonVoid(pydantic_v1.BaseModel):
    type: typing.Literal["nonVoid"] = "nonVoid"
    parameters: typing.List[Parameter]
    return_type: VariableType = pydantic_v1.Field(alias="returnType")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class FunctionSignature_VoidThatTakesActualResult(pydantic_v1.BaseModel):
    type: typing.Literal["voidThatTakesActualResult"] = "voidThatTakesActualResult"
    parameters: typing.List[Parameter]
    actual_result_type: VariableType = pydantic_v1.Field(alias="actualResultType")

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


FunctionSignature = typing.Union[
    FunctionSignature_Void, FunctionSignature_NonVoid, FunctionSignature_VoidThatTakesActualResult
]
