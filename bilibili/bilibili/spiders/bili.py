# -*- coding: utf-8 -*-
import scrapy
from ..items import BilibiliItem
import json
import time

# class BiliSpider(scrapy.Spider):
#     name = 'bili'
#     allowed_domains = ['bilibili.com']
#     start_urls = ['https://www.bilibili.com/video/av68180250/']
#
#
#     def parse(self, response):
#         ranks = response.xpath('//li[@class="rank-item"]')
#         for rank in ranks:
#             num = rank.xpath('.//div[@class="num"]/text()').get().strip()
#             title = rank.xpath('.//a[@class="title"]/text()').get().strip()
#             item = dict(num=num,title=title)
#             yield item
#         next_url = response.
#         if not next_url:
#             return
#         else:
#             yield scrapy.Request(next_url, callable=self.parse)
class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['bilibili.com']
    # start_urls = ['http://api.bilibili.com/archive_stat/stat?aid=0']
    totle_urls = "http://api.bilibili.com/archive_stat/stat?aid="
    # test_urls = ['http://httpbin.org/user-agent']

    custom_settings = {
        'ITEM_PIPELINES' : {
            #'bilibili.pipelines.BilibiliPipeline': 300,
            'bilibili.pipelines.DBPipeline': 300
        }
    }

    def start_requests(self):
        for i in range(10):
            next_url = str(i)
            yield scrapy.Request(self.totle_urls + next_url, callback=self.parse , meta={'download_timeout': 5})

    def parse(self, response):
        # if response.text == 0:
        #     aid = json.loads(response.text)['data']['aid']
        #     view = json.loads(response.text)['data']['view']
        #     danmaku = json.loads(response.text)['data']['danmaku']
        #     reply = json.loads(response.text)['data']['reply']
        #     favorite = json.loads(response.text)['data']['favorite']
        #     coin = json.loads(response.text)['data']['coin']
        #     share = json.loads(response.text)['data']['share']
        #     # now_rank = json.loads(response.text)['data']['now_rank']
        #     his_rank = json.loads(response.text)['data']['his_rank']
        #     like = json.loads(response.text)['data']['like']
        #     # dislike = json.loads(response.text)['data']['dislike']
        #     # no_reprint = json.loads(response.text)['data']['no_reprint']
        #     # copyright = json.loads(response.text)['data']['copyright']
        #     item = {"aid":aid,"view":view,"danmaku":danmaku,"reply":reply,"favorite":favorite,"coin":coin,"share":share,
        #     "his_rank":his_rank,"like":like}
        #     #"now_rank":now_rank,,"dislike":dislike,"no_reprint":no_reprint,"copyright":copyright
        #     yield item
        #
        if response.status != 200:
            time.sleep(300)
            yield scrapy.Request(response.url, callback = self.parse, dont_filter = True)
        else:
            try:
                if json.loads(response.text)['code'] == 0:
                    aid = json.loads(response.text)['data']['aid']
                    view = json.loads(response.text)['data']['view']
                    danmaku = json.loads(response.text)['data']['danmaku']
                    reply = json.loads(response.text)['data']['reply']
                    favorite = json.loads(response.text)['data']['favorite']
                    coin = json.loads(response.text)['data']['coin']
                    share = json.loads(response.text)['data']['share']
                    # now_rank = json.loads(response.text)['data']['now_rank']
                    his_rank = json.loads(response.text)['data']['his_rank']
                    like = json.loads(response.text)['data']['like']
                    # dislike = json.loads(response.text)['data']['dislike']
                    # no_reprint = json.loads(response.text)['data']['no_reprint']
                    # copyright = json.loads(response.text)['data']['copyright']
                    item = {"aid":aid,"view":view,"danmaku":danmaku,"reply":reply,"favorite":favorite,"coin":coin,"share":share,
                    "his_rank":his_rank,"like":like}
                    #"now_rank":now_rank,,"dislike":dislike,"no_reprint":no_reprint,"copyright":copyright
                    yield item
            except:
                yield scrapy.Request(response.url, callback=self.parse , meta={'download_timeout': 5}, dont_filter = True)


        # for i in range(5):
        #
        #     yield scrapy.Request(self.test_urls, dont_filter = True)
        #     user_agent = json.loads(response.text)['user-agent']
        #     print(user_agent)
