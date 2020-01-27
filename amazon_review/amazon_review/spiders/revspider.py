# -*- coding: utf-8 -*-
import scrapy


class RevspiderSpider(scrapy.Spider):
    name = 'revspider'
    allowed_domains = ['amazon.in']
    myBaseUrl = "https://www.amazon.in/Samsung-Sapphire-Display-Storage-6000mAH/product-reviews/B07HGMQX6N/ref=cm_cr_getr_d_paging_btm_next_5?ie=UTF8&reviewerType=all_reviews&pageNumber="
    start_urls=[]
    for i in range(1,20):
        start_urls.append(myBaseUrl+str(i))

    def parse(self, response):
        reviews = response.xpath('//span[@data-hook="review-body"]/span/text()').extract()
        for (review) in zip(reviews):
            yield {'Review': review}
