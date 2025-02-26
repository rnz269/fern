// This file was auto-generated by Fern from our API Definition.

package plant

import (
	context "context"
	core "github.com/fern-api/fern-go/internal/testdata/sdk/multi-environments/fixtures/core"
	option "github.com/fern-api/fern-go/internal/testdata/sdk/multi-environments/fixtures/option"
	http "net/http"
)

type Client struct {
	baseURL string
	caller  *core.Caller
	header  http.Header
}

func NewClient(opts ...option.RequestOption) *Client {
	options := core.NewRequestOptions(opts...)
	return &Client{
		baseURL: options.BaseURL,
		caller: core.NewCaller(
			&core.CallerParams{
				Client:      options.HTTPClient,
				MaxAttempts: options.MaxAttempts,
			},
		),
		header: options.ToHeader(),
	}
}

func (c *Client) GetPlant(
	ctx context.Context,
	opts ...option.RequestOption,
) (string, error) {
	options := core.NewRequestOptions(opts...)

	baseURL := "https://plants.yoursite.com"
	if c.baseURL != "" {
		baseURL = c.baseURL
	}
	if options.BaseURL != "" {
		baseURL = options.BaseURL
	}
	endpointURL := baseURL + "/plants"

	headers := core.MergeHeaders(c.header.Clone(), options.ToHeader())

	var response string
	if err := c.caller.Call(
		ctx,
		&core.CallParams{
			URL:         endpointURL,
			Method:      http.MethodGet,
			MaxAttempts: options.MaxAttempts,
			Headers:     headers,
			Client:      options.HTTPClient,
			Response:    &response,
		},
	); err != nil {
		return "", err
	}
	return response, nil
}
