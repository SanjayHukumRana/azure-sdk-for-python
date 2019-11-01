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


class RecoveryPointDiskConfiguration(Model):
    """Disk configuration.

    :param number_of_disks_included_in_backup: Number of disks included in
     backup
    :type number_of_disks_included_in_backup: int
    :param number_of_disks_attached_to_vm: Number of disks attached to the VM
    :type number_of_disks_attached_to_vm: int
    :param included_disk_list: Information of disks included in backup
    :type included_disk_list:
     list[~azure.mgmt.recoveryservicesbackup.models.DiskInformation]
    :param excluded_disk_list: Information of disks excluded from backup
    :type excluded_disk_list:
     list[~azure.mgmt.recoveryservicesbackup.models.DiskInformation]
    """

    _attribute_map = {
        'number_of_disks_included_in_backup': {'key': 'numberOfDisksIncludedInBackup', 'type': 'int'},
        'number_of_disks_attached_to_vm': {'key': 'numberOfDisksAttachedToVm', 'type': 'int'},
        'included_disk_list': {'key': 'includedDiskList', 'type': '[DiskInformation]'},
        'excluded_disk_list': {'key': 'excludedDiskList', 'type': '[DiskInformation]'},
    }

    def __init__(self, *, number_of_disks_included_in_backup: int=None, number_of_disks_attached_to_vm: int=None, included_disk_list=None, excluded_disk_list=None, **kwargs) -> None:
        super(RecoveryPointDiskConfiguration, self).__init__(**kwargs)
        self.number_of_disks_included_in_backup = number_of_disks_included_in_backup
        self.number_of_disks_attached_to_vm = number_of_disks_attached_to_vm
        self.included_disk_list = included_disk_list
        self.excluded_disk_list = excluded_disk_list
