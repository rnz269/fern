/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as SeedEnum from "../../api/index";
import * as core from "../../core";

export const ColorOrOperand: core.serialization.Schema<serializers.ColorOrOperand.Raw, SeedEnum.ColorOrOperand> =
    core.serialization.undiscriminatedUnion([
        core.serialization.lazy(async () => (await import("..")).Color),
        core.serialization.lazy(async () => (await import("..")).Operand),
    ]);

export declare namespace ColorOrOperand {
    type Raw = serializers.Color.Raw | serializers.Operand.Raw;
}
