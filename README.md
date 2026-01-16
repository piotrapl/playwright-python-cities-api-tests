# playwright-python_miasta_powiaty_wojew-api-tests
# Testy atomatyczne serwisu RESTful API dla polskich jednostek samorządu terytorialnego (JST) - Playwright/Python/unittest

## Zakres projektu

- Automatyzacja testów **REST API**
- Testy endpointów typu **GET**
- Testy **pozytywne i negatywne**
- Testy **data-driven**
- Walidacja odpowiedzi API (m.in. status, struktura)
- Generowanie **raportu HTML**
  Raport zostanie zapisany w katalogu reports/
- Projekt gotowy do uruchomienia w **CI**

## Technologie

- Python 3.9+
- Playwright (APIRequestContext)
- unittest
- HTML Test Runner

## Wymagania

- Python **3.9+**
- pip
- Dostęp do Internetu
- Windows / macOS / Linux

## Uruchomienie projektu

```bash
git clone <adres-repozytorium>
cd api-playwright-polish-gov
pip install -r requirements.txt
playwright install
python run_tests.py
