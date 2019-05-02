# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core import AsyncPipelineClient
from msrest import Serializer, Deserializer

from ._configuration_async import AzureConfigurationClientImpConfiguration
from .operations_async import AzureConfigurationClientImpOperationsMixin
from .. import models


class AzureConfigurationClientImp(AzureConfigurationClientImpOperationsMixin):
    """Represents an Azure App Configuration Client


    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None, config=None, **kwargs):

        if not base_url:
            base_url = 'http://localhost'
        self._config = config or AzureConfigurationClientImpConfiguration(credentials, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '0.1'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
