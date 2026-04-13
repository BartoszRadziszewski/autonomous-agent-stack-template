import pytest

def test_no_proxy_rule():
    """Sprawdza czy w kodzie nie ma zakazanych routerów API."""
    forbidden = ["openrouter.ai", "helicone.ai", "proxy"]
    with open("main.py", "r") as f:
        content = f.read()
        for word in forbidden:
            assert word not in content, f"❌ Wykryto zakazany endpoint: {word}"

def test_manifest_existence():
    import os
    assert os.path.exists("ANTI_GRAVITY_SECURITY_MANIFEST.md")