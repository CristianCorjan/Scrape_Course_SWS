import time
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re

# List of IDs (copy your extracted id_list here)
id_list = []  # <-- Paste your ID list here

# Target website
target_site = "campus.tum.de"

# Delay settings (to avoid getting blocked)
SEARCH_DELAY = 3
SCRAPE_DELAY = 2

# User-Agent string (compatible with Chrome, Firefox)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Function to search Google for the correct page
def google_search(id_number):
    query = f"site:{target_site} {id_number}"
    print(f"\033[1;34m[SEARCH]\033[0m Looking for: {id_number}")

    try:
        search_results = search(query)
        for url in search_results:
            if url.startswith("http"):  # Ensure valid URL
                print(f"\033[1;32m[FOUND]\033[0m {url}")
                return url
        print(f"\033[1;31m[NOT FOUND]\033[0m No results for {id_number}")
        return None
    except Exception as e:
        print(f"\033[1;31m[ERROR]\033[0m Google search failed: {e}")
        return None

# Function to extract "SWS" (Semesterwochenstunden) using regex
def extract_sws(tbody_list):
    for tbody in tbody_list:
        rows = tbody.find_all("tr")

        for row in rows:
            cells = row.find_all("td")
            cell_texts = [cell.get_text(strip=True) for cell in cells]

            # Search for "SWS" with [nach SPOV]
            for text in cell_texts:
                match = re.search(r"(\d+)\[nach SPOV\]", text)
                if match:
                    return match.group(1)

    return None  # Return None instead of printing errors

# Function to scrape the exam type & SWS
def scrape_page(url):
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            return f"\033[1;31m[ERROR]\033[0m HTTP {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")
        page_text = soup.get_text().lower()

        # Extract all tbody elements
        all_tbody = soup.find_all("tbody")

        # Check for "Written Exam" or "Schriftliche Klausur"
        exam_label = "Exam" if ("written exam" in page_text or "schriftliche klausur" in page_text) else "No Exam"

        # Extract "SWS" (Semesterwochenstunden) value from table
        sws = extract_sws(all_tbody)

        # If SWS is not found, mark it as "MANUALLY"
        if sws is None:
            return f"{exam_label} | \033[1;31mMANUALLY\033[0m"
        else:
            return f"{exam_label} | SWS: {sws}"

    except Exception as e:
        return f"\033[1;31m[ERROR]\033[0m {e}"

# Main script
if __name__ == "__main__":
    print("\033[1;36m[STARTING SCRAPER]\033[0m")
    print("=" * 50)

    for id_number in id_list:
        url = google_search(id_number)
        if url:
            time.sleep(SCRAPE_DELAY)
            result = scrape_page(url)
            print(f"\033[1;33m[{id_number}]\033[0m {result}")
        else:
            print(f"\033[1;31m[{id_number}]\033[0m No result found.")

    print("\n\033[1;36m[SCRAPING COMPLETE]\033[0m")

