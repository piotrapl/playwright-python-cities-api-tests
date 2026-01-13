# playwright-python_miasta_powiaty_wojew-api-tests
# Testy serwisu RESTful API dla polskich jednostek samorządu terytorialnego (JST) - Playwright/Python/unittest

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-Testy%20API-green)
![CI](https://img.shields.io/github/actions/workflow/status/<TWOJ_GITHUB_USERNAME>/<NAZWA_REPO>/ci.yml)

Projekt demonstracyjny automatyzacji testów API przygotowany z myślą o **stanowiskach QA / Automation Engineer**.  
Repozytorium pokazuje praktyczne użycie **Playwright (Python)**, **testów opartych o dane** oraz **czytelnej struktury testów API**.

---

## Zakres projektu

- Automatyzacja testów **REST API**
- Testy endpointów typu **GET**
- Testy **pozytywne i negatywne**
- Testy **data-driven**
- Walidacja odpowiedzi API (status, struktura, pola biznesowe)
- Generowanie **raportu HTML**
- Projekt gotowy do uruchomienia w **CI**

---

## Technologie

- Python 3.9+
- Playwright (APIRequestContext)
- unittest
- HTML Test Runner

---

## Wymagania

- Python **3.9+**
- pip
- Dostęp do Internetu
- Windows / macOS / Linux

---

## Uruchomienie projektu

```bash
git clone <adres-repozytorium>
cd api-playwright-polish-gov
pip install -r requirements.txt
playwright install
python run_tests.py
