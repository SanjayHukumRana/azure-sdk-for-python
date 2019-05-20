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


class SourceControlSyncJobCreateParameters(Model):
    """The parameters supplied to the create source control sync job operation.

    All required parameters must be populated in order to send to Azure.

    :param commit_id: Required. The commit id of the source control sync job.
     If not syncing to a commitId, enter an empty string.
    :type commit_id: str
    """

    _validation = {
        'commit_id': {'required': True, 'min_length': 0},
    }

    _attribute_map = {
        'commit_id': {'key': 'properties.commitId', 'type': 'str'},
    }

    def __init__(self, *, commit_id: str, **kwargs) -> None:
        super(SourceControlSyncJobCreateParameters, self).__init__(**kwargs)
        self.commit_id = commit_id