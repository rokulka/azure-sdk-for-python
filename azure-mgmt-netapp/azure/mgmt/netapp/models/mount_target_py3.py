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


class MountTarget(Model):
    """Mount Target.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :param tags: Resource tags
    :type tags: object
    :ivar mount_target_id: mountTargetId. UUID v4 used to identify the
     MountTarget
    :vartype mount_target_id: str
    :param file_system_id: Required. fileSystemId. UUID v4 used to identify
     the MountTarget
    :type file_system_id: str
    :ivar ip_address: ipAddress. The mount target's IPv4 address
    :vartype ip_address: str
    :param vlan_id: vlanid. Vlan Id
    :type vlan_id: int
    :param start_ip: startIp. The start of IPv4 address range to use when
     creating a new mount target
    :type start_ip: str
    :param end_ip: startIp. The end of IPv4 address range to use when creating
     a new mount target
    :type end_ip: str
    :param gateway: gateway. The gateway of the IPv4 address range to use when
     creating a new mount target
    :type gateway: str
    :param netmask: netmask. The netmask of the IPv4 address range to use when
     creating a new mount target
    :type netmask: str
    :ivar provisioning_state: Azure lifecycle management
    :vartype provisioning_state: str
    """

    _validation = {
        'location': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'mount_target_id': {'readonly': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'file_system_id': {'required': True, 'max_length': 36, 'min_length': 36, 'pattern': r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'},
        'ip_address': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
        'mount_target_id': {'key': 'properties.mountTargetId', 'type': 'str'},
        'file_system_id': {'key': 'properties.fileSystemId', 'type': 'str'},
        'ip_address': {'key': 'properties.ipAddress', 'type': 'str'},
        'vlan_id': {'key': 'properties.vlanId', 'type': 'int'},
        'start_ip': {'key': 'properties.startIp', 'type': 'str'},
        'end_ip': {'key': 'properties.endIp', 'type': 'str'},
        'gateway': {'key': 'properties.gateway', 'type': 'str'},
        'netmask': {'key': 'properties.netmask', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, file_system_id: str, tags=None, vlan_id: int=None, start_ip: str=None, end_ip: str=None, gateway: str=None, netmask: str=None, **kwargs) -> None:
        super(MountTarget, self).__init__(**kwargs)
        self.location = location
        self.id = None
        self.name = None
        self.tags = tags
        self.mount_target_id = None
        self.file_system_id = file_system_id
        self.ip_address = None
        self.vlan_id = vlan_id
        self.start_ip = start_ip
        self.end_ip = end_ip
        self.gateway = gateway
        self.netmask = netmask
        self.provisioning_state = None
