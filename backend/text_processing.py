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


def normalize_text(text: str) -> str:
    #Normalize Unicode and convert text to lowercase
    text = unicodedata.normalize("NFKC", text)
    return text.casefold()


def tokenize(text: str) -> list[str]:
    #Extract sequences of letters and digits as tokens
    normalized = normalize_text(text)
    return re.findall(r"\w+", normalized, flags=re.UNICODE)

