"""
Custom date parsing tests for WorkResponse.
These tests are NOT automatically generated because the custom _parse_date
validator is not part of the OpenAPI spec metadata.
"""

import unittest
from datetime import date

from openapi_client.models.work_response import WorkResponse


class TestWorkResponseCustom(unittest.TestCase):
    """Custom tests for WorkResponse date parsing."""

    def test_date_parsing_mm_dd_yyyy(self):
        """Test that dates in MM-dd-yyyy format are parsed correctly."""
        obj = WorkResponse(
            in_date="12-18-2025",
            delivery_date="01-15-2025",
            work_date="02-20-2025",
            due_date="03-01-2025",
            finished_date="04-10-2025",
            recommended_due_date="05-05-2025",
            calibrated_date="06-15-2025",
            work_start_date="07-20-2025",
        )
        self.assertEqual(obj.in_date, date(2025, 12, 18))
        self.assertEqual(obj.delivery_date, date(2025, 1, 15))
        self.assertEqual(obj.work_date, date(2025, 2, 20))
        self.assertEqual(obj.due_date, date(2025, 3, 1))
        self.assertEqual(obj.finished_date, date(2025, 4, 10))
        self.assertEqual(obj.recommended_due_date, date(2025, 5, 5))
        self.assertEqual(obj.calibrated_date, date(2025, 6, 15))
        self.assertEqual(obj.work_start_date, date(2025, 7, 20))

    def test_date_parsing_yyyy_mm_dd(self):
        """Test that dates in yyyy-MM-dd format (ISO) are also parsed."""
        obj = WorkResponse(
            work_date="2025-02-20",
            due_date="2025-03-01",
        )
        self.assertEqual(obj.work_date, date(2025, 2, 20))
        self.assertEqual(obj.due_date, date(2025, 3, 1))

    def test_date_none_is_preserved(self):
        """Test that None values for date fields are preserved."""
        obj = WorkResponse(
            work_date=None,
            due_date=None,
        )
        self.assertIsNone(obj.work_date)
        self.assertIsNone(obj.due_date)

    def test_date_object_passthrough(self):
        """Test that date objects can be passed directly."""
        d = date(2025, 12, 18)
        obj = WorkResponse(work_date=d)
        self.assertEqual(obj.work_date, d)

    def test_from_dict_with_date_strings(self):
        """Test that from_dict works with date strings in the dict."""
        data = {
            "workDate": "02-20-2025",
            "dueDate": "03-01-2025",
        }
        obj = WorkResponse.from_dict(data)
        self.assertEqual(obj.work_date, date(2025, 2, 20))
        self.assertEqual(obj.due_date, date(2025, 3, 1))


if __name__ == "__main__":
    unittest.main()
