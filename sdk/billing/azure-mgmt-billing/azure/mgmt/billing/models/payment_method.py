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

from .resource import Resource


class PaymentMethod(Resource):
    """A payment method resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param payment_method_type: Payment method type. Possible values include:
     'Credits', 'ChequeWire'
    :type payment_method_type: str or
     ~azure.mgmt.billing.models.PaymentMethodType
    :ivar details: Details about the payment method.
    :vartype details: str
    :ivar expiration: Expiration month and year.
    :vartype expiration: str
    :ivar currency: The currency associated with the payment method.
    :vartype currency: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'details': {'readonly': True},
        'expiration': {'readonly': True},
        'currency': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'payment_method_type': {'key': 'properties.paymentMethodType', 'type': 'str'},
        'details': {'key': 'properties.details', 'type': 'str'},
        'expiration': {'key': 'properties.expiration', 'type': 'str'},
        'currency': {'key': 'properties.currency', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PaymentMethod, self).__init__(**kwargs)
        self.payment_method_type = kwargs.get('payment_method_type', None)
        self.details = None
        self.expiration = None
        self.currency = None
