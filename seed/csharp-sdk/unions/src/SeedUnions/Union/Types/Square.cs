using System.Text.Json.Serialization;

namespace SeedUnions;

public class Square
{
    [JsonPropertyName("length")]
    public double Length { get; init; }
}
