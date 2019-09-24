# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
import time
import json
from scrapy.http import Request

class BiliSpider(RedisSpider):
    name = 'bili'
    allowed_domains = ['bilibili.com']
    redis_key = "bili:start_urls"
    totle_urls = "http://api.bilibili.com/archive_stat/stat?aid="

    custom_settings = {
        'ITEM_PIPELINES': {
            # 'bilibili.pipelines.BilibiliPipeline': 300,
            'bilibili.pipelines.DBPipeline': 300,
            'scrapy_redis.pipelines.RedisPipeline': 100,
        }
    }
    def start_requests(self):
        for i in range(100):
            next_url = str(i)
            yield Request(self.totle_urls + next_url, callback=self.parse, meta={'download_timeout': 5},dont_filter=True)

    def parse(self, response):
        if response.status != 200:
            time.sleep(300)
            yield Request(response.url, callback=self.parse, dont_filter=True)
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
                    item = {"aid": aid, "view": view, "danmaku": danmaku, "reply": reply, "favorite": favorite,
                            "coin": coin, "share": share,
                            "his_rank": his_rank, "like": like}
                    # "now_rank":now_rank,,"dislike":dislike,"no_reprint":no_reprint,"copyright":copyright
                    yield item
            except:
                yield Request(response.url, callback=self.parse, meta={'download_timeout': 5}, dont_filter=True)

