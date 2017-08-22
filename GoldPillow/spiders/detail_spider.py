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
                    # self.settings.['DEFAULT_REQUEST_HEADERS']['Referer'] = temp_dic['url']
                    print(self.settings.attributes['DEFAULT_REQUEST_HEADERS'])
                    yield scrapy.Request(temp_dic['url'], callback=self.parse)

    def parse(self, response):
        print(response.xpath('//strong[@class="profile_nickname"]/text()').extract_first().strip())
        yield {
            'name': response.xpath('//strong[@class="profile_nickname"]/text()').extract_first().strip(),
            'description': response.xpath('//div[@class="profile_desc_value"]/text()').extract()[0],
            'company': response.xpath('//div[@class="profile_desc_value"]/text()').extract()[1],
        }
# response.xpath('//div[@class="content"]/p/text()').extract()

# <strong class="profile_nickname">
#                       上海国际自然保护周
#                     </strong>
