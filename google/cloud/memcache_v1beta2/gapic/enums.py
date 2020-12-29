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

"""Wrappers for protocol buffer enum types."""

import enum


class MemcacheVersion(enum.IntEnum):
    """
    Memcached versions supported by our service.

    Attributes:
      MEMCACHE_VERSION_UNSPECIFIED (int)
      MEMCACHE_1_5 (int): Memcached 1.5 version.
    """

    MEMCACHE_VERSION_UNSPECIFIED = 0
    MEMCACHE_1_5 = 1


class Instance(object):
    class State(enum.IntEnum):
        """
        Different states of a Memcached instance.
        LINT.IfChange

        Attributes:
          STATE_UNSPECIFIED (int): State not set.
          CREATING (int): Memcached instance is being created.
          READY (int): Memcached instance has been created and ready to be used.
          DELETING (int): Memcached instance is being deleted.
          PERFORMING_MAINTENANCE (int): Memcached instance is going through maintenance, e.g. data plane rollout.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 4
        PERFORMING_MAINTENANCE = 5

    class Node(object):
        class State(enum.IntEnum):
            """
            Different states of a Memcached node.
            LINT.IfChange

            Attributes:
              STATE_UNSPECIFIED (int): Node state is not set.
              CREATING (int): Node is being created.
              READY (int): Node has been created and ready to be used.
              DELETING (int): Node is being deleted.
              UPDATING (int): Node is being updated.
            """

            STATE_UNSPECIFIED = 0
            CREATING = 1
            READY = 2
            DELETING = 3
            UPDATING = 4

    class InstanceMessage(object):
        class Code(enum.IntEnum):
            """
            Attributes:
              CODE_UNSPECIFIED (int): Message Code not set.
              ZONE_DISTRIBUTION_UNBALANCED (int): Memcached nodes are distributed unevenly.
            """

            CODE_UNSPECIFIED = 0
            ZONE_DISTRIBUTION_UNBALANCED = 1
