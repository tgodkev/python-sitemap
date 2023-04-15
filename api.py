from fastapi import FastAPI
from typing import List
from main import crawl_website

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sitemap")
def get_sitemap() -> List[str]:
    base_url = "https://kevinknight.io"  # Replace with your website URL
    all_urls = crawl_website(base_url)
    return list(all_urls)
