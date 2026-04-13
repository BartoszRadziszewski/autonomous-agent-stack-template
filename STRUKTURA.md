STRUKTURA (v2 — 2026-04-14)

autonomous-agent-stack-template/          ← [ROOT REPOZYTORIUM]
│
├── README.md                             ← Landing page (Misja DFE/ALK, badge, opis Anti-Gravity)
├── SETUP.md                              ← Instrukcja: klucze API, venv, pierwsze kroki, testy
├── CHANGELOG.md                          ← Historia wersji (od v0.9.0)
├── STRUKTURA.md                          ← Ten plik — mapa projektu
├── LICENSE (MIT LICENENSE.md)            ← Licencja MIT
├── .gitignore                            ← Wyklucza .env, __pycache__, stack/logs/, stack/memory/
├── .env.example                          ← Szablon zmiennych środowiskowych
├── .claudecode.md                        ← Instrukcja dla Claude Code (Dual-Mode Safety)
├── ANTI_GRAVITY_SECURITY_MANIFEST.md     ← Manifest (UCSB, Direct-to-Model, Prompt Anchoring)
├── EVALS.md                              ← Scenariusze ewaluacyjne E1–E3 dla agenta
├── requirements.txt                      ← Zależności Python (google-generativeai, chromadb…)
│
├── [IMPLEMENTACJA]
├── main.py                               ← Główny runner — klasa AntiGravityAgent
├── generate_identity.py                  ← Interaktywny generator stack_identity_card.yaml
├── config_loader.py                      ← Loader konfiguracji YAML (helper)
├── logger.py                             ← AntiGravityLogger — logi JSON/JSONL
├── sql_bridge.py                         ← Mostek SQLite (lokalny, No-Proxy)
├── INTEGRITY_CHECK.py                    ← Weryfikacja sum kontrolnych (HMAC-SHA256)
├── distribute_files.py                   ← Skrypt dystrybucji do _Stack Template
│
├── [CI/CD]
├── anti-gravity-ci.yml                   ← GitHub Actions: wykrywanie API key leaks + testy
│
├── [TESTY]
├── test_security_rules.py                ← pytest: weryfikacja zasad No-Proxy i integralności
│
├── .claude/                              ← [LOGIKA AGENTA]
│   ├── CLAUDE.md                         ← Instrukcje projektowe (placeholdery wypełniane z config)
│   ├── skills/                           ← [MODUŁY UMIEJĘTNOŚCI]
│   │   ├── skill_rag.md                  ← Zarządzanie wiedzą (Vector DB)
│   │   ├── skill_verification.md         ← Procedura Prompt Anchoring
│   │   ├── skill_didactic.md             ← Wsparcie edukacyjne (ALK/DFE)
│   │   ├── skill_memory.md               ← Zarządzanie kontekstem sesji
│   │   └── skill_observability.md        ← Monitorowanie kosztów i tokenów
│   ├── agents/                           ← [DEFINICJE RÓL]
│   │   ├── agent_worker.md               ← Instrukcja wykonawcza
│   │   └── agent_orchestrator.md         ← Logika zarządzania zadaniami
│   └── rules/                            ← [ZASADY OGÓLNE]
│       └── rules_governance.md           ← Standardy etyczne i operacyjne (Financial Integrity)
│
├── onboarding/                           ← [PROCES STARTOWY]
│   └── ONBOARDING.md                     ← Kwestionariusz Q0–Q7 + Decision Tree (architektury)
│
├── docs/                                 ← [DOKUMENTACJA MERYTORYCZNA]
│   ├── WHEN_TO_USE.md                    ← Poradnik: Single vs Multi-Agent
│   ├── CONTRIBUTING.md                   ← Jak studenci mogą rozwijać projekt
│   └── THREAT_MODEL_AND_INTEGRITY.md     ← Opis zagrożeń Intermediary Attacks (UCSB)
│
├── examples/                             ← [SZABLONY KONFIGURACYJNE]
│   ├── stack_identity_card.example.yaml  ← Metadane stosu (punkt startowy przed generate_identity.py)
│   └── agent.example.yaml                ← Przykładowa definicja agenta z cost_constraints
│
├── stack/                                ← [RUNTIME — tworzony automatycznie przez main.py]
│   ├── config/                           ← stack_identity_card.yaml (canonical config)
│   ├── logs/                             ← agent_runtime.log, audit logs (.gitignored)
│   ├── memory/                           ← Stan sesji agenta (.gitignored)
│   ├── data/                             ← Pliki wejściowe Excel/CSV (.gitignored)
│   └── security/                         ← Kotwice integralności (.gitignored)
│
└── archiwum/                             ← [WERSJE POPRZEDNIE — zgodnie z protokołem wersjonowania]
    ├── CHANGELOG_v1.md
    └── STRUKTURA_v1.md

