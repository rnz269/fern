# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1


class Base(pydantic_v1.BaseModel):
    id: str

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class UnionWithBaseProperties_Integer(Base):
    type: typing.Literal["integer"] = "integer"
    value: int

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class UnionWithBaseProperties_String(Base):
    type: typing.Literal["string"] = "string"
    value: str

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


class UnionWithBaseProperties_Foo(Base):
    type: typing.Literal["foo"] = "foo"
    name: str

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True


UnionWithBaseProperties = typing.Union[
    UnionWithBaseProperties_Integer, UnionWithBaseProperties_String, UnionWithBaseProperties_Foo
]
