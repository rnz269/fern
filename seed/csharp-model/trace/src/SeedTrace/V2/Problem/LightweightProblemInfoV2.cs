using System.Text.Json.Serialization;
using SeedTrace;

namespace SeedTrace.V2;

public class LightweightProblemInfoV2
{
    [JsonPropertyName("problemId")]
    public string ProblemId { get; init; }

    [JsonPropertyName("problemName")]
    public string ProblemName { get; init; }

    [JsonPropertyName("problemVersion")]
    public int ProblemVersion { get; init; }

    [JsonPropertyName("variableTypes")]
    public List<HashSet<VariableType>> VariableTypes { get; init; }
}
