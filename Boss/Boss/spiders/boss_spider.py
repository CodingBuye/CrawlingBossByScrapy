# -*- coding: utf-8 -*-
import scrapy
from Boss.items import BossItem


class BossSpiderSpider(scrapy.Spider):
    name = 'boss_spider'  # 爬虫名称，和项目名不能重复
    allowed_domains = ['www.zhipin.com']  # 允许的域名，不在这个域名内的将不会被抓取
    start_urls = ['https://www.zhipin.com/job_detail/?ka=header-job']  # 入口的url，扔到调度器中去
    """
    调度器拿到入口url后会将其交给引擎，引擎再将url交给下载器进行数据的解析和下载，
    下载完之后返回spider文件中，用parse进行解析
    """

    # 默认解析函数
    def parse(self, response):
        job_list = response.xpath("//div[@class='job-list']//ul/li")
        # 循环条目
        for job_item in job_list:
            # 数据的详细解析
            boss_item = BossItem()
            boss_item['job_name'] = job_item.xpath(".//div[@class='job-title']/text()").extract_first()
            boss_item['monthly_salary'] = job_item.xpath(".//span[@class='red']/text()").extract_first()
            boss_item['company_name'] = job_item.xpath("//div[@class='company-text']/h3[@class='name']/a/text()").extract_first()
            boss_item['company_type'] = job_item.xpath("//div[@class='company-text']/p/text()").extract()[0]
            boss_item['is_listed'] = job_item.xpath("//div[@class='company-text']/p/text()").extract()[1]
            boss_item['company_size'] = job_item.xpath("//div[@class='company-text']/p/text()").extract()[2]
            boss_item['company_addr'] = job_item.xpath("//div[@class='info-primary']/p/text()").extract()[0]
            boss_item['experience'] = job_item.xpath("//div[@class='info-primary']/p/text()").extract()[1]
            boss_item['education'] = job_item.xpath("//div[@class='info-primary']/p/text()").extract()[2]
            yield boss_item  # yield到pipelines中去
        # 解析下一页规则，取后一页，让scrapy自动翻页爬取
        next_link = response.xpath("//div[@class='page']/a[@class='next']/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://www.zhipin.com"+next_link, callback=self.parse)  # yield到调度器
