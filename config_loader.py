import yaml

def load_stack_config():
    try:
        with open("examples/stack_identity_card.example.yaml", "r") as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print("❌ Brak pliku konfiguracji stosu!")
        return None