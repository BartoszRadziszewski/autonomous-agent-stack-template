# Instrukcja Wdrozenia Systemu Anti-Gravity

Niniejszy przewodnik przeprowadzi Cię przez proces instalacji i konfiguracji Twojego pierwszego autonomicznego agenta w architekturze **Google Autonomous Stack Template (GAST)**.

---

## 1. Wymagania wstepne
- **Python**: Wersja 3.10 lub nowsza.
- **Google AI API Key**: Pobierz klucz z [Google AI Studio](https://aistudio.google.com/).
- **Git**: Do sklonowania repozytorium.

---

## 2. Instalacja srodowiska

Otwórz terminal w głównym folderze projektu i wykonaj poniższe kroki:

### A. Konfiguracja wirtualnego srodowiska (VENV)
```bash
# Tworzenie srodowiska
python -m venv venv

# Aktywacja (Windows)
venv\Scripts\activate

# Aktywacja (Linux/macOS)
source venv/bin/activate
```

### B. Instalacja zaleznosci
```bash
pip install -r requirements.txt
```

Plik `requirements.txt` zawiera wszystkie wymagane biblioteki:
- `google-generativeai` — oficjalny SDK Google Gemini
- `python-dotenv` — ladowanie zmiennych z `.env`
- `pandas` — analiza danych finansowych
- `openpyxl` — parsowanie plikow Excel (.xlsx)
- `chromadb` — lokalny Vector DB (RAG)

---

## 3. Konfiguracja kluczy API

Skopiuj plik `.env.example` do `.env` i uzupelnij klucz API:

```bash
cp .env.example .env
```

Nastepnie edytuj `.env`:
```
GOOGLE_API_KEY=TU_WKLEJ_SWOJ_KLUCZ
INTEGRITY_SECRET=dowolny_losowy_string
DATA_PATH=./stack/data
DEBUG=True
```

> Klucz pobierzesz bezplatnie z: https://aistudio.google.com/

---

## 4. Inicjalizacja projektu (Onboarding)

Uruchom interaktywny generator konfiguracji:

```bash
python generate_identity.py
```

Skrypt przeprowadzi Cię przez pytania (podobne do Q0-Q7 z `onboarding/ONBOARDING.md`) i wygeneruje plik `stack/config/stack_identity_card.yaml`.

Alternatywnie — przejdz reczny onboarding: otwórz `onboarding/ONBOARDING.md` i odpowiedz na pytania Q0-Q7.

---

## 5. Uruchomienie agenta

```bash
python main.py
```

Agent automatycznie:
1. Tworzy strukture folderów `stack/` (jesli nie istnieje)
2. Laduje konfiguracje z `stack/config/stack_identity_card.yaml`
3. Inicjalizuje polaczenie Direct-to-Model z Google Gemini
4. Uruchamia petlę konwersacyjna

Logi zapisywane sa w `stack/logs/agent_runtime.log`.

---

## 6. Weryfikacja bezpieczenstwa i testy

### Sprawdzenie integralnosci (HMAC)
```bash
python INTEGRITY_CHECK.py
```

### Uruchomienie testów bezpieczenstwa (pytest)
```bash
pip install pytest
pytest test_security_rules.py -v
```

Testy sprawdzaja:
- Brak zakazanych routerów API w kodzie (OpenRouter, Helicone itp.)
- Istnienie `ANTI_GRAVITY_SECURITY_MANIFEST.md`

---

## 7. Struktura folderów runtime (generowana automatycznie)

Po pierwszym uruchomieniu `main.py` pojawi sie folder `stack/`:
```
stack/
├── config/   ← stack_identity_card.yaml (Twoja konfiguracja)
├── logs/     ← agent_runtime.log
├── memory/   ← stan sesji agenta
├── data/     ← pliki Excel/CSV do analizy
└── security/ ← kotwice integralnosci
```

> Folder `stack/` jest wykluczony z Git (`.gitignore`) — zawiera dane runtime.

---

## Szybki start (TL;DR)

```bash
git clone <repo-url>
cd autonomous-agent-stack-template
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # uzupelnij GOOGLE_API_KEY
python generate_identity.py
python main.py
```
