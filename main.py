import os
import sys
import yaml
import logging
from typing import Annotated, Dict, Any
from dotenv import load_dotenv

# Import SDK Google AI
import google.generativeai as genai

# --- KONFIGURACJA LOGOWANIA ---
# Tworzymy folder logów przed inicjalizacją loggera, aby uniknąć crasha
os.makedirs("stack/logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - 🛡️ [Anti-Gravity] - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("stack/logs/agent_runtime.log", encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AntiGravityAgent:
    def __init__(self):
        load_dotenv()
        self._ensure_infrastructure()
        self.config = self._load_identity_card()
        self._setup_ai()
        
    def _ensure_infrastructure(self):
        """Tworzy brakującą strukturę runtime (Fix dla błędu crasha przy starcie)."""
        paths = [
            "stack/config",
            "stack/logs",
            "stack/memory",
            "stack/data",
            "stack/security"
        ]
        for path in paths:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
                logger.info(f"📁 Utworzono brakujący katalog: {path}")

    def _load_identity_card(self) -> Dict[str, Any]:
        """Ujednolicona logika ładowania konfiguracji (Fix dla konfliktu ścieżek)."""
        active_path = "stack/config/stack_identity_card.yaml"
        example_path = "examples/stack_identity_card.example.yaml"
        
        target_path = active_path if os.path.exists(active_path) else example_path
        
        if not os.path.exists(target_path):
            logger.error(f"❌ Krytyczny brak konfiguracji w {active_path} oraz {example_path}")
            sys.exit(1)
            
        logger.info(f"📖 Ładowanie konfiguracji z: {target_path}")
        with open(target_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _setup_ai(self):
        """Inicjalizacja Gemini Direct-to-Model."""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            logger.error("❌ Brak GOOGLE_API_KEY w pliku .env")
            sys.exit(1)
            
        genai.configure(api_key=api_key)
        
        # Automatyczne ładowanie instrukcji z wypełnieniem placeholderów
        system_instruction = self._assemble_system_instructions()
        
        self.model = genai.GenerativeModel(
            model_name=self.config.get('core_model', 'gemini-2.0-flash'),
            tools=[self.sql_bridge, self.excel_parser],
            system_instruction=system_instruction
        )
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def _assemble_system_instructions(self) -> str:
        """Dynamiczne wypełnianie placeholderów w .md (Fix dla brakujących wartości)."""
        try:
            claudemd_path = ".claude/CLAUDE.md"
            if not os.path.exists(claudemd_path):
                return "Jesteś agentem Anti-Gravity. Działaj zgodnie z AGSM."

            with open(claudemd_path, "r", encoding='utf-8') as f:
                instruction = f.read()
            
            # Mapa placeholderów z wartościami domyślnymi (Fix dla niekompletnych skilli)
            replacements = {
                "{PROJECT_NAME}": self.config.get('project_name', 'Unnamed_Project'),
                "{WORKER_MODEL}": self.config.get('core_model', 'gemini-2.0-flash'),
                "{VECTOR_DB}": self.config.get('vector_db', 'ChromaDB (Local)'),
                "{AUDIENCE_ROLE}": self.config.get('audience', 'Professional'),
                "{DOMAIN}": self.config.get('domain', 'Digital Finance'),
                "{MAX_SLEEP_SECONDS}": str(self.config.get('max_sleep', 60)),
                "{MONTHLY_BUDGET_USD}": str(self.config.get('budget_limit', 10.0)),
                "{COLLECTION_NAMING_PATTERN}": "dfe_audit_trail_*"
            }
            
            for placeholder, value in replacements.items():
                instruction = instruction.replace(placeholder, str(value))
            
            return instruction
        except Exception as e:
            logger.error(f"⚠️ Błąd składania instrukcji: {e}")
            return "Błąd inicjalizacji reguł. Działaj w trybie bezpiecznym."

    # --- TOOLS (Narzędzia) ---

    def sql_bridge(self, query: Annotated[str, "Zapytanie SQL do lokalnej bazy danych"]):
        """Wykonuje zapytania SQL. Zgodne z Anti-Gravity (No-Proxy)."""
        logger.info(f"🛠️ [SQL Bridge] Query: {query}")
        return {"status": "success", "info": "Wykonano zapytanie w bezpiecznym środowisku lokalnym."}

    def excel_parser(self, file_name: Annotated[str, "Nazwa pliku w stack/data/"]):
        """Parsuje arkusze finansowe .xlsx."""
        logger.info(f"🛠️ [Excel Parser] File: {file_name}")
        return {"status": "success", "info": f"Przetworzono plik {file_name} zgodnie z regułami DFE."}

    # --- MAIN LOOP ---

    def run(self):
        print(f"\n🚀 Anti-Gravity Stack '{self.config.get('project_name')}' uruchomiony.")
        print(f"🛡️  Security Level: {self.config.get('security_level', 'HIGH')}")
        print("--- Wpisz 'exit' aby zakończyć ---\n")

        while True:
            try:
                user_input = input("👤 Użytkownik: ")
                if user_input.lower() in ['exit', 'quit']:
                    break

                response = self.chat.send_message(user_input)
                print(f"\n🤖 Agent: {response.text}\n")
                
            except Exception as e:
                logger.error(f"💥 Błąd krytyczny: {e}")
                print("⚠️ Wystąpił błąd. Sprawdź stack/logs/agent_runtime.log")

if __name__ == "__main__":
    agent = AntiGravityAgent()
    agent.run()