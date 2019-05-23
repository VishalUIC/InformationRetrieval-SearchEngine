import queue
import requests
import regex as re
from bs4 import BeautifulSoup
import json
import threading


web_pages = {}


def crawl(url):
    try:
        page = requests.get(url).content.decode("utf-8")
        xml_pattern = re.compile("<.[^(><.)]+>")
        soup = BeautifulSoup(page, 'html.parser')
        content = ""
        for strong_tag in soup.find_all('span'):
            content += " " + strong_tag.text
        for strong_tag in soup.find_all('h'):
            content += " " + strong_tag.text
        for strong_tag in soup.find_all('p'):
            content += " " + strong_tag.text


        web_pages[url] = {}
        web_pages[url]['content'] = content
        return page
    except Exception as e:
        return ""


def extract_urls(url, page):
    urls = []
    if page != "" and len(page) > 0:
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find_all("a"):
            link = link.get("href")
            if link is not None and "uic.edu" in link:
                urls.append(link)
        web_pages[url]['links'] = list(set(urls))
        print("Crawled {0}/3000".format(len(web_pages)))
        return list(set(urls))
    return []


def main():
    while len(web_pages) < 3000:
        current_url = url_queue.get()
        webPage = crawl(current_url)
        for next_url in extract_urls(current_url, webPage):
            if next_url not in seen:
                seen.add(next_url)
                url_queue.put(next_url)


try:
    initial_page = "http://www.cs.uic.edu"
    url_queue = queue.Queue()
    seen = set()
    seen.add(initial_page)
    url_queue.put(initial_page)

    threads = []

    for _ in range(20):
        process = threading.Thread(target=main, args=[])
        process.start()
        threads.append(process)

    for process in threads:
        process.join()

except KeyboardInterrupt as e:
    pass
with open('webpagesdump.json', 'w') as dump:
    json.dump(web_pages, dump)
print("Crawler job is executed successfully and scraped {0} document. Run the search engine now".format(len(web_pages)))
