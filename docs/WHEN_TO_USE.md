# Kiedy stosować dany model agenta?

### 1. Single-Agent (Worker)
- Proste skrypty automatyzacji.
- Analiza pojedynczego pliku Word/Excel/PowerPoint/xml/html/pdf/txt/csv/md.
- Szybkie prototypowanie promptów.

### 2. Multi-Agent (Orchestrator + Workers)
- Systemy ERP/FA/DMS/CRM/LMS.
- Procesy wymagające weryfikacji przez drugą instancję (Verifier pattern).
- Zadania długofalowe z dużą ilością danych kontekstowych.

### 3. Anti-Gravity Bridge
- Gdy wymagane jest połączenie z lokalną bazą SQL bez wystawiania jej na świat.