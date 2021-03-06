# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JitNetworkAccessPolicy(Model):
    """JitNetworkAccessPolicy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param kind: Kind of the resource
    :type kind: str
    :ivar location: Location where the resource is stored
    :vartype location: str
    :param virtual_machines: Required. Configurations for
     Microsoft.Compute/virtualMachines resource type.
    :type virtual_machines:
     list[~azure.mgmt.security.models.JitNetworkAccessPolicyVirtualMachine]
    :param requests:
    :type requests: list[~azure.mgmt.security.models.JitNetworkAccessRequest]
    :ivar provisioning_state: Gets the provisioning state of the Just-in-Time
     policy.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'virtual_machines': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'virtual_machines': {'key': 'properties.virtualMachines', 'type': '[JitNetworkAccessPolicyVirtualMachine]'},
        'requests': {'key': 'properties.requests', 'type': '[JitNetworkAccessRequest]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, virtual_machines, kind: str=None, requests=None, **kwargs) -> None:
        super(JitNetworkAccessPolicy, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.kind = kind
        self.location = None
        self.virtual_machines = virtual_machines
        self.requests = requests
        self.provisioning_state = None
