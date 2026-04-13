# 📜 Changelog

Wszystkie istotne zmiany w projekcie **Google Autonomous Stack Template (GAST)** będą dokumentowane w tym pliku zgodnie z zasadami [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.1.0] - 2026-04-14
### Added
- Integracja metody `_ensure_infrastructure` w `main.py` — automatyczne tworzenie struktury `stack/` przy starcie agenta
- Dodanie `.claudecode.md` z Dual-Mode Strategy (publiczny `_Stack Template` / prywatny `_My Projects`)
- Dodanie `ANTI_GRAVITY_SECURITY_MANIFEST.md` — pełny manifest filozofii Direct-to-Silicon
- Ujednolicenie ścieżek konfiguracji (`stack/config/stack_identity_card.yaml` jako canonical, z fallback na `examples/`)
- Domyślne wartości wszystkich placeholderów w `_assemble_system_instructions()`

### Changed
- Zaktualizowana `STRUKTURA.md` — uwzględnienie wszystkich plików implementacyjnych
- Zaktualizowany `SETUP.md` — pełna instrukcja z `pip install -r requirements.txt` i sekcją testów

---
## [1.0.0] - 2025-03-01
### Added
- **Inicjalizacja Architektury Anti-Gravity**: Wdrożenie fundamentów lekkości i bezpośredniej komunikacji z modelami.
- **Security Manifest**: Dodanie dokumentacji `ANTI_GRAVITY_SECURITY_MANIFEST.md` w odpowiedzi na raporty UCSB o atakach Intermediary.
- **Dual-Mode Support**: Przygotowanie struktury pod separację projektów publicznych (B) i prywatnych (C).
- **Global Skills**: Wprowadzenie modułów `skill_verification`, `skill_memory` oraz `skill_didactic`.
- **Onboarding Framework**: Dodanie kwestionariusza Q0-Q7 w celu standaryzacji startu nowych agentów.

### Changed
- Ujednolicony standard nazewnictwa dla agentów (Orchestrator/Worker).
- Optymalizacja struktury `.claude/` pod mechanizm dziedziczenia reguł.

### Security
- Wdrożenie protokołu **Prompt Anchoring** (HMAC-SHA256) jako standardu weryfikacji integralności promptów.
- Restrykcyjna polityka `.gitignore` dla plików środowiskowych `.env`.

---
## [0.9.0] - 2025-01-15
### Added
- Pierwsze szkice struktury folderów dla Akademii Leona Koźmińskiego.
- Koncepcja "Direct-to-Silicon" dla Google Gemini.