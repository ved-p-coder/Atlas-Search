from fastapi.testclient import TestClient

# Used to build file paths reliably across different working directories
from pathlib import Path

from backend.main import app

from backend.text_processing import extract_text, normalize_text, tokenize

client = TestClient(app)


def test_health_check():
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "application": "Atlas Search",
    }

def test_extract_text_from_html():
    html = """
    <html>
        <head><title>Search</title></head>
        <body>
            <h1>Python Search</h1>
            <p>Build an engine.</p>
            <script>secret_script()</script>
        </body>
    </html>
    """

    text = extract_text(html)

    assert "Python Search" in text
    assert "Build an engine." in text
    assert "secret_script()" not in text
