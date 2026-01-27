import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def api_request():
    """
    Shared APIRequestContext for all tests (fast).
    ignore_https_errors=True because the API SSL cert may be expired.
    """
    base_url = "https://local-gov-units.polandapi.com"

    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url=base_url,
            ignore_https_errors=True
        )
        yield request_context
        request_context.dispose()