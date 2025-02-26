/**
 * This file was auto-generated by Fern from our API Definition.
 */
package com.seed.extraProperties.types;

import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.seed.extraProperties.core.ObjectMappers;
import java.util.Map;

public final class Failure {
    private final Map<String, Object> additionalProperties;

    private Failure(Map<String, Object> additionalProperties) {
        this.additionalProperties = additionalProperties;
    }

    @JsonProperty("status")
    public String getStatus() {
        return "failure";
    }

    @java.lang.Override
    public boolean equals(Object other) {
        if (this == other) return true;
        return other instanceof Failure;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @java.lang.Override
    public String toString() {
        return ObjectMappers.stringify(this);
    }
}
