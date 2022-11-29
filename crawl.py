import requests
from bs4 import BeautifulSoup

def news_crawler():
    base = "https://news.cnyes.com"
    url  = "https://news.cnyes.com/news/cat/headline"
    re   = requests.get(url)

    content = ""

    soup = BeautifulSoup(re.text, "html.parser")
    data = soup.find_all("a", {"class": "_1Zdp"})
    
    for index, d in enumerate(data):
        if index <8:
            title = d.text
            href  = base + d.get("href")
            content += "{}\n{}\n\n".format(title, href)
        else:
            break
        
    return content


def weekly_news():
    base_1 = "https://www.businessweekly.com.tw"
    url_1  = "https://www.businessweekly.com.tw/channel/insight/0000000320"
    re   = requests.get(url_1)

    content = ""


    soup = BeautifulSoup(re.text, "html.parser")
    data = soup.find_all("div", {"Article-content d-xs-flex"})



    for index, d in enumerate(data):
        if index <8:
            title = d.text.strip()
            # href  = base_1 + d.get("href")
            href  = base_1 + str(d.find('a')['href'])

            content +=  title + '\n' +href +'\n\n'


        else:
            break
    return content