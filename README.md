# News Headlines Scraper

A simple Python script that fetches headlines from BBC News and saves them to a local text file.

## Features
- Downloads the BBC News homepage HTML
- Extracts visible headings such as h1, h2, and h3 tags
- Removes duplicate headlines while preserving order
- Saves the results to `headlines.txt`

## Requirements
Install the dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage
Run the script:

```bash
python news_headlines_scraper.py
```

The script will create a file named `headlines.txt` in the project folder containing the scraped headlines.

## Notes
- The script depends on the structure of the target website and may need updates if the site changes.
- Make sure you have an active internet connection when running it.
