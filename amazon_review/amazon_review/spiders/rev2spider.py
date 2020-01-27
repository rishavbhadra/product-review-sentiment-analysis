# -*- coding: utf-8 -*-
import scrapy


class Rev2spiderSpider(scrapy.Spider):
    name = 'rev2spider'
    allowed_domains = ['https://www.amazon.in/Samsung-Sapphire-Display-Storage-6000mAH/product-reviews/B07HGMQX6N/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8']
    start_urls = ['http://https://www.amazon.in/Samsung-Sapphire-Display-Storage-6000mAH/product-reviews/B07HGMQX6N/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8/']

    def parse(self, response):
        pass
