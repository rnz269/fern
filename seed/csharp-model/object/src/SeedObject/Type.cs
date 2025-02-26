using System.Text.Json.Serialization;
using SeedObject;

namespace SeedObject;

public class Type
{
    [JsonPropertyName("one")]
    public int One { get; init; }

    [JsonPropertyName("two")]
    public double Two { get; init; }

    [JsonPropertyName("three")]
    public string Three { get; init; }

    [JsonPropertyName("four")]
    public bool Four { get; init; }

    [JsonPropertyName("five")]
    public long Five { get; init; }

    [JsonPropertyName("six")]
    public DateTime Six { get; init; }

    [JsonPropertyName("seven")]
    public DateOnly Seven { get; init; }

    [JsonPropertyName("eight")]
    public Guid Eight { get; init; }

    [JsonPropertyName("nine")]
    public string Nine { get; init; }

    [JsonPropertyName("ten")]
    public List<List<int>> Ten { get; init; }

    [JsonPropertyName("eleven")]
    public List<HashSet<double>> Eleven { get; init; }

    [JsonPropertyName("twelve")]
    public List<Dictionary<string, bool>> Twelve { get; init; }

    [JsonPropertyName("thirteen")]
    public List<long?> Thirteen { get; init; }

    [JsonPropertyName("fourteen")]
    public object Fourteen { get; init; }

    [JsonPropertyName("fifteen")]
    public List<List<List<List<int>>>> Fifteen { get; init; }

    [JsonPropertyName("sixteen")]
    public List<List<List<Dictionary<string, int>>>> Sixteen { get; init; }

    [JsonPropertyName("seventeen")]
    public List<List<List<Guid?>>> Seventeen { get; init; }

    [JsonPropertyName("eighteen")]
    public List<string> Eighteen { get; init; }

    [JsonPropertyName("nineteen")]
    public Name Nineteen { get; init; }
}
