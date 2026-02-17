"""Shared fixtures for pymetquay integration tests."""

import os

import pytest
from dotenv import load_dotenv

load_dotenv()


def _credentials_available() -> bool:
    has_access = bool(
        os.environ.get("METQUAY_ACCESS_KEY") or os.environ.get("ACCESS_KEY")
    )
    has_secret = bool(
        os.environ.get("METQUAY_SECRET_KEY") or os.environ.get("SECRET_KEY")
    )
    return has_access and has_secret


requires_credentials = pytest.mark.skipif(
    not _credentials_available(),
    reason="METQUAY_ACCESS_KEY and METQUAY_SECRET_KEY not set",
)


@pytest.fixture(scope="session")
def client():
    """Session-scoped MetquayClient shared across all integration tests."""
    from pymetquay import MetquayClient

    with MetquayClient() as c:
        yield c
