# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 0.14.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class SubProduct(SubResource):

    _required = []

    _attribute_map = {
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'provisioning_state_values': {'key': 'properties.provisioningStateValues', 'type': 'str'},
    }

    def __init__(self, *args, **kwargs):
        """SubProduct

        :param str provisioning_state
        :param str provisioning_state_values: Possible values for this
        property include: 'Succeeded', 'Failed', 'canceled', 'Accepted',
        'Creating', 'Created', 'Updating', 'Updated', 'Deleting', 'Deleted',
        'OK'.
        """
        self.provisioning_state = None
        self.provisioning_state_values = None

        super(SubProduct, self).__init__(*args, **kwargs)