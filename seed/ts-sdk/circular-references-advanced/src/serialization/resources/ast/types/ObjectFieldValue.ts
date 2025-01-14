/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedApi from "../../../../api/index";
import * as core from "../../../../core";
import { FieldName } from "./FieldName";

export const ObjectFieldValue: core.serialization.ObjectSchema<
    serializers.ObjectFieldValue.Raw,
    SeedApi.ObjectFieldValue
> = core.serialization.object({
    name: FieldName,
    value: core.serialization.lazy(async () => (await import("../../..")).FieldValue),
});

export declare namespace ObjectFieldValue {
    interface Raw {
        name: FieldName.Raw;
        value: serializers.FieldValue.Raw;
    }
}
