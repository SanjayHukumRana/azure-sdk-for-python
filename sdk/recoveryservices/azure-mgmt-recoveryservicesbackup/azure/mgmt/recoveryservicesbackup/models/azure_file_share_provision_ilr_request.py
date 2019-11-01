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

from .ilr_request import ILRRequest


class AzureFileShareProvisionILRRequest(ILRRequest):
    """Update snapshot Uri with the correct friendly Name of the source Azure file
    share.

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_point_id: Recovery point ID.
    :type recovery_point_id: str
    :param source_resource_id: Source Storage account ARM Id
    :type source_resource_id: str
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_point_id': {'key': 'recoveryPointId', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureFileShareProvisionILRRequest, self).__init__(**kwargs)
        self.recovery_point_id = kwargs.get('recovery_point_id', None)
        self.source_resource_id = kwargs.get('source_resource_id', None)
        self.object_type = 'AzureFileShareProvisionILRRequest'
