/**
 * This file was auto-generated by Fern from our API Definition.
 */

import { SeedLiteralClient } from "../src/Client";

const client = new SeedLiteralClient({ environment: process.env.TESTS_BASE_URL || "test" });

describe("Headers", () => {
    test("send", async () => {
        const response = await client.headers.send({
            endpointVersion: "02-12-2024",
            async: true,
            query: "What is the weather today",
        });
        expect(response).toEqual({ message: "The weather is sunny", status: 200, success: true });
    });
});
