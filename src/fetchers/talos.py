import requests
from bs4 import BeautifulSoup

def fetch_talos_latest_blog_text():
    url = "https://blog.talosintelligence.com"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Get the first article link
        article = soup.find("article")
        if not article:
            return None
        link = article.find("a")["href"]
        article_url = link if link.startswith("http") else url + link
        article_resp = requests.get(article_url, timeout=10)
        article_soup = BeautifulSoup(article_resp.text, "html.parser")
        return "\n".join(p.get_text() for p in article_soup.find_all("p"))
    except Exception as e:
        print(f" Talos fetch failed: {e}")
        return None
