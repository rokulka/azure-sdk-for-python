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

try:
    from .azure_time_series_data_py3 import AzureTimeSeriesData
    from .azure_metrics_base_data_py3 import AzureMetricsBaseData
    from .azure_metrics_data_py3 import AzureMetricsData
    from .azure_metrics_document_py3 import AzureMetricsDocument
    from .api_error_py3 import ApiError
    from .api_failure_response_py3 import ApiFailureResponse
    from .azure_metrics_result_py3 import AzureMetricsResult, AzureMetricsResultException
except (SyntaxError, ImportError):
    from .azure_time_series_data import AzureTimeSeriesData
    from .azure_metrics_base_data import AzureMetricsBaseData
    from .azure_metrics_data import AzureMetricsData
    from .azure_metrics_document import AzureMetricsDocument
    from .api_error import ApiError
    from .api_failure_response import ApiFailureResponse
    from .azure_metrics_result import AzureMetricsResult, AzureMetricsResultException

__all__ = [
    'AzureTimeSeriesData',
    'AzureMetricsBaseData',
    'AzureMetricsData',
    'AzureMetricsDocument',
    'ApiError',
    'ApiFailureResponse',
    'AzureMetricsResult', 'AzureMetricsResultException',
]