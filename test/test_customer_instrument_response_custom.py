"""
Custom date parsing tests for Customer InstrumentResponse.
These tests are NOT automatically generated because the custom _parse_date
validator is not part of the OpenAPI spec metadata.
"""

from datetime import date

from openapi_client.models.customer_instrument_response import CustomerInstrumentResponse


class TestCustomerInstrumentResponseCustom:
    """Custom tests for CustomerInstrumentResponse date parsing."""

    def test_date_parsing_mm_dd_yyyy(self):
        """Test that dates in MM-dd-yyyy format are parsed correctly."""
        obj = CustomerInstrumentResponse(
            calibrated_date="12-18-2025",
            due_date="06-18-2026",
            verification_due_date="03-18-2026",
            last_received_date="12-01-2025",
            last_delivered_date="12-20-2025",
            audited_date="11-15-2025",
        )
        assert obj.calibrated_date == date(2025, 12, 18)
        assert obj.due_date == date(2026, 6, 18)
        assert obj.verification_due_date == date(2026, 3, 18)
        assert obj.last_received_date == date(2025, 12, 1)
        assert obj.last_delivered_date == date(2025, 12, 20)
        assert obj.audited_date == date(2025, 11, 15)

    def test_date_parsing_yyyy_mm_dd(self):
        """Test that dates in yyyy-MM-dd format (ISO) are also parsed."""
        obj = CustomerInstrumentResponse(
            calibrated_date="2025-12-18",
            due_date="2026-06-18",
        )
        assert obj.calibrated_date == date(2025, 12, 18)
        assert obj.due_date == date(2026, 6, 18)

    def test_date_none_is_preserved(self):
        """Test that None values for date fields are preserved."""
        obj = CustomerInstrumentResponse(
            calibrated_date=None,
            due_date=None,
        )
        assert obj.calibrated_date is None
        assert obj.due_date is None

    def test_date_object_passthrough(self):
        """Test that date objects can be passed directly."""
        d = date(2025, 12, 18)
        obj = CustomerInstrumentResponse(calibrated_date=d)
        assert obj.calibrated_date == d

    def test_from_dict_with_date_strings(self):
        """Test that from_dict works with date strings in the dict."""
        data = {
            "calibratedDate": "12-18-2025",
            "dueDate": "06-18-2026",
        }
        obj = CustomerInstrumentResponse.from_dict(data)
        assert obj.calibrated_date == date(2025, 12, 18)
        assert obj.due_date == date(2026, 6, 18)
