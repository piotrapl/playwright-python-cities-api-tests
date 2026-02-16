import playwright
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

# api_request to:
# 1. technicznie: fikstura (pytest fixture), która:
#   - jest funkcją
#   - jest oznaczona dekoratorem @pytest.fixture, 
#   - zarządzana przez pytest, który dba o jej tworzenie i usuwanie
#   - jest wstrzykiwana do metod testowych jako argument, 
#     dzięki czemu testy mogą korzystać z tego samego kontekstu APIRequestContext
# 2. to też: instancja klasy: playwright.sync_api.APIRequestContext
#    APIRequestContext to:
#          klasa z modułu playwright.sync_api,
#    - reprezentująca sesję klienta HTTP używaną do wysyłania zapytań API
#    - inaczej: kontekst do wykonywania zapytań HTTP do testowanego API,
#               współdzielony między testami, 
#    APIRequestContext  ->  klasa
#    api_request        ->  intancja tej klasy

# 3. to też: fikcyjny klient API (Fake API client) - określenie mniej formalne, bardziej opisowe
#     technicznie niezbyt precyzyjne, bo:
#       - nie mockuje niczego,
#       - wysyła prawdziwe requesty HTTP
#       - nie jest to stub (atrapa, zaślepka), coś co udaje prawdziwy obiekt, ale nie wykonuje jego rzeczywistej funkcjonalności,
#       także:
#       - używa prawdziwego endpointu,
#       - wykonuje prawdziwe wywołania sieciowe,
#       - waliduje prawdziwe response'y,
# precyzyjniej niż 'fake API client' można by powiedzieć, że to:
#       1. wrapper na klienta API = warstwa opakowująca klienta API
#       2. fikstura (fxture) klienta HTTP (HTTP client fixture)
#       3. współdzielony kontekst zapytań HTTP do testowanego API (shared API request context)  
#      ale jest to określenie użyte w celu podkreślenia, że nie jest to prawdziwy klient AP