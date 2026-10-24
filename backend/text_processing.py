import re
import unicodedata

from bs4 import BeautifulSoup


def extract_text(html: str) -> str:
    #Extract readable text from an HTML document
    soup = BeautifulSoup(html, "html.parser")

    # Remove content that should not be indexed as page text.
    for element in soup(["script", "style", "noscript"]):
        element.decompose()

    return soup.get_text(separator=" ", strip=True)
