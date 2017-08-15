import scrapy
from urllib import parse
import json


class DetailSpider(scrapy.Spider):
    name = "detail"

    def start_requests(self):
        with open('distinct-accounts.csv', 'r', encoding='utf-8', newline='\n') as da:
            content = da.readlines()
            url_list = []
            for row in content:
                temp_dic = json.loads(row)
                yield scrapy.Request(temp_dic['url'], callback=self.parse)

    def parse(self, response):
        yield {
            'name': response.xpath('//strong[@class="profile_nickname"]/text()').extract_first().strip(),
            'description': response.xpath('//div[@class="profile_desc_value"]/text()').extract()[0],
            'company': response.xpath('//div[@class="profile_desc_value"]/text()').extract()[1],
        }


# <strong class="profile_nickname">
#                       上海国际自然保护周
#                     </strong>
