# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateInstance
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-memcache


# [START memcache_v1beta2_generated_CloudMemcache_CreateInstance_sync]
from google.cloud import memcache_v1beta2


def sample_create_instance():
    # Create a client
    client = memcache_v1beta2.CloudMemcacheClient()

    # Initialize request argument(s)
    resource = memcache_v1beta2.Instance()
    resource.name = "name_value"
    resource.node_count = 1070
    resource.node_config.cpu_count = 976
    resource.node_config.memory_size_mb = 1505

    request = memcache_v1beta2.CreateInstanceRequest(
        parent="parent_value",
        instance_id="instance_id_value",
        resource=resource,
    )

    # Make the request
    operation = client.create_instance(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END memcache_v1beta2_generated_CloudMemcache_CreateInstance_sync]
