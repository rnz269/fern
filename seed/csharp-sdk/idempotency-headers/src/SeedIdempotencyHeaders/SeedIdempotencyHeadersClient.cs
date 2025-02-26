using SeedIdempotencyHeaders;

namespace SeedIdempotencyHeaders;

public partial class SeedIdempotencyHeadersClient
{
    private RawClient _client;

    public SeedIdempotencyHeadersClient(string token, ClientOptions clientOptions)
    {
        _client = new RawClient(
            new Dictionary<string, string>
            {
                { "Authorization", $"Bearer {token}" },
                { "X-Fern-Language", "C#" },
            },
            clientOptions ?? new ClientOptions()
        );
        Payment = new PaymentClient(_client);
    }

    public PaymentClient Payment { get; }

    private string GetFromEnvironmentOrThrow(string env, string message)
    {
        var value = Environment.GetEnvironmentVariable(env);
        if (value == null)
        {
            throw new Exception(message);
        }
        return value;
    }
}
