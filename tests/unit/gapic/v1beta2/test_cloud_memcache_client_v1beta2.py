# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pytest

from google.rpc import status_pb2

from google.cloud import memcache_v1beta2
from google.cloud.memcache_v1beta2.proto import cloud_memcache_pb2
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.requests = []

    def unary_unary(self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestCloudMemcacheClient(object):
    def test_list_instances(self):
        # Setup Expected Response
        next_page_token = ""
        resources_element = {}
        resources_2 = [resources_element]
        expected_response = {
            "next_page_token": next_page_token,
            "resources": resources_2,
        }
        expected_response = cloud_memcache_pb2.ListInstancesResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup Request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        paged_list_response = client.list_instances(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.resources[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = cloud_memcache_pb2.ListInstancesRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_instances_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup request
        parent = client.location_path("[PROJECT]", "[LOCATION]")

        paged_list_response = client.list_instances(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_instance(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        authorized_network = "authorizedNetwork-1733809270"
        node_count = 1539922066
        memcache_full_version = "memcacheFullVersion-1666834598"
        discovery_endpoint = "discoveryEndpoint224997188"
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "authorized_network": authorized_network,
            "node_count": node_count,
            "memcache_full_version": memcache_full_version,
            "discovery_endpoint": discovery_endpoint,
        }
        expected_response = cloud_memcache_pb2.Instance(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup Request
        name = client.instance_path("[PROJECT]", "[LOCATION]", "[INSTANCE]")

        response = client.get_instance(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = cloud_memcache_pb2.GetInstanceRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_instance_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup request
        name = client.instance_path("[PROJECT]", "[LOCATION]", "[INSTANCE]")

        with pytest.raises(CustomException):
            client.get_instance(name)

    def test_create_instance(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        authorized_network = "authorizedNetwork-1733809270"
        node_count = 1539922066
        memcache_full_version = "memcacheFullVersion-1666834598"
        discovery_endpoint = "discoveryEndpoint224997188"
        expected_response = {
            "name": name,
            "display_name": display_name,
            "authorized_network": authorized_network,
            "node_count": node_count,
            "memcache_full_version": memcache_full_version,
            "discovery_endpoint": discovery_endpoint,
        }
        expected_response = cloud_memcache_pb2.Instance(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_create_instance", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup Request
        parent = client.location_path("[PROJECT]", "[LOCATION]")
        instance_id = "instanceId-2101995259"
        resource = {}

        response = client.create_instance(parent, instance_id, resource)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = cloud_memcache_pb2.CreateInstanceRequest(
            parent=parent, instance_id=instance_id, resource=resource
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_instance_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_create_instance_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup Request
        parent = client.location_path("[PROJECT]", "[LOCATION]")
        instance_id = "instanceId-2101995259"
        resource = {}

        response = client.create_instance(parent, instance_id, resource)
        exception = response.exception()
        assert exception.errors[0] == error

    def test_update_instance(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        authorized_network = "authorizedNetwork-1733809270"
        node_count = 1539922066
        memcache_full_version = "memcacheFullVersion-1666834598"
        discovery_endpoint = "discoveryEndpoint224997188"
        expected_response = {
            "name": name,
            "display_name": display_name,
            "authorized_network": authorized_network,
            "node_count": node_count,
            "memcache_full_version": memcache_full_version,
            "discovery_endpoint": discovery_endpoint,
        }
        expected_response = cloud_memcache_pb2.Instance(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_update_instance", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup Request
        update_mask = {}
        resource = {}

        response = client.update_instance(update_mask, resource)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = cloud_memcache_pb2.UpdateInstanceRequest(
            update_mask=update_mask, resource=resource
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_instance_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_update_instance_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup Request
        update_mask = {}
        resource = {}

        response = client.update_instance(update_mask, resource)
        exception = response.exception()
        assert exception.errors[0] == error

    def test_update_parameters(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        authorized_network = "authorizedNetwork-1733809270"
        node_count = 1539922066
        memcache_full_version = "memcacheFullVersion-1666834598"
        discovery_endpoint = "discoveryEndpoint224997188"
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "authorized_network": authorized_network,
            "node_count": node_count,
            "memcache_full_version": memcache_full_version,
            "discovery_endpoint": discovery_endpoint,
        }
        expected_response = cloud_memcache_pb2.Instance(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_update_parameters", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup Request
        name = client.instance_path("[PROJECT]", "[LOCATION]", "[INSTANCE]")
        update_mask = {}

        response = client.update_parameters(name, update_mask)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = cloud_memcache_pb2.UpdateParametersRequest(
            name=name, update_mask=update_mask
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_parameters_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_update_parameters_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup Request
        name = client.instance_path("[PROJECT]", "[LOCATION]", "[INSTANCE]")
        update_mask = {}

        response = client.update_parameters(name, update_mask)
        exception = response.exception()
        assert exception.errors[0] == error

    def test_delete_instance(self):
        # Setup Expected Response
        expected_response = {}
        expected_response = empty_pb2.Empty(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_delete_instance", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        response = client.delete_instance()
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = cloud_memcache_pb2.DeleteInstanceRequest()
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_instance_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_delete_instance_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        response = client.delete_instance()
        exception = response.exception()
        assert exception.errors[0] == error

    def test_apply_parameters(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        authorized_network = "authorizedNetwork-1733809270"
        node_count = 1539922066
        memcache_full_version = "memcacheFullVersion-1666834598"
        discovery_endpoint = "discoveryEndpoint224997188"
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "authorized_network": authorized_network,
            "node_count": node_count,
            "memcache_full_version": memcache_full_version,
            "discovery_endpoint": discovery_endpoint,
        }
        expected_response = cloud_memcache_pb2.Instance(**expected_response)
        operation = operations_pb2.Operation(
            name="operations/test_apply_parameters", done=True
        )
        operation.response.Pack(expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup Request
        name = client.instance_path("[PROJECT]", "[LOCATION]", "[INSTANCE]")

        response = client.apply_parameters(name)
        result = response.result()
        assert expected_response == result

        assert len(channel.requests) == 1
        expected_request = cloud_memcache_pb2.ApplyParametersRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_apply_parameters_exception(self):
        # Setup Response
        error = status_pb2.Status()
        operation = operations_pb2.Operation(
            name="operations/test_apply_parameters_exception", done=True
        )
        operation.error.CopyFrom(error)

        # Mock the API response
        channel = ChannelStub(responses=[operation])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = memcache_v1beta2.CloudMemcacheClient()

        # Setup Request
        name = client.instance_path("[PROJECT]", "[LOCATION]", "[INSTANCE]")

        response = client.apply_parameters(name)
        exception = response.exception()
        assert exception.errors[0] == error
