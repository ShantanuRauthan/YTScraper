# YTScraper

A Selenium-based YouTube scraper that searches for videos by keyword and extracts metadata — URLs, titles, view counts, and duration.

## Features

- Searches YouTube by keyword
- Extracts video URL, title, views, and duration for each result
- Saves results to a text file
- Headless browser automation

## Installation

```bash
git clone https://github.com/ShantanuRauthan/YTScraper.git
cd YTScraper
pip install selenium
```

Requires [ChromeDriver](https://chromedriver.chromium.org/) installed and available in PATH.

## Usage

```bash
python3 ytscraper.py <search-keyword>
```

Results are saved to a text file in the current directory.

## Technologies

- Python
- Selenium WebDriver
- ChromeDriver

