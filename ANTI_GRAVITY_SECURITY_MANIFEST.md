# 🛡️ Manifest Bezpieczeństwa Anti-Gravity (AGSM)

## 1. Wstęp i Filozofia
Manifest definiuje standard "Direct-to-Silicon". Eliminujemy zbędne warstwy pośrednie w komunikacji z modelami AI, aby zminimalizować ryzyko wycieku danych finansowych i manipulacji promptami.

## 2. Ochrona przed Intermediary Attacks (Raport UCSB)
Zgodnie z badaniami University of California, pośrednicy LLM stanowią krytyczne zagrożenie:
- Deszyfrują połączenie TLS w locie.
- Mają dostęp do treści promptów (w tym danych ERP/FK).
- Mogą wstrzykiwać instrukcje (Prompt Injection).

**Zasada nr 1: Direct-to-Model (No-Proxy)**
Wszystkie implementacje w tym stosie łączą się wyłącznie bezpośrednio z oficjalnymi endpointami dostawcy (np. `googleapis.com`).

## 3. Kryptograficzna Integralność (Prompt Anchoring)
Każdy agent operujący na danych wrażliwych musi stosować mechanizm kotwiczenia:
- **Hashing**: Instrukcje systemowe generują sumę kontrolną SHA-256 przed wysłaniem.
- **Weryfikacja**: Agent akceptuje odpowiedź modelu tylko, jeśli potwierdza ona nienaruszony kontekst operacyjny.

## 4. Separacja Kontekstów (Context Isolation)
Nigdy nie używamy tych samych kluczy API dla Strefy B (Publicznej) i Strefy C (Prywatnej). Klucze biznesowe nigdy nie opuszczają lokalnego pliku `.env`.

## 5. Minimalizm Technologiczny
Złożoność jest wrogiem bezpieczeństwa. Preferujemy czysty kod (Native SDK) nad ciężkimi frameworkami (LangChain/LlamaIndex).