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
# Snippet for ApplySoftwareUpdate
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-memcache


# [START memcache_generated_memcache_v1beta2_CloudMemcache_ApplySoftwareUpdate_sync]
from google.cloud import memcache_v1beta2


def sample_apply_software_update():
    # Create a client
    client = memcache_v1beta2.CloudMemcacheClient()

    # Initialize request argument(s)
    request = memcache_v1beta2.ApplySoftwareUpdateRequest(
        instance="instance_value",
    )

    # Make the request
    operation = client.apply_software_update(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()
    print(response)

# [END memcache_generated_memcache_v1beta2_CloudMemcache_ApplySoftwareUpdate_sync]
