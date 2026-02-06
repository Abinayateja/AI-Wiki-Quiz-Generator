import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):

    res=requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
    soup=BeautifulSoup(res.text,"html.parser")

    title_tag=soup.find("h1")
    title=title_tag.get_text() if title_tag else "No Title"

    content=soup.find("div",{"id":"mw-content-text"})

    paragraphs=content.find_all("p") if content else []

    text=" ".join(p.get_text() for p in paragraphs if p.get_text().strip())

    sections = [
    h.get_text().replace("[edit]","").strip()
    for h in content.find_all("h2")
] if content else []

    return title,text,sections,res.text
    
