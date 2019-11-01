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

from .restore_request_py3 import RestoreRequest


class AzureFileShareRestoreRequest(RestoreRequest):
    """AzureFileShare Restore Request.

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    :param recovery_type: Type of this recovery. Possible values include:
     'Invalid', 'OriginalLocation', 'AlternateLocation', 'RestoreDisks',
     'Offline'
    :type recovery_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RecoveryType
    :param source_resource_id: Source storage account ARM Id
    :type source_resource_id: str
    :param copy_options: Options to resolve copy conflicts. Possible values
     include: 'Invalid', 'CreateCopy', 'Skip', 'Overwrite', 'FailOnConflict'
    :type copy_options: str or
     ~azure.mgmt.recoveryservicesbackup.models.CopyOptions
    :param restore_request_type: Restore Type (FullShareRestore or
     ItemLevelRestore). Possible values include: 'Invalid', 'FullShareRestore',
     'ItemLevelRestore'
    :type restore_request_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.RestoreRequestType
    :param restore_file_specs: List of Source Files/Folders(which need to
     recover) and TargetFolderPath details
    :type restore_file_specs:
     list[~azure.mgmt.recoveryservicesbackup.models.RestoreFileSpecs]
    :param target_details: Target File Share Details
    :type target_details:
     ~azure.mgmt.recoveryservicesbackup.models.TargetAFSRestoreInfo
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'recovery_type': {'key': 'recoveryType', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'copy_options': {'key': 'copyOptions', 'type': 'str'},
        'restore_request_type': {'key': 'restoreRequestType', 'type': 'str'},
        'restore_file_specs': {'key': 'restoreFileSpecs', 'type': '[RestoreFileSpecs]'},
        'target_details': {'key': 'targetDetails', 'type': 'TargetAFSRestoreInfo'},
    }

    def __init__(self, *, recovery_type=None, source_resource_id: str=None, copy_options=None, restore_request_type=None, restore_file_specs=None, target_details=None, **kwargs) -> None:
        super(AzureFileShareRestoreRequest, self).__init__(**kwargs)
        self.recovery_type = recovery_type
        self.source_resource_id = source_resource_id
        self.copy_options = copy_options
        self.restore_request_type = restore_request_type
        self.restore_file_specs = restore_file_specs
        self.target_details = target_details
        self.object_type = 'AzureFileShareRestoreRequest'
