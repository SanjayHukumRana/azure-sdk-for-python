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


class ProtectionPolicy(Model):
    """Base class for backup policy. Workload-specific backup policies are derived
    from this class.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureVmWorkloadProtectionPolicy,
    AzureFileShareProtectionPolicy, AzureIaaSVMProtectionPolicy,
    AzureSqlProtectionPolicy, GenericProtectionPolicy, MabProtectionPolicy

    All required parameters must be populated in order to send to Azure.

    :param protected_items_count: Number of items associated with this policy.
    :type protected_items_count: int
    :param backup_management_type: Required. Constant filled by server.
    :type backup_management_type: str
    """

    _validation = {
        'backup_management_type': {'required': True},
    }

    _attribute_map = {
        'protected_items_count': {'key': 'protectedItemsCount', 'type': 'int'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
    }

    _subtype_map = {
        'backup_management_type': {'AzureWorkload': 'AzureVmWorkloadProtectionPolicy', 'AzureStorage': 'AzureFileShareProtectionPolicy', 'AzureIaasVM': 'AzureIaaSVMProtectionPolicy', 'AzureSql': 'AzureSqlProtectionPolicy', 'GenericProtectionPolicy': 'GenericProtectionPolicy', 'MAB': 'MabProtectionPolicy'}
    }

    def __init__(self, *, protected_items_count: int=None, **kwargs) -> None:
        super(ProtectionPolicy, self).__init__(**kwargs)
        self.protected_items_count = protected_items_count
        self.backup_management_type = None
