# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..types.color_or_operand import ColorOrOperand
from ..types.operand import Operand


class PathParamClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def send(
        self,
        operand: Operand,
        maybe_operand: typing.Optional[Operand],
        operand_or_color: ColorOrOperand,
        maybe_operand_or_color: typing.Optional[ColorOrOperand],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        operand : Operand

        maybe_operand : typing.Optional[Operand]

        operand_or_color : ColorOrOperand

        maybe_operand_or_color : typing.Optional[ColorOrOperand]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from seed.client import SeedEnum

        client = SeedEnum(
            base_url="https://yourhost.com/path/to/api",
        )
        client.path_param.send(
            operand=">",
            maybe_operand="less_than",
            operand_or_color="red",
            maybe_operand_or_color="red",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"path/{jsonable_encoder(operand)}/{jsonable_encoder(maybe_operand)}/{jsonable_encoder(operand_or_color)}/{jsonable_encoder(maybe_operand_or_color)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPathParamClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def send(
        self,
        operand: Operand,
        maybe_operand: typing.Optional[Operand],
        operand_or_color: ColorOrOperand,
        maybe_operand_or_color: typing.Optional[ColorOrOperand],
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        operand : Operand

        maybe_operand : typing.Optional[Operand]

        operand_or_color : ColorOrOperand

        maybe_operand_or_color : typing.Optional[ColorOrOperand]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from seed.client import AsyncSeedEnum

        client = AsyncSeedEnum(
            base_url="https://yourhost.com/path/to/api",
        )
        await client.path_param.send(
            operand=">",
            maybe_operand="less_than",
            operand_or_color="red",
            maybe_operand_or_color="red",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"path/{jsonable_encoder(operand)}/{jsonable_encoder(maybe_operand)}/{jsonable_encoder(operand_or_color)}/{jsonable_encoder(maybe_operand_or_color)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
