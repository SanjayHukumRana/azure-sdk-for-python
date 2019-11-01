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

from .azure_workload_restore_request_py3 import AzureWorkloadRestoreRequest


class AzureWorkloadSQLRestoreRequest(AzureWorkloadRestoreRequest):
    """AzureWorkload SQL -specific restore. Specifically for full/diff restore.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureWorkloadSQLPointInTimeRestoreRequest

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_type: Type of this recovery. Possible values include:
     'Invalid', 'OriginalLocation', 'AlternateLocation', 'RestoreDisks',
     'Offline'
    :type recovery_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RecoveryType
    :param source_resource_id: Fully qualified ARM ID of the VM on which
     workload that was running is being recovered.
    :type source_resource_id: str
    :param property_bag: Workload specific property bag.
    :type property_bag: dict[str, str]
    :param target_info: Details of target database
    :type target_info:
     ~azure.mgmt.recoveryservicesbackup.models.TargetRestoreInfo
    :param recovery_mode: Defines whether the current recovery mode is file
     restore or database restore. Possible values include: 'Invalid',
     'FileRecovery', 'WorkloadRecovery'
    :type recovery_mode: str or
     ~azure.mgmt.recoveryservicesbackup.models.RecoveryMode
    :param should_use_alternate_target_location: Default option set to true.
     If this is set to false, alternate data directory must be provided
    :type should_use_alternate_target_location: bool
    :param is_non_recoverable: SQL specific property where user can chose to
     set no-recovery when restore operation is tried
    :type is_non_recoverable: bool
    :param alternate_directory_paths: Data directory details
    :type alternate_directory_paths:
     list[~azure.mgmt.recoveryservicesbackup.models.SQLDataDirectoryMapping]
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_type': {'key': 'recoveryType', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'property_bag': {'key': 'propertyBag', 'type': '{str}'},
        'target_info': {'key': 'targetInfo', 'type': 'TargetRestoreInfo'},
        'recovery_mode': {'key': 'recoveryMode', 'type': 'str'},
        'should_use_alternate_target_location': {'key': 'shouldUseAlternateTargetLocation', 'type': 'bool'},
        'is_non_recoverable': {'key': 'isNonRecoverable', 'type': 'bool'},
        'alternate_directory_paths': {'key': 'alternateDirectoryPaths', 'type': '[SQLDataDirectoryMapping]'},
    }

    _subtype_map = {
        'object_type': {'AzureWorkloadSQLPointInTimeRestoreRequest': 'AzureWorkloadSQLPointInTimeRestoreRequest'}
    }

    def __init__(self, *, recovery_type=None, source_resource_id: str=None, property_bag=None, target_info=None, recovery_mode=None, should_use_alternate_target_location: bool=None, is_non_recoverable: bool=None, alternate_directory_paths=None, **kwargs) -> None:
        super(AzureWorkloadSQLRestoreRequest, self).__init__(recovery_type=recovery_type, source_resource_id=source_resource_id, property_bag=property_bag, target_info=target_info, recovery_mode=recovery_mode, **kwargs)
        self.should_use_alternate_target_location = should_use_alternate_target_location
        self.is_non_recoverable = is_non_recoverable
        self.alternate_directory_paths = alternate_directory_paths
        self.object_type = 'AzureWorkloadSQLRestoreRequest'
