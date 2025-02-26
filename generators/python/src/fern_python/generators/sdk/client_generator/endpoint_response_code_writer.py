import fern.ir.resources as ir_types
from typing_extensions import Never

from fern_python.codegen import AST
from fern_python.external_dependencies.httpx_sse import HttpxSSE
from fern_python.external_dependencies.json import Json
from fern_python.generators.sdk.context.sdk_generator_context import SdkGeneratorContext


class EndpointResponseCodeWriter:
    RESPONSE_VARIABLE = "_response"
    RESPONSE_JSON_VARIABLE = "_response_json"
    STREAM_TEXT_VARIABLE = "_text"
    FILE_CHUNK_VARIABLE = "_chunk"
    EVENT_SOURCE_VARIABLE = "_event_source"
    SSE_VARIABLE = "_sse"

    def __init__(
        self,
        *,
        context: SdkGeneratorContext,
        endpoint: ir_types.HttpEndpoint,
        is_async: bool,
    ):
        self._context = context
        self._endpoint = endpoint
        self._is_async = is_async

    def get_writer(self) -> AST.CodeWriter:
        def write(writer: AST.NodeWriter) -> None:
            self._context.ir.error_discrimination_strategy.visit(
                status_code=lambda: self._write_status_code_discriminated_response_handler(
                    writer=writer,
                ),
                property=lambda strategy: self._write_property_discriminated_response_handler(
                    writer=writer, strategy=strategy
                ),
            )

        return AST.CodeWriter(write)

    def _handle_success_stream(self, *, writer: AST.NodeWriter, stream_response: ir_types.StreamingResponse) -> None:
        stream_response_union = stream_response.get_as_union()
        if stream_response_union.type == "sse":
            writer.write(f"{EndpointResponseCodeWriter.EVENT_SOURCE_VARIABLE} = ")
            writer.write_node(
                AST.ClassInstantiation(
                    HttpxSSE.EVENT_SOURCE, [AST.Expression(EndpointResponseCodeWriter.RESPONSE_VARIABLE)]
                )
            )
            writer.write_newline_if_last_line_not()
            if self._is_async:
                writer.write("async ")
            writer.write_line(
                f"for {EndpointResponseCodeWriter.SSE_VARIABLE} in {EndpointResponseCodeWriter.EVENT_SOURCE_VARIABLE}.{self._get_iter_sse_method(is_async=self._is_async)}():"
            )
            with writer.indent():
                writer.write("yield ")
                writer.write_node(
                    self._context.core_utilities.get_construct(
                        self._get_streaming_response_data_type(stream_response),
                        AST.Expression(Json.loads(AST.Expression(f"{EndpointResponseCodeWriter.SSE_VARIABLE}.data"))),
                    ),
                )
        else:
            if self._is_async:
                writer.write("async ")
            writer.write_line(
                f"for {EndpointResponseCodeWriter.STREAM_TEXT_VARIABLE} in {EndpointResponseCodeWriter.RESPONSE_VARIABLE}.{self._get_iter_lines_method(is_async=self._is_async)}(): "
            )
            with writer.indent():
                writer.write_line(f"if len({EndpointResponseCodeWriter.STREAM_TEXT_VARIABLE}) == 0:")
                with writer.indent():
                    writer.write_line("continue")
                writer.write("yield ")
                writer.write_node(
                    self._context.core_utilities.get_construct(
                        self._get_streaming_response_data_type(stream_response),
                        AST.Expression(Json.loads(AST.Expression(EndpointResponseCodeWriter.STREAM_TEXT_VARIABLE))),
                    ),
                )

        writer.write_line("return")

    def _get_iter_lines_method(self, *, is_async: bool) -> str:
        if is_async:
            return "aiter_lines"
        else:
            return "iter_lines"

    def _get_iter_sse_method(self, *, is_async: bool) -> str:
        if is_async:
            return "aiter_sse"
        else:
            return "iter_sse"

    def _handle_success_json(
        self, *, writer: AST.NodeWriter, json_response: ir_types.JsonResponse, use_response_json: bool
    ) -> None:
        writer.write("return ")
        writer.write_node(
            self._context.core_utilities.get_construct(
                self._get_json_response_body_type(json_response),
                AST.Expression(
                    f"{EndpointResponseCodeWriter.RESPONSE_JSON_VARIABLE}"
                    if use_response_json
                    else f"{EndpointResponseCodeWriter.RESPONSE_VARIABLE}.json()"
                ),
            )
        )
        writer.write_newline_if_last_line_not()

    def _handle_success_text(
        self,
        *,
        writer: AST.NodeWriter,
    ) -> None:
        writer.write("return ")
        writer.write_node(AST.Expression(f"{EndpointResponseCodeWriter.RESPONSE_VARIABLE}.text"))
        writer.write("  # type: ignore ")
        writer.write_newline_if_last_line_not()

    def _handle_success_file_download(self, *, writer: AST.NodeWriter) -> None:
        if self._is_async:
            writer.write("async ")
        writer.write_line(
            f"for {EndpointResponseCodeWriter.FILE_CHUNK_VARIABLE} in {EndpointResponseCodeWriter.RESPONSE_VARIABLE}.{self._get_iter_bytes_method(is_async=self._is_async)}(): "
        )
        with writer.indent():
            writer.write(f"yield {EndpointResponseCodeWriter.FILE_CHUNK_VARIABLE}")
        writer.write_newline_if_last_line_not()
        writer.write_line("return")

    def _get_iter_bytes_method(self, *, is_async: bool) -> str:
        if is_async:
            return "aiter_bytes"
        else:
            return "iter_bytes"

    def _write_status_code_discriminated_response_handler(self, *, writer: AST.NodeWriter) -> None:
        writer.write_line(f"if 200 <= {EndpointResponseCodeWriter.RESPONSE_VARIABLE}.status_code < 300:")
        with writer.indent():
            if self._endpoint.response is None:
                writer.write_line("return")
            else:
                self._endpoint.response.visit(
                    json=lambda json_response: self._handle_success_json(
                        writer=writer, json_response=json_response, use_response_json=False
                    ),
                    streaming=lambda stream_response: self._handle_success_stream(
                        writer=writer, stream_response=stream_response
                    ),
                    file_download=lambda _: self._handle_success_file_download(writer=writer),
                    text=lambda _: self._handle_success_text(writer=writer),
                )

        # in streaming responses, we need to call read() or aread()
        # before deserializing or httpx will raise ResponseNotRead
        if self._endpoint.response is not None and (
            self._endpoint.response.get_as_union().type == "streaming"
            or self._endpoint.response.get_as_union().type == "fileDownload"
        ):
            writer.write_line(
                f"await {EndpointResponseCodeWriter.RESPONSE_VARIABLE}.aread()"
                if self._is_async
                else f"{EndpointResponseCodeWriter.RESPONSE_VARIABLE}.read()"
            )

        for error in self._endpoint.errors.get_as_list():
            error_declaration = self._context.ir.errors[error.error.error_id]

            writer.write_line(
                f"if {EndpointResponseCodeWriter.RESPONSE_VARIABLE}.status_code == {error_declaration.status_code}:"
            )
            with writer.indent():
                writer.write("raise ")
                writer.write_node(
                    AST.ClassInstantiation(
                        class_=self._context.get_reference_to_error(error.error),
                        args=[
                            self._context.core_utilities.get_construct(
                                self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                                    error_declaration.type
                                ),
                                AST.Expression(f"{EndpointResponseCodeWriter.RESPONSE_VARIABLE}.json()"),
                            )
                        ]
                        if error_declaration.type is not None
                        else None,
                    )
                )
                writer.write_newline_if_last_line_not()

        self._try_deserialize_json_response(writer=writer)

        writer.write("raise ")
        writer.write_node(
            self._context.core_utilities.instantiate_api_error(
                body=AST.Expression(EndpointResponseCodeWriter.RESPONSE_JSON_VARIABLE),
                status_code=AST.Expression(f"{EndpointResponseCodeWriter.RESPONSE_VARIABLE}.status_code"),
            )
        )
        writer.write_newline_if_last_line_not()

    def _write_property_discriminated_response_handler(
        self,
        *,
        writer: AST.NodeWriter,
        strategy: ir_types.ErrorDiscriminationByPropertyStrategy,
    ) -> None:
        if self._endpoint.response is not None:
            self._try_deserialize_json_response(writer=writer)

        writer.write_line(f"if 200 <= {EndpointResponseCodeWriter.RESPONSE_VARIABLE}.status_code < 300:")
        with writer.indent():
            if self._endpoint.response is None:
                writer.write_line("return")
            else:
                self._endpoint.response.visit(
                    json=lambda json_response: self._handle_success_json(
                        writer=writer, json_response=json_response, use_response_json=True
                    ),
                    streaming=lambda stream_response: self._handle_success_stream(
                        writer=writer, stream_response=stream_response
                    ),
                    file_download=lambda _: self._handle_success_file_download(writer=writer),
                    text=lambda _: self._handle_success_text(writer=writer),
                )

        if self._endpoint.response is None:
            self._try_deserialize_json_response(writer=writer)

        if len(self._endpoint.errors.get_as_list()) > 0:
            writer.write_line(
                f'if "{strategy.discriminant.wire_value}" in {EndpointResponseCodeWriter.RESPONSE_JSON_VARIABLE}:'
            )
            with writer.indent():
                for error in self._endpoint.errors.get_as_list():
                    error_declaration = self._context.ir.errors[error.error.error_id]

                    writer.write_line(
                        f'if {EndpointResponseCodeWriter.RESPONSE_JSON_VARIABLE}["{strategy.discriminant.wire_value}"] == "{error_declaration.discriminant_value.wire_value}":'
                    )
                    with writer.indent():
                        writer.write("raise ")
                        writer.write_node(
                            AST.ClassInstantiation(
                                class_=self._context.get_reference_to_error(error.error),
                                args=[
                                    self._context.core_utilities.get_construct(
                                        self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                                            error_declaration.type
                                        ),
                                        AST.Expression(
                                            f'{EndpointResponseCodeWriter.RESPONSE_JSON_VARIABLE}["{strategy.content_property.wire_value}"]'
                                        ),
                                    )
                                ]
                                if error_declaration.type is not None
                                else None,
                            )
                        )
                        writer.write_newline_if_last_line_not()

        writer.write("raise ")
        writer.write_node(
            self._context.core_utilities.instantiate_api_error(
                body=AST.Expression(EndpointResponseCodeWriter.RESPONSE_JSON_VARIABLE),
                status_code=AST.Expression(f"{EndpointResponseCodeWriter.RESPONSE_VARIABLE}.status_code"),
            )
        )
        writer.write_newline_if_last_line_not()

    def _deserialize_json_response(self, *, writer: AST.NodeWriter) -> None:
        writer.write_line(
            f"{EndpointResponseCodeWriter.RESPONSE_JSON_VARIABLE} = {EndpointResponseCodeWriter.RESPONSE_VARIABLE}.json()"
        )

    def _try_deserialize_json_response(self, *, writer: AST.NodeWriter) -> None:
        writer.write_line("try:")
        with writer.indent():
            self._deserialize_json_response(writer=writer)
        writer.write("except ")
        writer.write_reference(Json.JSONDecodeError())
        writer.write_line(":")
        with writer.indent():
            writer.write("raise ")
            writer.write_node(
                self._context.core_utilities.instantiate_api_error(
                    body=AST.Expression(f"{EndpointResponseCodeWriter.RESPONSE_VARIABLE}.text"),
                    status_code=AST.Expression(f"{EndpointResponseCodeWriter.RESPONSE_VARIABLE}.status_code"),
                )
            )
            writer.write_newline_if_last_line_not()

    def _get_response_body_type(self, response: ir_types.HttpResponse) -> AST.TypeHint:
        return response.visit(
            file_download=lambda _: AST.TypeHint.async_iterator(AST.TypeHint.bytes())
            if self._is_async
            else AST.TypeHint.iterator(AST.TypeHint.bytes()),
            json=lambda json_response: self._get_json_response_body_type(json_response),
            streaming=lambda streaming_response: self._get_streaming_response_data_type(streaming_response),
            text=lambda _: AST.TypeHint.str_(),
        )

    def _get_json_response_body_type(
        self,
        json_response: ir_types.JsonResponse,
    ) -> AST.TypeHint:
        return json_response.visit(
            response=lambda response: self._context.pydantic_generator_context.get_type_hint_for_type_reference(
                response.response_body_type
            ),
            nested_property_as_response=lambda _: raise_json_nested_property_as_response_unsupported(),
        )

    def _get_streaming_response_data_type(self, streaming_response: ir_types.StreamingResponse) -> AST.TypeHint:
        union = streaming_response.get_as_union()
        if union.type == "json":
            return self._context.pydantic_generator_context.get_type_hint_for_type_reference(union.payload)
        if union.type == "sse":
            return self._context.pydantic_generator_context.get_type_hint_for_type_reference(union.payload)
        if union.type == "text":
            return AST.TypeHint.str_()
        raise RuntimeError(f"{union.type} streaming response is unsupported")


def raise_json_nested_property_as_response_unsupported() -> Never:
    raise RuntimeError("nested property json response is unsupported")
