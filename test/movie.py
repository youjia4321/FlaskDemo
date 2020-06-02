import requests
from lxml import etree
import random

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}


def ran(c, d):
    a = random.uniform(c, d)
    C = 1
    return round(a, C)


def get_page(url):
    resp = requests.get(url, headers=headers)
    return resp.text


def parse_html(page):
    resp = etree.HTML(page)
    dds = resp.xpath("//dl[@class='board-wrapper']//dd")
    _info = []
    for dd in dds:
        url = "https://maoyan.com"+dd.xpath("./a/@href")[0]
        _type, director = parse_detail(url)
        dd_info = {
            'mname': dd.xpath("./a/@title")[0],
            'mscore': ''.join(dd.xpath('.//div[@class="movie-item-number score-num"]//p//text()')),
            # 'score': ran(7, 10),
            'mactor': ''.join(dd.xpath(".//div[@class='movie-item-info']//p[@class='star"
                             "']/text()")[0].replace('\n', '').strip().split("：")[1]),
            'mprice': ran(30, 100),
            'mtype': _type,
            'mdirector': director
        }
        _info.append(dd_info)
    return _info


def parse_detail(url):
    resp = requests.get(url, headers=headers)
    _html = etree.HTML(resp.text)
    _type = "/".join([item.strip() for item in _html.xpath("//div[@class='movie-brief-container']/ul/li/a/text()")])
    director = _html.xpath('/html/body/div[4]/div/div[1]/div/div[3]/div[1]/di'
                           'v[2]/div[2]/div/div[1]/ul/li/div/a/text()')[0].replace('\n', '').strip()
    return _type, director


if __name__ == "__main__":
    for i in range(7, 10):
        html = get_page("https://maoyan.com/board/4?offset={}".format(i*10))
        info = parse_html(html)
        for item in info:
            print(item)
