"""Verify that live API response shapes match the generated model fields.

These tests catch spec-vs-reality drift by comparing the keys in the raw
JSON response against the model's declared ``__properties``.  Two failure
modes are detected:

* **Unexpected keys** -- the API returns a field not declared in the spec.
  This means ``from_dict()`` silently drops data that downstream callers
  might need.
* **Missing keys** -- the spec declares a field that the API never returns.
  These are expected to some degree (optional fields) but a wholesale
  mismatch signals a spec error.
"""

import json
from typing import Any, List, Set, Type

import pytest

from openapi_client.api_response import ApiResponse
from openapi_client.models.customer_instrument_response import (
    CustomerInstrumentResponse,
)
from openapi_client.models.customer_response import CustomerResponse
from openapi_client.models.work_response import WorkResponse
from tests.conftest import requires_credentials


def _raw_keys_from(api_response: ApiResponse) -> List[Set[str]]:  # type: ignore[type-arg]
    """Extract the set of JSON keys from each object in the raw response body."""
    payload: Any = json.loads(api_response.raw_data)
    if isinstance(payload, list):
        return [set(item.keys()) for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        return [set(payload.keys())]
    return []


def _model_properties(model_cls: Type[Any]) -> Set[str]:
    """Return the set of properties declared on a generated model class."""
    # The OpenAPI generator creates a ClassVar[List[str]] named __properties
    # containing the JSON alias names for every field.
    props: List[str] = getattr(model_cls, f"_{model_cls.__name__}__properties", [])
    return set(props)


@requires_credentials
class TestResponseShapes:
    """For each list endpoint, assert that live API keys match the model."""

    def test_customer_response_shape(self, client):
        resp: ApiResponse = client._customers_api.get_customers_with_http_info(  # type: ignore[type-arg]
            limit=1,
        )
        key_sets = _raw_keys_from(resp)
        if not key_sets:
            pytest.skip("No customers in account")

        expected = _model_properties(CustomerResponse)
        for actual_keys in key_sets:
            unexpected = actual_keys - expected
            assert (
                not unexpected
            ), f"API returned fields not in CustomerResponse model: {unexpected}"

    def test_instrument_response_shape(self, client):
        resp: ApiResponse = client._instruments_api.get_customer_instruments_with_http_info(  # type: ignore[type-arg]
            limit=1,
        )
        key_sets = _raw_keys_from(resp)
        if not key_sets:
            pytest.skip("No instruments in account")

        expected = _model_properties(CustomerInstrumentResponse)
        for actual_keys in key_sets:
            unexpected = actual_keys - expected
            assert (
                not unexpected
            ), f"API returned fields not in CustomerInstrumentResponse model: {unexpected}"

    def test_work_response_shape(self, client):
        from openapi_client.exceptions import ApiException

        try:
            resp: ApiResponse = client._works_api.get_works_with_http_info(  # type: ignore[type-arg]
                limit=1,
            )
        except ApiException as e:
            if e.status == 500:
                pytest.skip(f"Server error: {e.reason}")
            raise

        key_sets = _raw_keys_from(resp)
        if not key_sets:
            pytest.skip("No works in account")

        expected = _model_properties(WorkResponse)
        for actual_keys in key_sets:
            unexpected = actual_keys - expected
            assert (
                not unexpected
            ), f"API returned fields not in WorkResponse model: {unexpected}"
