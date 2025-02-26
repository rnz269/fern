/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../..";
import * as FernIr from "../../../../api";
import * as core from "../../../../core";

export const ExamplePrimitive: core.serialization.Schema<serializers.ExamplePrimitive.Raw, FernIr.ExamplePrimitive> =
    core.serialization
        .union("type", {
            integer: core.serialization.object({
                integer: core.serialization.number(),
            }),
            double: core.serialization.object({
                double: core.serialization.number(),
            }),
            string: core.serialization.object({
                string: core.serialization.lazyObject(async () => (await import("../../..")).EscapedString),
            }),
            boolean: core.serialization.object({
                boolean: core.serialization.boolean(),
            }),
            long: core.serialization.object({
                long: core.serialization.number(),
            }),
            datetime: core.serialization.object({
                datetime: core.serialization.date(),
            }),
            date: core.serialization.object({
                date: core.serialization.string(),
            }),
            uuid: core.serialization.object({
                uuid: core.serialization.string(),
            }),
        })
        .transform<FernIr.ExamplePrimitive>({
            transform: (value) => {
                switch (value.type) {
                    case "integer":
                        return FernIr.ExamplePrimitive.integer(value.integer);
                    case "double":
                        return FernIr.ExamplePrimitive.double(value.double);
                    case "string":
                        return FernIr.ExamplePrimitive.string(value.string);
                    case "boolean":
                        return FernIr.ExamplePrimitive.boolean(value.boolean);
                    case "long":
                        return FernIr.ExamplePrimitive.long(value.long);
                    case "datetime":
                        return FernIr.ExamplePrimitive.datetime(value.datetime);
                    case "date":
                        return FernIr.ExamplePrimitive.date(value.date);
                    case "uuid":
                        return FernIr.ExamplePrimitive.uuid(value.uuid);
                    default:
                        return value as FernIr.ExamplePrimitive;
                }
            },
            untransform: ({ _visit, ...value }) => value as any,
        });

export declare namespace ExamplePrimitive {
    type Raw =
        | ExamplePrimitive.Integer
        | ExamplePrimitive.Double
        | ExamplePrimitive.String
        | ExamplePrimitive.Boolean
        | ExamplePrimitive.Long
        | ExamplePrimitive.Datetime
        | ExamplePrimitive.Date
        | ExamplePrimitive.Uuid;

    interface Integer {
        type: "integer";
        integer: number;
    }

    interface Double {
        type: "double";
        double: number;
    }

    interface String {
        type: "string";
        string: serializers.EscapedString.Raw;
    }

    interface Boolean {
        type: "boolean";
        boolean: boolean;
    }

    interface Long {
        type: "long";
        long: number;
    }

    interface Datetime {
        type: "datetime";
        datetime: string;
    }

    interface Date {
        type: "date";
        date: string;
    }

    interface Uuid {
        type: "uuid";
        uuid: string;
    }
}
