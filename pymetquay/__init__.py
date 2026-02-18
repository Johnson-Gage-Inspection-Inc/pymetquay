"""pymetquay - Convenience wrapper for the Metquay CRUD API."""

from openapi_client.api.authenticate_api import AuthenticateApi
from openapi_client.api.customerinstruments_api import CustomerinstrumentsApi
from openapi_client.api.customers_api import CustomersApi
from openapi_client.api.instrumentcategories_api import InstrumentcategoriesApi
from openapi_client.api.works_api import WorksApi
from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.configuration import Configuration
from openapi_client.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)
from openapi_client.models.authentication_request import AuthenticationRequest
from openapi_client.models.authentication_response import AuthenticationResponse
from openapi_client.models.created_response import CreatedResponse
from openapi_client.models.customer_instrument_request import CustomerInstrumentRequest
from openapi_client.models.customer_instrument_response import (
    CustomerInstrumentResponse,
)
from openapi_client.models.customer_request import CustomerRequest
from openapi_client.models.customer_response import CustomerResponse
from openapi_client.models.error_response import ErrorResponse
from openapi_client.models.instrument_category_request import InstrumentCategoryRequest
from openapi_client.models.work_request import WorkRequest
from openapi_client.models.work_response import WorkResponse
from pymetquay._version import __version__
from pymetquay.client import MetquayClient

__all__ = [
    "MetquayClient",
    "__version__",
    # API classes
    "ApiClient",
    "ApiResponse",
    "Configuration",
    "AuthenticateApi",
    "CustomersApi",
    "CustomerinstrumentsApi",
    "InstrumentcategoriesApi",
    "WorksApi",
    # Models
    "AuthenticationRequest",
    "AuthenticationResponse",
    "CreatedResponse",
    "CustomerInstrumentRequest",
    "CustomerInstrumentResponse",
    "CustomerRequest",
    "CustomerResponse",
    "ErrorResponse",
    "InstrumentCategoryRequest",
    "WorkRequest",
    "WorkResponse",
    # Exceptions
    "ApiException",
    "ApiAttributeError",
    "ApiKeyError",
    "ApiTypeError",
    "ApiValueError",
    "OpenApiException",
]
