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


class MetricSettings(Model):
    """Part of MultiTenantDiagnosticSettings. Specifies the settings for a
    particular metric.

    All required parameters must be populated in order to send to Azure.

    :param time_grain: the timegrain of the metric in ISO8601 format.
    :type time_grain: timedelta
    :param category: Name of a Diagnostic Metric category for a resource type
     this setting is applied to. To obtain the list of Diagnostic metric
     categories for a resource, first perform a GET diagnostic settings
     operation.
    :type category: str
    :param enabled: Required. a value indicating whether this category is
     enabled.
    :type enabled: bool
    :param retention_policy: the retention policy for this category.
    :type retention_policy: ~azure.mgmt.monitor.models.RetentionPolicy
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'time_grain': {'key': 'timeGrain', 'type': 'duration'},
        'category': {'key': 'category', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(self, **kwargs):
        super(MetricSettings, self).__init__(**kwargs)
        self.time_grain = kwargs.get('time_grain', None)
        self.category = kwargs.get('category', None)
        self.enabled = kwargs.get('enabled', None)
        self.retention_policy = kwargs.get('retention_policy', None)
