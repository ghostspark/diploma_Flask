import requests as r
import re
from lxml import etree
import pandas as pd


def dd_sc(name, a, b, c):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    url = "http://search.dangdang.com/?key={}&act=input&sort_type=sort_sale_amt_desc".format(name)
    t = r.request('GET', 'https://www.baidu.com')
    cookies = t.cookies
    x = r.request('get', url=url, headers=headers, cookies=cookies)
    ht = etree.HTML(x.text)
    it = []
    for k in range(5):
        it.append({})
        path = "//li[@class='line{}']".format(k + 1)
        # it[k]['id'] = k
        try:
            it[k]['name'] = ht.xpath(path + "/a/@title")
        except:
            it[k]['name'] = '/'
        try:
            it[k]['price'] = \
                re.split("¥", ht.xpath(path + "//p[@class='price']/span[@class='search_now_price']")[0].text)[1]
        except:
            it[k]['price'] = "/"
        try:
            it[k]['brand'] = ht.xpath(path + "/p[@class='search_book_author']/span[3]/a")[0].text
        except:
            it['brand'] = "/"
        it[k]['volume'] = str(k+1)
        try:
            it[k]['discuss'] = re.split("条", ht.xpath(path + "/p[@class='search_star_line']/a")[0].text)[0]
        except:
            it[k]['discuss'] = "/"
        it[k]['url'] = ht.xpath(path + '/p/a/@href')[0]
        try:
            it[k]['good_discuss'] = re.split(":", ht.xpath(path + "/p[@class='search_star_line']/span/span/@style")[0])[
                1]
        except:
            it[k]['good_discuss'] = '/'
        it[k]['score'] = round((float(it[k]['price']) * float(a) + float(it[k]['volume'])) * float(b)+(100000/float(
            it[k]['discuss'])) * float(c), 2)
        it[k]['type'] = '当当'
    dd_data_f = pd.DataFrame(it)
    return dd_data_f

# fin = dd_sc("五年高考三年模拟数学")
# print(fin)