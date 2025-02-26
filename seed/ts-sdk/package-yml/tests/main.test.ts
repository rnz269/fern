/**
 * This file was auto-generated by Fern from our API Definition.
 */

import { SeedPackageYmlClient } from "../src/Client";

const client = new SeedPackageYmlClient({ environment: process.env.TESTS_BASE_URL || "test", id: "id" });

describe("SeedPackageYmlClient", () => {
    test("echo", async () => {
        const response = await client.echo("Hello world!");
        expect(response).toEqual("Hello world!");
    });
});
