using System.Text.Json.Serialization;
using SeedTrace.V2;

namespace SeedTrace.V2;

public class Files
{
    [JsonPropertyName("files")]
    public List<List<FileInfoV2>> Files_ { get; init; }
}
