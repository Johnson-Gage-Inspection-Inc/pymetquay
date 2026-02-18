"""Convenience wrapper around the generated Metquay OpenAPI client."""

from __future__ import annotations

import logging
import os
import time
from typing import Callable, List, Optional, TypeVar

from dotenv import load_dotenv

from openapi_client import ApiClient, Configuration
from openapi_client.api.authenticate_api import AuthenticateApi
from openapi_client.api.customerinstruments_api import CustomerinstrumentsApi
from openapi_client.api.customers_api import CustomersApi
from openapi_client.api.instrumentcategories_api import InstrumentcategoriesApi
from openapi_client.api.works_api import WorksApi
from openapi_client.models.authentication_request import AuthenticationRequest
from openapi_client.models.authentication_response import AuthenticationResponse
from openapi_client.models.created_response import CreatedResponse
from openapi_client.models.customer_instrument_request import CustomerInstrumentRequest
from openapi_client.models.customer_instrument_response import (
    CustomerInstrumentResponse,
)
from openapi_client.models.customer_request import CustomerRequest
from openapi_client.models.customer_response import CustomerResponse
from openapi_client.models.instrument_category_request import InstrumentCategoryRequest
from openapi_client.models.work_request import WorkRequest
from openapi_client.models.work_response import WorkResponse

logger = logging.getLogger(__name__)

T = TypeVar("T")

_TOKEN_REFRESH_MARGIN_SECONDS = 120
_DEFAULT_TOKEN_TTL = 900
_DEFAULT_PAGE_LIMIT = 50


class MetquayClient:
    """High-level client for the Metquay CRUD API.

    Wraps the generated ``openapi_client`` with automatic token management,
    pagination helpers, and ``.env``-based configuration.

    Usage::

        from pymetquay import MetquayClient

        with MetquayClient() as client:
            customers = client.list_customers(limit=10)
    """

    def __init__(
        self,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        host: Optional[str] = None,
        *,
        dotenv_path: Optional[str] = None,
    ) -> None:
        load_dotenv(dotenv_path=dotenv_path)

        self._access_key = (
            access_key
            or os.environ.get("METQUAY_ACCESS_KEY")
            or os.environ.get("ACCESS_KEY", "")
        )
        self._secret_key = (
            secret_key
            or os.environ.get("METQUAY_SECRET_KEY")
            or os.environ.get("SECRET_KEY", "")
        )
        metquay_host = (
            host
            or os.environ.get("METQUAY_HOST")
            or os.environ.get("HOST", "johnsongage.metquay.co")
        )

        if not self._access_key or not self._secret_key:
            raise ValueError(
                "Metquay credentials required. Provide access_key/secret_key "
                "arguments or set METQUAY_ACCESS_KEY/METQUAY_SECRET_KEY (or "
                "ACCESS_KEY/SECRET_KEY) environment variables (or in a .env file)."
            )

        self._configuration = Configuration(host=f"https://{metquay_host}/api/v1")
        self._api_client = ApiClient(self._configuration)

        self._auth_api = AuthenticateApi(self._api_client)
        self._customers_api = CustomersApi(self._api_client)
        self._instruments_api = CustomerinstrumentsApi(self._api_client)
        self._categories_api = InstrumentcategoriesApi(self._api_client)
        self._works_api = WorksApi(self._api_client)

        self._token: Optional[str] = None
        self._token_acquired_at: float = 0.0
        self._token_ttl: int = _DEFAULT_TOKEN_TTL

    # -- Context manager ---------------------------------------------------

    def __enter__(self) -> MetquayClient:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

    # -- Authentication ----------------------------------------------------

    def _is_token_valid(self) -> bool:
        if self._token is None:
            return False
        elapsed = time.monotonic() - self._token_acquired_at
        remaining = self._token_ttl - elapsed
        return remaining > _TOKEN_REFRESH_MARGIN_SECONDS

    def _ensure_authenticated(self) -> None:
        if self._is_token_valid():
            return
        self.authenticate()

    def authenticate(self) -> AuthenticationResponse:
        """Authenticate and obtain a new bearer token."""
        if self._access_key is None:
            raise ValueError("Access key is required for authentication")
        if self._secret_key is None:
            raise ValueError("Secret key is required for authentication")
        request = AuthenticationRequest(
            accessKey=self._access_key,
            secretKey=self._secret_key,
        )
        response: AuthenticationResponse = self._auth_api.get_access_token(request)

        self._token = response.access_token
        self._token_acquired_at = time.monotonic()
        self._token_ttl = response.expires_in or _DEFAULT_TOKEN_TTL
        self._configuration.access_token = self._token

        logger.info(
            "Authenticated successfully (token expires in %d seconds)",
            self._token_ttl,
        )
        return response

    # -- Generic pagination helper -----------------------------------------

    def _paginate_all(
        self,
        list_fn: Callable[..., List[T]],
        *,
        page_size: int = _DEFAULT_PAGE_LIMIT,
        **kwargs,
    ) -> List[T]:
        """Fetch all pages from a paginated list endpoint."""
        all_records = []
        offset = 0
        while True:
            self._ensure_authenticated()
            page = list_fn(first=offset, limit=page_size, **kwargs)
            all_records.extend(page)
            if len(page) < page_size:
                break
            offset += len(page)
        return all_records

    # -- Customers ---------------------------------------------------------

    def list_customers(
        self,
        *,
        first: Optional[int] = None,
        limit: Optional[int] = None,
        workspace_code: Optional[str] = None,
        paginate_all: bool = False,
    ) -> List[CustomerResponse]:
        """List customers, optionally auto-paginating all results."""
        if paginate_all:
            return self._paginate_all(
                self._customers_api.get_customers,
                workspace_code=workspace_code,
            )
        self._ensure_authenticated()
        return self._customers_api.get_customers(
            workspace_code=workspace_code,
            first=first,
            limit=limit,
        )

    def create_customer(self, request: CustomerRequest) -> CreatedResponse:
        """Create a new customer."""
        self._ensure_authenticated()
        return self._customers_api.create_customer(request)

    def update_customer(self, metquay_id: int, request: CustomerRequest) -> None:
        """Update a customer by Metquay ID (full replacement)."""
        self._ensure_authenticated()
        self._customers_api.update_customer(metquay_id, request)

    def delete_customer(self, metquay_id: int) -> None:
        """Delete a customer by Metquay ID."""
        self._ensure_authenticated()
        self._customers_api.delete_customer(metquay_id)

    # -- Customer instruments ----------------------------------------------

    def list_instruments(
        self,
        *,
        first: Optional[int] = None,
        limit: Optional[int] = None,
        workspace_code: Optional[str] = None,
        paginate_all: bool = False,
    ) -> List[CustomerInstrumentResponse]:
        """List customer instruments, optionally auto-paginating all results."""
        if paginate_all:
            return self._paginate_all(
                self._instruments_api.get_customer_instruments,
                workspace_code=workspace_code,
            )
        self._ensure_authenticated()
        return self._instruments_api.get_customer_instruments(
            workspace_code=workspace_code,
            first=first,
            limit=limit,
        )

    def create_instrument(self, request: CustomerInstrumentRequest) -> CreatedResponse:
        """Register a new customer instrument."""
        self._ensure_authenticated()
        return self._instruments_api.create_customer_instrument(request)

    def update_instrument(
        self, metquay_id: int, request: CustomerInstrumentRequest
    ) -> None:
        """Update a customer instrument by Metquay ID."""
        self._ensure_authenticated()
        self._instruments_api.update_customer_instrument(metquay_id, request)

    def delete_instrument(self, metquay_id: int) -> None:
        """Delete a customer instrument by Metquay ID."""
        self._ensure_authenticated()
        self._instruments_api.delete_customer_instrument(metquay_id)

    # -- Instrument categories ---------------------------------------------
    # NOTE: The generated API has no list/get endpoint for instrument
    # categories. Only create, update, and delete are available.

    def create_instrument_category(
        self, request: InstrumentCategoryRequest
    ) -> CreatedResponse:
        """Create a new instrument category."""
        self._ensure_authenticated()
        return self._categories_api.create_instrument_category(request)

    def update_instrument_category(
        self, metquay_id: int, request: InstrumentCategoryRequest
    ) -> None:
        """Update an instrument category by Metquay ID."""
        self._ensure_authenticated()
        self._categories_api.update_instrument_category(metquay_id, request)

    def delete_instrument_category(self, metquay_id: int) -> None:
        """Delete an instrument category by Metquay ID."""
        self._ensure_authenticated()
        self._categories_api.delete_instrument_category(metquay_id)

    # -- Works -------------------------------------------------------------

    def list_works(
        self,
        *,
        first: Optional[int] = None,
        limit: Optional[int] = None,
        workspace_code: Optional[str] = None,
        paginate_all: bool = False,
    ) -> List[WorkResponse]:
        """List works, optionally auto-paginating all results."""
        if paginate_all:
            return self._paginate_all(
                self._works_api.get_works,
                workspace_code=workspace_code,
            )
        self._ensure_authenticated()
        return self._works_api.get_works(
            workspace_code=workspace_code,
            first=first,
            limit=limit,
        )

    def create_work(self, request: WorkRequest) -> CreatedResponse:
        """Create a new work order."""
        self._ensure_authenticated()
        return self._works_api.create_work(request)

    def update_work(self, metquay_id: int, request: WorkRequest) -> None:
        """Update a work order by Metquay ID."""
        self._ensure_authenticated()
        self._works_api.update_work(metquay_id, request)
