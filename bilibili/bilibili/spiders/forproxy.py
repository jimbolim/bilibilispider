# -*- coding: utf-8 -*-
import scrapy
import requests

class ForproxySpider(scrapy.Spider):
    name = 'forproxy'
    allowed_domains = ['xicidaili.com/nn']
    # start_urls = ['https://www.xicidaili.com/nn']
    totle_url = 'https://www.xicidaili.com/nn/'
    custom_settings = {
        'ITEM_PIPELINES': {
            'bilibili.pipelines.ForproxyPipeline': 300
        }
    }

    def start_requests(self):
        for i in range(1,10):

            yield scrapy.Request(self.totle_url+str(i),self.parse)

    def parse(self, response):
        proxys = response.xpath('//tr')
        for proxy in proxys[1:]:
            mid = proxy.xpath('.//td')
            ip = mid[1].get()[4:-5]
            port = mid[2].get()[4:-5]
            item = 'http://' + ip + ':' + port
            try:
                requests.get('http://www.baidu.com',proxies={'http' : item}, timeout=1)
            except:
                print(item+'connect failed')
            else:
                res = {'success' : item}
                yield res
                print(item+'success')



            # if mid[5].get() == '<td>HTTPS</td>':
            #     item = 'https://'+ ip + ':' + port
            #     yield item
            # if mid[5].get() == '<td>HTTPS</td>':
            #     print(mid[1].get()+mid[2].get())
