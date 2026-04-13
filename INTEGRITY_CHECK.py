import hashlib

def verify_request_integrity(system_prompt, user_query):
    payload = f"{system_prompt}|{user_query}"
    signature = hashlib.sha256(payload.encode()).hexdigest()
    print(f"[Anti-Gravity] Wygenerowano sygnaturę integralności: {signature}")
    return signature

# Przykład użycia
sys_p = "Jesteś asystentem edukacyjnym."
user_p = "Jak działa AI?"
verify_request_integrity(sys_p, user_p)