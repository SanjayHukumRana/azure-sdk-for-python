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


class ScheduleProperties(Model):
    """Definition of schedule parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param start_time: Gets or sets the start time of the schedule.
    :type start_time: datetime
    :ivar start_time_offset_minutes: Gets the start time's offset in minutes.
    :vartype start_time_offset_minutes: float
    :param expiry_time: Gets or sets the end time of the schedule.
    :type expiry_time: datetime
    :param expiry_time_offset_minutes: Gets or sets the expiry time's offset
     in minutes.
    :type expiry_time_offset_minutes: float
    :param is_enabled: Gets or sets a value indicating whether this schedule
     is enabled. Default value: False .
    :type is_enabled: bool
    :param next_run: Gets or sets the next run time of the schedule.
    :type next_run: datetime
    :param next_run_offset_minutes: Gets or sets the next run time's offset in
     minutes.
    :type next_run_offset_minutes: float
    :param interval: Gets or sets the interval of the schedule.
    :type interval: int
    :param frequency: Gets or sets the frequency of the schedule. Possible
     values include: 'OneTime', 'Day', 'Hour', 'Week', 'Month'
    :type frequency: str or ~azure.mgmt.automation.models.ScheduleFrequency
    :param time_zone: Gets or sets the time zone of the schedule.
    :type time_zone: str
    :param advanced_schedule: Gets or sets the advanced schedule.
    :type advanced_schedule: ~azure.mgmt.automation.models.AdvancedSchedule
    :param creation_time: Gets or sets the creation time.
    :type creation_time: datetime
    :param last_modified_time: Gets or sets the last modified time.
    :type last_modified_time: datetime
    :param description: Gets or sets the description.
    :type description: str
    """

    _validation = {
        'start_time_offset_minutes': {'readonly': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'start_time_offset_minutes': {'key': 'startTimeOffsetMinutes', 'type': 'float'},
        'expiry_time': {'key': 'expiryTime', 'type': 'iso-8601'},
        'expiry_time_offset_minutes': {'key': 'expiryTimeOffsetMinutes', 'type': 'float'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'next_run': {'key': 'nextRun', 'type': 'iso-8601'},
        'next_run_offset_minutes': {'key': 'nextRunOffsetMinutes', 'type': 'float'},
        'interval': {'key': 'interval', 'type': 'int'},
        'frequency': {'key': 'frequency', 'type': 'str'},
        'time_zone': {'key': 'timeZone', 'type': 'str'},
        'advanced_schedule': {'key': 'advancedSchedule', 'type': 'AdvancedSchedule'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ScheduleProperties, self).__init__(**kwargs)
        self.start_time = kwargs.get('start_time', None)
        self.start_time_offset_minutes = None
        self.expiry_time = kwargs.get('expiry_time', None)
        self.expiry_time_offset_minutes = kwargs.get('expiry_time_offset_minutes', None)
        self.is_enabled = kwargs.get('is_enabled', False)
        self.next_run = kwargs.get('next_run', None)
        self.next_run_offset_minutes = kwargs.get('next_run_offset_minutes', None)
        self.interval = kwargs.get('interval', None)
        self.frequency = kwargs.get('frequency', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.advanced_schedule = kwargs.get('advanced_schedule', None)
        self.creation_time = kwargs.get('creation_time', None)
        self.last_modified_time = kwargs.get('last_modified_time', None)
        self.description = kwargs.get('description', None)
