import scrapy
import logging
from twisted.internet import reactor, defer

import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging, _get_handler
from scrapy.utils.project import get_project_settings


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        page = getattr(self, 'page', 1)
        yield scrapy.Request('http://quotes.toscrape.com/page/{}/'.format(page),
                             self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
