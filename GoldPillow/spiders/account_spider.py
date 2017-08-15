import scrapy
from urllib import parse


class AccountSpider(scrapy.Spider):
    name = "account"
    # keyword = '团购'
    # keyword_url = parse.quote(keyword)
    # start_urls = [
    #     'http://weixin.sogou.com/weixin?query=%s&_sug_type_=&s_from=input&_sug_=n&type=2&ie=utf8&page=1' % keyword_url,
    # ]

    def start_requests(self):
        keyword = getattr(self, 'tag', 'None')
        keyword_url = parse.quote(keyword)
        if keyword_url is not None:
            url = ('http://weixin.sogou.com/weixin?query=%s&_sug_type_=&s_from=input&_sug_=n&type=2&ie=utf8&page=1' % keyword_url)
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for account in response.xpath('//ul[@class="news-list"]/li/div/div/a[@class="account"]'):
            yield {
                'name': account.xpath('text()').extract_first(),
                'url': account.xpath('@href').extract_first(),
            }
        next_page = response.xpath('//a[@id="sogou_next"]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)
