# frozen_string_literal: true

require_relative "../../requests"
require "json"
require "async"

module SeedSingleUrlEnvironmentNoDefaultClient
  class DummyClient
    # @return [SeedSingleUrlEnvironmentNoDefaultClient::RequestClient]
    attr_reader :request_client

    # @param request_client [SeedSingleUrlEnvironmentNoDefaultClient::RequestClient]
    # @return [SeedSingleUrlEnvironmentNoDefaultClient::DummyClient]
    def initialize(request_client:)
      @request_client = request_client
    end

    # @param request_options [SeedSingleUrlEnvironmentNoDefaultClient::RequestOptions]
    # @return [String]
    def get_dummy(request_options: nil)
      response = @request_client.conn.get do |req|
        req.options.timeout = request_options.timeout_in_seconds unless request_options&.timeout_in_seconds.nil?
        req.headers["Authorization"] = request_options.token unless request_options&.token.nil?
        req.headers = { **req.headers, **(request_options&.additional_headers || {}) }.compact
        req.url "#{@request_client.get_url(request_options: request_options)}/dummy"
      end
      JSON.parse(response.body)
    end
  end

  class AsyncDummyClient
    # @return [SeedSingleUrlEnvironmentNoDefaultClient::AsyncRequestClient]
    attr_reader :request_client

    # @param request_client [SeedSingleUrlEnvironmentNoDefaultClient::AsyncRequestClient]
    # @return [SeedSingleUrlEnvironmentNoDefaultClient::AsyncDummyClient]
    def initialize(request_client:)
      @request_client = request_client
    end

    # @param request_options [SeedSingleUrlEnvironmentNoDefaultClient::RequestOptions]
    # @return [String]
    def get_dummy(request_options: nil)
      Async do
        response = @request_client.conn.get do |req|
          req.options.timeout = request_options.timeout_in_seconds unless request_options&.timeout_in_seconds.nil?
          req.headers["Authorization"] = request_options.token unless request_options&.token.nil?
          req.headers = { **req.headers, **(request_options&.additional_headers || {}) }.compact
          req.url "#{@request_client.get_url(request_options: request_options)}/dummy"
        end
        parsed_json = JSON.parse(response.body)
        parsed_json
      end
    end
  end
end
