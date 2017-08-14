from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging
from GoldPillow.spiders.example import *
from xpinyin import Pinyin
import distinct

P = Pinyin()
# define output_filename and tag
TAG_LIST = ["拼团", "拼单", "秒杀", "团购", "敏感肌", "生活方式", "日本", "韩国"]
file_list = []
TO_CRAWL = ['humor', 'love']
# 'followall' is the name of one of the spiders of the project.
# for spider in range(2):
settings = Settings()
settings.set("USER_AGENT", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36")
settings.set("FEED_FORMAT", 'csv')
settings.set("FEED_URI", 'test.csv')
# settings.set("ITEM_PIPELINES",{ 'pipelines.CustomPipeline': 300})
# settings.set("DOWNLOAD_DELAY", 1)
crawler = CrawlerProcess(settings)
crawler.crawl(HumorSpider)
crawler.start()
crawler.crawl(LoveSpider)
crawler.start()
reactor.run()

# execute the scrapy
# for tag_name in TAG_LIST:
#     output_filename = "%s.csv" % P.get_pinyin(tag_name)
#     file_list.append(output_filename)
#     cmdline.execute(("scrapy crawl account -o %s -a tag='%s'" %
#                     (output_filename, tag_name)).split())
#     print("Waiting for crawling of keyword: %s ..." % tag_name)
# print("Crawling finished, keywords number: %i" % len(TAG_LIST))

# distinct the records in output_files
# account_dic is a dic `key = account name` and `value = account url`
# distinct.main(filename_list)
# print("Loading from distinct account list ...")
# cmdline.execute(("scrapy crawl detail -o 'output.csv'").split())
