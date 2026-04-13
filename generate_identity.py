import yaml
import os

def run_onboarding():
    print("🚀 Anti-Gravity Onboarding: Generowanie Stack Identity Card\n")
    
    config = {
        "stack_id": f"AG-{os.urandom(2).hex().upper()}",
        "project_name": input("Q1: Nazwa projektu: "),
        "audience": input("Q2: Kto jest odbiorcą (np. Student ALK, CFO VIVE): "),
        "vector_db": input("Q3: Typ Vector DB (np. ChromaDB): "),
        "budget_limit": float(input("Q7: Miesięczny limit USD: ") or 10.0),
        "security_level": "High (Strict Direct-to-Model)"
    }

    path = "stack/config/stack_identity_card.yaml"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, "w") as f:
        yaml.dump(config, f)
    
    print(f"\n✅ Sukces! Plik utworzony w {path}")

if __name__ == "__main__":
    run_onboarding()