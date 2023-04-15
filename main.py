import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_urls(base_url, url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    urls = set()

    domain = urlparse(base_url).netloc
    for link in soup.find_all("a"):
        href = link.get("href")

        if href:
            full_url = urljoin(base_url, href)
            if urlparse(full_url).netloc == domain:
                urls.add(full_url)

    return urls

def crawl_website(base_url, max_depth=3):
    visited = set()
    to_visit = [(base_url, 0)]

    while to_visit:
        url, depth = to_visit.pop(0)

        if depth > max_depth:
            continue

        if url not in visited:
            visited.add(url)

            try:
                urls = get_urls(base_url, url)
                for new_url in urls:
                    to_visit.append((new_url, depth + 1))
            except Exception as e:
                print(f"Error fetching URL {url}: {e}")

    return visited

base_url = "https://kevinknight.io"  # Replace with your website URL
all_urls = crawl_website(base_url)
print(all_urls)
