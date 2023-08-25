import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import TwscWebsiteItem
from bs4 import BeautifulSoup


def replace_multiple_newlines(txt):
    txt = "\n".join([ x.strip() for x in txt.split("\n")])
    while '\n\n' in txt:
        txt = txt.replace("\n\n", "\n")
    return txt
    
class WebSpider(scrapy.Spider):
    name = "website"
    
    start_urls = [
        "https://tws.twcc.ai/",
    ]
    allowed_domains = ['tws.twcc.ai', 'twsc.twcc.ai']
    def parse(self, response):
        item = TwscWebsiteItem()
        item['url'] = response.url
        item['title'] = response.xpath('//title/text()').get()
        item['body'] = replace_multiple_newlines("".join(BeautifulSoup(response.body.decode('utf-8'), "html.parser").get_text()))
        yield item
        link_extractor = LinkExtractor()
        links = link_extractor.extract_links(response)
        for link in links:
            yield scrapy.Request(link.url, callback=self.parse)
        
