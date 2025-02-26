import { OAuthRefreshEndpoint } from "@fern-api/ir-sdk";
import { FernFileContext } from "../FernFileContext";
import { IdGenerator } from "../IdGenerator";
import { EndpointResolver } from "../resolvers/EndpointResolver";
import { PropertyResolver } from "../resolvers/PropertyResolver";
import { RefreshTokenEndpoint } from "./convertOAuthUtils";

export async function convertOAuthRefreshEndpoint({
    endpointResolver,
    propertyResolver,
    file,
    refreshTokenEndpoint
}: {
    endpointResolver: EndpointResolver;
    propertyResolver: PropertyResolver;
    file: FernFileContext;
    refreshTokenEndpoint: RefreshTokenEndpoint;
}): Promise<OAuthRefreshEndpoint | undefined> {
    const resolvedEndpoint = endpointResolver.resolveEndpointOrThrow({
        endpoint: refreshTokenEndpoint.endpoint,
        file
    });
    return {
        endpointReference: IdGenerator.generateEndpointIdFromResolvedEndpoint(resolvedEndpoint),
        requestProperties: {
            refreshToken: await propertyResolver.resolveRequestPropertyOrThrow({
                file,
                endpoint: refreshTokenEndpoint.endpoint,
                propertyComponents: refreshTokenEndpoint.requestProperties.refresh_token
            })
        },
        responseProperties: {
            accessToken: await propertyResolver.resolveResponsePropertyOrThrow({
                file,
                endpoint: refreshTokenEndpoint.endpoint,
                propertyComponents: refreshTokenEndpoint.responseProperties.access_token
            }),
            expiresIn:
                refreshTokenEndpoint.responseProperties.expires_in != null
                    ? await propertyResolver.resolveResponsePropertyOrThrow({
                          file,
                          endpoint: refreshTokenEndpoint.endpoint,
                          propertyComponents: refreshTokenEndpoint.responseProperties.expires_in
                      })
                    : undefined,
            refreshToken:
                refreshTokenEndpoint.responseProperties.refresh_token != null
                    ? await propertyResolver.resolveResponsePropertyOrThrow({
                          file,
                          endpoint: refreshTokenEndpoint.endpoint,
                          propertyComponents: refreshTokenEndpoint.responseProperties.refresh_token
                      })
                    : undefined
        }
    };
}
