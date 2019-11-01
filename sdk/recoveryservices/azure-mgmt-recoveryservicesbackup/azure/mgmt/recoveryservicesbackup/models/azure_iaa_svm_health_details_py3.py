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


class AzureIaaSVMHealthDetails(Model):
    """Azure IaaS VM workload-specific Health Details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Health Code
    :vartype code: int
    :ivar title: Health Title
    :vartype title: str
    :ivar message: Health Message
    :vartype message: str
    :ivar recommendations: Health Recommended Actions
    :vartype recommendations: list[str]
    """

    _validation = {
        'code': {'readonly': True},
        'title': {'readonly': True},
        'message': {'readonly': True},
        'recommendations': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'title': {'key': 'title', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'recommendations': {'key': 'recommendations', 'type': '[str]'},
    }

    def __init__(self, **kwargs) -> None:
        super(AzureIaaSVMHealthDetails, self).__init__(**kwargs)
        self.code = None
        self.title = None
        self.message = None
        self.recommendations = None
