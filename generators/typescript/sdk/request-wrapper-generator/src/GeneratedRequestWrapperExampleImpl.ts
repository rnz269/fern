import { ExampleEndpointCall, Name, TypeReference } from "@fern-fern/ir-sdk/api";
import { GetReferenceOpts, PackageId } from "@fern-typescript/commons";
import { GeneratedRequestWrapperExample, SdkContext } from "@fern-typescript/contexts";
import { ts } from "ts-morph";

export declare namespace GeneratedRequestWrapperExampleImpl {
    export interface Init {
        bodyPropertyName: string;
        example: ExampleEndpointCall;
        packageId: PackageId;
        endpointName: Name;
    }
}

export class GeneratedRequestWrapperExampleImpl implements GeneratedRequestWrapperExample {
    private bodyPropertyName: string;
    private example: ExampleEndpointCall;
    private packageId: PackageId;
    private endpointName: Name;

    constructor({ bodyPropertyName, example, packageId, endpointName }: GeneratedRequestWrapperExampleImpl.Init) {
        this.bodyPropertyName = bodyPropertyName;
        this.example = example;
        this.packageId = packageId;
        this.endpointName = endpointName;
    }

    public build(context: SdkContext, opts: GetReferenceOpts): ts.Expression {
        return this.buildExample({ context, opts });
    }

    private buildExample({ context, opts }: { context: SdkContext; opts: GetReferenceOpts }): ts.Expression {
        // We may need to wrap it in quotes if it contains special characters
        // These get placed in the object literal as keys, so they may need to be strings
        const asObjectProperty = (value: string) => {
            const regex = /^[a-zA-Z_][a-zA-Z0-9_]*$/;
            if (regex.test(value)) {
                return value;
            }
            return ts.factory.createStringLiteral(value);
        };

        const generatedType = context.requestWrapper.getGeneratedRequestWrapper(this.packageId, this.endpointName);
        const headerProperties = [...this.example.serviceHeaders, ...this.example.endpointHeaders].map((header) => {
            return ts.factory.createPropertyAssignment(
                asObjectProperty(generatedType.getPropertyNameOfNonLiteralHeaderFromName(header.name).propertyName),
                context.type.getGeneratedExample(header.value).build(context, opts)
            );
        });
        const queryParamProperties = [...this.example.queryParameters].map((queryParam) => {
            return ts.factory.createPropertyAssignment(
                asObjectProperty(generatedType.getPropertyNameOfQueryParameterFromName(queryParam.name).propertyName),
                context.type.getGeneratedExample(queryParam.value).build(context, opts)
            );
        });
        const bodyProperties =
            this.example.request?._visit<ts.PropertyAssignment[]>({
                inlinedRequestBody: (body) => {
                    return body.properties.map((property) => {
                        if (property.originalTypeDeclaration != null) {
                            const originalTypeForProperty = context.type.getGeneratedType(
                                property.originalTypeDeclaration
                            );
                            if (originalTypeForProperty.type === "union") {
                                const propertyKey = originalTypeForProperty.getSinglePropertyKey({
                                    name: property.name,
                                    type: TypeReference.named(property.originalTypeDeclaration)
                                });
                                return ts.factory.createPropertyAssignment(
                                    propertyKey,
                                    context.type.getGeneratedExample(property.value).build(context, opts)
                                );
                            }
                            if (originalTypeForProperty.type !== "object") {
                                throw new Error(
                                    `Property does not come from an object, instead got ${originalTypeForProperty.type}`
                                );
                            }
                            const key = originalTypeForProperty.getPropertyKey({
                                propertyWireKey: property.name.wireValue
                            });
                            return ts.factory.createPropertyAssignment(
                                key,
                                context.type.getGeneratedExample(property.value).build(context, opts)
                            );
                        } else {
                            return ts.factory.createPropertyAssignment(
                                asObjectProperty(generatedType.getInlinedRequestBodyPropertyKeyFromName(property.name)),
                                context.type.getGeneratedExample(property.value).build(context, opts)
                            );
                        }
                    });
                },
                reference: (type) => {
                    return [
                        ts.factory.createPropertyAssignment(
                            this.bodyPropertyName,
                            context.type.getGeneratedExample(type).build(context, opts)
                        )
                    ];
                },
                _other: () => {
                    throw new Error("Encountered unknown example request type");
                }
            }) ?? [];

        return ts.factory.createObjectLiteralExpression(
            [...headerProperties, ...queryParamProperties, ...bodyProperties],
            true
        );
    }
}
