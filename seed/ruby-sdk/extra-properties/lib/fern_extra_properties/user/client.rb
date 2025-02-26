# frozen_string_literal: true

require_relative "../../requests"
require_relative "types/user"
require "async"

module SeedExtraPropertiesClient
  class UserClient
    # @return [SeedExtraPropertiesClient::RequestClient]
    attr_reader :request_client

    # @param request_client [SeedExtraPropertiesClient::RequestClient]
    # @return [SeedExtraPropertiesClient::UserClient]
    def initialize(request_client:)
      @request_client = request_client
    end

    # @param type [String]
    # @param version [String]
    # @param name [String]
    # @param request_options [SeedExtraPropertiesClient::RequestOptions]
    # @return [SeedExtraPropertiesClient::User::User]
    def create_user(type:, version:, name:, request_options: nil)
      response = @request_client.conn.post do |req|
        req.options.timeout = request_options.timeout_in_seconds unless request_options&.timeout_in_seconds.nil?
        req.headers = { **req.headers, **(request_options&.additional_headers || {}) }.compact
        req.body = {
          **(request_options&.additional_body_parameters || {}),
          _type: type,
          _version: version,
          name: name
        }.compact
        req.url "#{@request_client.get_url(request_options: request_options)}/user"
      end
      SeedExtraPropertiesClient::User::User.from_json(json_object: response.body)
    end
  end

  class AsyncUserClient
    # @return [SeedExtraPropertiesClient::AsyncRequestClient]
    attr_reader :request_client

    # @param request_client [SeedExtraPropertiesClient::AsyncRequestClient]
    # @return [SeedExtraPropertiesClient::AsyncUserClient]
    def initialize(request_client:)
      @request_client = request_client
    end

    # @param type [String]
    # @param version [String]
    # @param name [String]
    # @param request_options [SeedExtraPropertiesClient::RequestOptions]
    # @return [SeedExtraPropertiesClient::User::User]
    def create_user(type:, version:, name:, request_options: nil)
      Async do
        response = @request_client.conn.post do |req|
          req.options.timeout = request_options.timeout_in_seconds unless request_options&.timeout_in_seconds.nil?
          req.headers = { **req.headers, **(request_options&.additional_headers || {}) }.compact
          req.body = {
            **(request_options&.additional_body_parameters || {}),
            _type: type,
            _version: version,
            name: name
          }.compact
          req.url "#{@request_client.get_url(request_options: request_options)}/user"
        end
        SeedExtraPropertiesClient::User::User.from_json(json_object: response.body)
      end
    end
  end
end
