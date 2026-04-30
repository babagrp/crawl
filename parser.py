from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "https://www.lnmu.ac.in"

def extract_links(html):
    soup = BeautifulSoup(html, "lxml")
    links = []

    for a in soup.select("a"):
        href = a.get("href")
        text = a.get_text(strip=True)

        if href and "faculty" in href.lower():
            links.append({
                "name": text,
                "url": urljoin(BASE, href)
            })

    return links


def extract_data(html, faculty_name, source):
    soup = BeautifulSoup(html, "lxml")
    results = []

    for row in soup.select("tr"):
        cols = [c.get_text(strip=True) for c in row.select("td")]

        if len(cols) >= 2:
            results.append({
                "name": cols[0],
                "designation": cols[1],
                "faculty": faculty_name,
                "source": source
            })

    return results
