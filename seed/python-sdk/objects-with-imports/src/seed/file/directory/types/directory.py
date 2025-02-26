# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import pydantic_v1
from ...types.file import File


class Directory(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from seed import File
    from seed.file import Directory

    Directory(
        name="root",
        files=[
            File(
                name="file.txt",
                contents="...",
                info="REGULAR",
            )
        ],
        directories=[
            Directory(
                name="tmp",
                files=[
                    File(
                        name="another_file.txt",
                        contents="...",
                        info="REGULAR",
                    )
                ],
            )
        ],
    )
    """

    name: str
    files: typing.Optional[typing.List[File]] = None
    directories: typing.Optional[typing.List[Directory]] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


Directory.update_forward_refs()
