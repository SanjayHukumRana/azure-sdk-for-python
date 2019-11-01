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

from .azure_workload_recovery_point import AzureWorkloadRecoveryPoint


class AzureWorkloadSAPHanaRecoveryPoint(AzureWorkloadRecoveryPoint):
    """SAPHana specific recoverypoint, specifically encapsulates full/diff
    recoverypoints.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :ivar recovery_point_time_in_utc: UTC time at which recovery point was
     created
    :vartype recovery_point_time_in_utc: datetime
    :ivar type: Type of restore point. Possible values include: 'Invalid',
     'Full', 'Log', 'Differential'
    :vartype type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RestorePointType
    """

    _validation = {
        'object_type': {'required': True},
        'recovery_point_time_in_utc': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_point_time_in_utc': {'key': 'recoveryPointTimeInUTC', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureWorkloadSAPHanaRecoveryPoint, self).__init__(**kwargs)
        self.object_type = 'AzureWorkloadSAPHanaRecoveryPoint'
