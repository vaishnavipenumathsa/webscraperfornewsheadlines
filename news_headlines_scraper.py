import requests
from bs4 import BeautifulSoup

OUTPUT_FILE = "headlines.txt"
NEWS_URL = "https://www.bbc.com/news"


def fetch_html(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def extract_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    headlines = []

    # Common headline tags on news sites
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text:
            headlines.append(text)

    # Keep unique values preserving order
    seen = set()
    unique_headlines = []
    for headline in headlines:
        if headline not in seen:
            seen.add(headline)
            unique_headlines.append(headline)

    return unique_headlines


def save_headlines(headlines, path):
    with open(path, "w", encoding="utf-8") as f:
        for headline in headlines:
            f.write(headline + "\n")


if __name__ == "__main__":
    print(f"Fetching headlines from: {NEWS_URL}")
    html = fetch_html(NEWS_URL)
    headlines = extract_headlines(html)

    if not headlines:
        print("No headlines found. Check the page structure or the target URL.")
    else:
        save_headlines(headlines, OUTPUT_FILE)
        print(f"Saved {len(headlines)} headlines to {OUTPUT_FILE}")
