import pytest
from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# znak @ oznacza dekorator w Pythonie, który modyfikuje funkcję poniżej
# scope="session" - tzn, że fixture będzie utworzony raz na sesję testową
# tekst ograniczony """ (3 znakami ") to docstring funkcji, jej dokumentacja

@pytest.fixture(scope="session")
def api_request():
    """
    Wspólny kontekst APIRequestContext dla wszystkich testów (szybki).
    ignore_https_errors=True - powód: certyfikat SSL API w przypadku tej usługi
    może być nieaktualny.
    """
    base_url = "https://local-gov-units.polandapi.com"

    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url=base_url,
            ignore_https_errors=True
        )
        yield request_context
        request_context.dispose()