# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import pydantic_v1
from .test_submission_status_v_2 import TestSubmissionStatusV2
from .workspace_submission_status_v_2 import WorkspaceSubmissionStatusV2

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def test(self, value: TestSubmissionStatusV2) -> SubmissionStatusV2:
        return SubmissionStatusV2(__root__=_SubmissionStatusV2.Test(**value.dict(exclude_unset=True), type="test"))

    def workspace(self, value: WorkspaceSubmissionStatusV2) -> SubmissionStatusV2:
        return SubmissionStatusV2(
            __root__=_SubmissionStatusV2.Workspace(**value.dict(exclude_unset=True), type="workspace")
        )


class SubmissionStatusV2(pydantic_v1.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_SubmissionStatusV2.Test, _SubmissionStatusV2.Workspace]:
        return self.__root__

    def visit(
        self,
        test: typing.Callable[[TestSubmissionStatusV2], T_Result],
        workspace: typing.Callable[[WorkspaceSubmissionStatusV2], T_Result],
    ) -> T_Result:
        if self.__root__.type == "test":
            return test(TestSubmissionStatusV2(**self.__root__.dict(exclude_unset=True, exclude={"type"})))
        if self.__root__.type == "workspace":
            return workspace(WorkspaceSubmissionStatusV2(**self.__root__.dict(exclude_unset=True, exclude={"type"})))

    __root__: typing_extensions.Annotated[
        typing.Union[_SubmissionStatusV2.Test, _SubmissionStatusV2.Workspace], pydantic_v1.Field(discriminator="type")
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic_v1.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _SubmissionStatusV2:
    class Test(TestSubmissionStatusV2):
        type: typing.Literal["test"] = "test"

        class Config:
            allow_population_by_field_name = True
            populate_by_name = True

    class Workspace(WorkspaceSubmissionStatusV2):
        type: typing.Literal["workspace"] = "workspace"

        class Config:
            allow_population_by_field_name = True
            populate_by_name = True


SubmissionStatusV2.update_forward_refs()
