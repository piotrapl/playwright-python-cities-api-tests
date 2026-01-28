import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def api_request():
    """
    Wspólny kontekst APIRequestContext dla wszystkich testów (szybki).
    ignore_https_errors=True ponieważ certyfikat SSL API może być nieaktualny.
    """
    base_url = "https://local-gov-units.polandapi.com"

    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url=base_url,
            ignore_https_errors=True
        )
        yield request_context
        request_context.dispose()