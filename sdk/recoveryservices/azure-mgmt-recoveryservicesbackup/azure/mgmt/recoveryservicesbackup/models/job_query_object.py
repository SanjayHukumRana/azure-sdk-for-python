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


class JobQueryObject(Model):
    """Filters to list the jobs.

    :param status: Status of the job. Possible values include: 'Invalid',
     'InProgress', 'Completed', 'Failed', 'CompletedWithWarnings', 'Cancelled',
     'Cancelling'
    :type status: str or ~azure.mgmt.recoveryservicesbackup.models.JobStatus
    :param backup_management_type: Type of backup management for the job.
     Possible values include: 'Invalid', 'AzureIaasVM', 'MAB', 'DPM',
     'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param operation: Type of operation. Possible values include: 'Invalid',
     'Register', 'UnRegister', 'ConfigureBackup', 'Backup', 'Restore',
     'DisableBackup', 'DeleteBackupData', 'CrossRegionRestore', 'Undelete'
    :type operation: str or
     ~azure.mgmt.recoveryservicesbackup.models.JobOperationType
    :param job_id: JobID represents the job uniquely.
    :type job_id: str
    :param start_time: Job has started at this time. Value is in UTC.
    :type start_time: datetime
    :param end_time: Job has ended at this time. Value is in UTC.
    :type end_time: datetime
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(JobQueryObject, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.backup_management_type = kwargs.get('backup_management_type', None)
        self.operation = kwargs.get('operation', None)
        self.job_id = kwargs.get('job_id', None)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
