"""Read-only integration tests for the Metquay API wrapper.

These tests only call list/read endpoints. They never create, update, or
delete resources. They require valid API credentials in .env or environment
variables.
"""

import pytest

from openapi_client.exceptions import ApiException
from tests.conftest import requires_credentials


@requires_credentials
class TestAuthentication:
    def test_authenticate_returns_token(self, client):
        """Explicitly calling authenticate() should return a valid token."""
        response = client.authenticate()
        assert response.access_token
        assert response.token_type.lower() == "bearer"

    def test_token_is_reused_on_subsequent_calls(self, client):
        """After authenticating, the internal token should be reused."""
        client.authenticate()
        token_1 = client._token
        # A list call should NOT trigger re-auth (token is fresh)
        client.list_customers(limit=1)
        assert client._token == token_1


@requires_credentials
class TestListCustomers:
    def test_list_customers_returns_list(self, client):
        customers = client.list_customers(limit=5)
        assert isinstance(customers, list)

    def test_list_customers_pagination(self, client):
        page1 = client.list_customers(first=0, limit=2)
        page2 = client.list_customers(first=2, limit=2)
        assert isinstance(page1, list)
        assert isinstance(page2, list)
        if len(page1) == 2 and len(page2) > 0:
            assert page1 != page2

    def test_list_customers_paginate_all(self, client):
        all_customers = client.list_customers(paginate_all=True)
        assert isinstance(all_customers, list)
        single_page = client.list_customers(limit=50)
        assert len(all_customers) >= len(single_page)


@requires_credentials
class TestListInstruments:
    def test_list_instruments_returns_list(self, client):
        instruments = client.list_instruments(limit=5)
        assert isinstance(instruments, list)

    def test_list_instruments_pagination(self, client):
        page = client.list_instruments(first=0, limit=2)
        assert isinstance(page, list)


@requires_credentials
class TestListWorks:
    def test_list_works_returns_list(self, client):
        try:
            works = client.list_works(limit=5)
            assert isinstance(works, list)
        except ApiException as e:
            if e.status == 500:
                pytest.skip(f"Server error: {e.reason}")
            raise

    def test_list_works_pagination(self, client):
        try:
            page = client.list_works(first=0, limit=2)
            assert isinstance(page, list)
        except ApiException as e:
            if e.status == 500:
                pytest.skip(f"Server error: {e.reason}")
            raise
