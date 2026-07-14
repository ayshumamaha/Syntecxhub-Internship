# Web Scraper for Headlines

## SyntecxHub Internship – Task 3

### Project Overview

This project is a Python-based web scraper that fetches the latest news headlines from the BBC News website. It extracts the headline titles and corresponding URLs using web scraping techniques and saves the collected information into a CSV file for future use.

The project demonstrates the use of Python libraries for HTTP requests, HTML parsing, data extraction, and CSV file handling.

---

## Features

- Fetches the latest headlines from BBC News
- Extracts headline titles
- Extracts article URLs
- Removes duplicate headlines
- Displays headlines in a readable format
- Saves results to a CSV file
- Includes basic exception handling
- Adds a small delay between displaying headlines

---

## Technologies Used

- Python 3
- Requests
- BeautifulSoup (bs4)
- CSV Module
- Time Module

---

## Project Structure

```
Web-Scraper-for-Headlines/
│
├── news_scraper.py
├── headlines.csv
└── README.md
```

---

## Installation

Install the required library:

```bash
pip install beautifulsoup4
```

---

## How to Run

Execute the Python script:

```bash
python news_scraper.py
```

For Google Colab:

1. Install BeautifulSoup.
2. Run the scraper code.
3. Download the generated `headlines.csv` file.

---

## Output

The program:

- Connects to BBC News
- Fetches the latest headlines
- Displays headline titles
- Displays article URLs
- Saves all results into **headlines.csv**

---

## Sample Output

```
BBC NEWS HEADLINE SCRAPER

Connecting to BBC News...

1. Headline Title
https://www.bbc.com/news/...

2. Headline Title
https://www.bbc.com/news/...

...

Total Headlines Found : 25

CSV File Saved : headlines.csv
```

---

## Learning Outcomes

- Web Scraping using Requests
- HTML Parsing using BeautifulSoup
- Data Extraction
- CSV File Handling
- Exception Handling
- Python Automation

---

## Author

**M. Ayshwarya**

SyntecxHub Internship – Python Development
