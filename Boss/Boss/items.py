# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()        # 职位名称
    monthly_salary = scrapy.Field()  # 月薪
    company_name = scrapy.Field()    # 公司名称
    company_addr = scrapy.Field()    # 公司地址
    company_type = scrapy.Field()    # 公司类型
    company_size = scrapy.Field()    # 公司规模
    is_listed = scrapy.Field()       # 是否上市
    experience = scrapy.Field()      # 工作经验
    education = scrapy.Field()       # 学历


