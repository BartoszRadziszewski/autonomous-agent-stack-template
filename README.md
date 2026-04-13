# Google Autonomous Stack Template (GAST)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Security-Direct--to--Model-red)
![ALK](https://img.shields.io/badge/Partner-ALK%20Kozminski-navy)

Oficjalny szablon agentowy wspierający studia podyplomowe **"AI w Finansach i Controllingu Przedsiębiorstw"** na Akademii Leona Koźmińskiego (ALK) oraz projekty **Fundacji Klub Dyrektorów Finansowych (KDF)**.

---

## O projekcie

GAST to minimalistyczny framework dla autonomicznych agentów AI oparty na filozofii **Anti-Gravity** — lekkości, bezpieczeństwie i bezpośrednim połączeniu z Google Gemini.

### Główne cechy

- **Anti-Gravity Architecture** — brak zbędnych warstw pośrednich, natywny SDK Google
- **Security-First** — ochrona przed Intermediary Attacks (badania UCSB), Prompt Anchoring (HMAC-SHA256)
- **Ready for Finance** — moduły weryfikacji, obserwowalności kosztów i wsparcia edukacyjnego
- **Dual-Mode** — separacja projektów publicznych (szablony) i prywatnych (dane biznesowe)

---

## Szybki start

```bash
git clone https://github.com/<twoja-nazwa>/autonomous-agent-stack-template.git
cd autonomous-agent-stack-template

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/macOS

pip install -r requirements.txt
cp .env.example .env           # uzupelnij GOOGLE_API_KEY

python generate_identity.py    # interaktywna konfiguracja
python main.py
```

Klucz API Google pobierzesz bezplatnie z [Google AI Studio](https://aistudio.google.com/).

---

## Struktura projektu

```
autonomous-agent-stack-template/
├── main.py                    ← Runner agenta (AntiGravityAgent)
├── requirements.txt           ← Zaleznosci Python
├── .env.example               ← Szablon konfiguracji
├── .claude/                   ← Logika agenta (skills, agents, rules)
├── onboarding/                ← Kwestionariusz startowy Q0-Q7
├── docs/                      ← Dokumentacja (Single vs Multi-Agent, Contributing)
├── examples/                  ← Szablony YAML (stack identity, agent definition)
└── stack/                     ← Runtime (tworzony automatycznie, gitignored)
```

Pelna mapa: [STRUKTURA.md](STRUKTURA.md)

---

## Bezpieczenstwo

Projekt implementuje zasady z raportu **University of California, Santa Barbara** o atakach Intermediary:

1. **Direct-to-Model** — polaczenie wylacznie z `googleapis.com`, bez routerow API
2. **Prompt Anchoring** — weryfikacja integralnosci instrukcji systemowych (HMAC-SHA256)
3. **Context Isolation** — separacja kluczy API miedzy strefami publiczna i prywatna

Szczegoły: [ANTI_GRAVITY_SECURITY_MANIFEST.md](ANTI_GRAVITY_SECURITY_MANIFEST.md)

---

## Dla studentow ALK / czlonkow KDF

1. Przejdz `onboarding/ONBOARDING.md` — kwestionariusz Q0-Q7 dopasuje architekture do Twojego projektu
2. Sprawdz `docs/WHEN_TO_USE.md` — kiedy Single Agent, a kiedy Multi-Agent
3. Uruchom `python generate_identity.py` — wygeneruj konfiguracje swojego stosu
4. Czytaj komentarze w kodzie — agent tlumaczyl kazdy krok (skill_didactic)

---

## Autor i partnerzy

**Autor:** Bartosz Radziszewski — [dfe.org.pl](https://dfe.org.pl)

**Partnerzy:**
- [Akademia Leona Kozminskiego](https://kozminski.edu.pl) — studia podyplomowe AI w Finansach
- [Fundacja Klub Dyrektorow Finansowych](https://kdf.org.pl) — KDF Dialog

---

## Licencja

MIT License — szczegoly w pliku [LICENSE](LICENSE).
