using System.Text.Json.Serialization;

namespace SeedExamples;

public class Moment
{
    [JsonPropertyName("id")]
    public Guid Id { get; init; }

    [JsonPropertyName("date")]
    public DateOnly Date { get; init; }

    [JsonPropertyName("datetime")]
    public DateTime Datetime { get; init; }
}
