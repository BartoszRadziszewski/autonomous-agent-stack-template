# Bezpieczeństwo: Raport Intermediary Attacks

Zgodnie z badaniami University of California, Santa Barbara, pośrednicy (routery API) mogą manipulować Twoim kodem. 

### Nasze rozwiązanie:
1. **Direct-to-Silicon**: Łączymy się tylko bezpośrednio z `googleapis.com`.
2. **Kryptograficzna Kotwica**: Każde zapytanie musi posiadać hash SHA-256.
3. **Controlled Generation**: Wymuszamy JSON Schema, aby uniemożliwić wstrzyknięcie złośliwego kodu przez pośrednika.