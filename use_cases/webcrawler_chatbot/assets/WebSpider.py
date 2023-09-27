import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import WebsiteItem
from bs4 import BeautifulSoup


def replace_multiple_newlines(txt):
    txt = "\n".join([ x.strip() for x in txt.split("\n")])
    while '\n\n' in txt:
        txt = txt.replace("\n\n", "\n")
    return txt
    
class WebSpider(scrapy.Spider):
    name = "website"
   
    import os
    if 'CRAWL_DOMAINS' in os.environ:
        allowed_domains = os.environ['CRAWL_DOMAINS'].split(",")
    else:
        allowed_domains = ['twsc.twcc.ai']

    if 'CRAWL_START_URL' in os.environ:
        start_urls = os.environ['CRAWL_START_URL'].split(",")
    else:
        start_urls = ["https://twsc.twcc.ai/"]

    def parse(self, response):
        item = WebsiteItem()
        item['url'] = response.url
        item['title'] = response.xpath('//title/text()').get()
        item['body'] = replace_multiple_newlines("".join(BeautifulSoup(response.body.decode('utf-8'), "html.parser").get_text()))
        yield item
        link_extractor = LinkExtractor()
        links = link_extractor.extract_links(response)
        for link in links:
            yield scrapy.Request(link.url, callback=self.parse)
        
