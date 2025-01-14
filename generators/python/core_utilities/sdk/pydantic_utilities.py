import pydantic

IS_PYDANTIC_V2 = pydantic.VERSION.startswith("2.")

if IS_PYDANTIC_V2:
    import pydantic.v1 as pydantic_v1  # type: ignore  # nopycln: import
else:
    import pydantic as pydantic_v1  # type: ignore  # nopycln: import

__all__ = ["pydantic_v1"]
