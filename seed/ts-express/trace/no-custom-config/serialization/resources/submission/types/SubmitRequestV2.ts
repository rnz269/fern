/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../../../index";
import * as SeedTrace from "../../../../api/index";
import * as core from "../../../../core";

export const SubmitRequestV2: core.serialization.ObjectSchema<
    serializers.SubmitRequestV2.Raw,
    SeedTrace.SubmitRequestV2
> = core.serialization.object({
    submissionId: core.serialization.lazy(async () => (await import("../../..")).SubmissionId),
    language: core.serialization.lazy(async () => (await import("../../..")).Language),
    submissionFiles: core.serialization.list(
        core.serialization.lazyObject(async () => (await import("../../..")).SubmissionFileInfo)
    ),
    problemId: core.serialization.lazy(async () => (await import("../../..")).ProblemId),
    problemVersion: core.serialization.number().optional(),
    userId: core.serialization.string().optional(),
});

export declare namespace SubmitRequestV2 {
    interface Raw {
        submissionId: serializers.SubmissionId.Raw;
        language: serializers.Language.Raw;
        submissionFiles: serializers.SubmissionFileInfo.Raw[];
        problemId: serializers.ProblemId.Raw;
        problemVersion?: number | null;
        userId?: string | null;
    }
}
