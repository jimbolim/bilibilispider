# -*- coding: utf-8 -*-
import scrapy
import json

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['httpbin.org/user-agent']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print('='*50)
        print(response.text)
        print('=' * 50)