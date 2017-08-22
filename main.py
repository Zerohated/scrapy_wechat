from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging, _get_handler
from scrapy.utils.project import get_project_settings
from GoldPillow.spiders.account_spider import AccountSpider
from GoldPillow.spiders.detail_spider import DetailSpider
from xpinyin import Pinyin
import random
import distinct
import logging


P = Pinyin()
# define output_filename and tag
# TAG_LIST = ["拼团", "拼单", "秒杀", "团购", "敏感肌", "生活方式", "日本", "韩国"]
TAG_LIST = ['宠物+团购', '宠物', '猫狗', '掉毛']
FILE_LIST = []
for each in TAG_LIST:
    FILE_LIST.append("temp/%s.csv" % P.get_pinyin(each))
print(FILE_LIST)


# <crwaling accounts START>
@defer.inlineCallbacks
def crawl():
    s = get_project_settings()
    for tag in TAG_LIST:
        tag_pinyin = P.get_pinyin(tag)
        print("<crwaling accounts...>")
        print("<crwaling %s.." % tag_pinyin)
        s.update({
            'FEED_URI': 'temp/%s.csv' % tag_pinyin,
            'FEED_FORMAT': 'csv',
            # 'FEED_EXPORTERS': 'CsvItemExporter',
            'LOG_FILE': 'log/%s.log' % tag_pinyin
        })
        # print("Waiting for crawling of keyword: %s ..." % tag_name)
        # manually configure logging for LOG_FILE
        configure_logging(settings=s, install_root_handler=False)
        logging.root.setLevel(logging.NOTSET)
        handler = _get_handler(s)
        logging.root.addHandler(handler)
        runner = CrawlerRunner(s)
        yield runner.crawl(AccountSpider, tag=tag)
        # # reset root handler
        logging.root.removeHandler(handler)
        print("<crwaling %s ended!.." % tag_pinyin)
    # distinct the records in output_files
    print("Loading from distinct account list ...")
    t = distinct.main(FILE_LIST)
    print("Distincted succeed")
    # print("<crwaling detail START...>")
    # s = get_project_settings()
    # s.update({
    #     'FEED_URI': 'account_detail.csv',
    #     'LOG_FILE': 'log/detail.log'
    # })
    # # manually configure logging for LOG_FILE
    # configure_logging(settings=s, install_root_handler=False)
    # logging.root.setLevel(logging.NOTSET)
    # handler = _get_handler(s)
    # logging.root.addHandler(handler)
    # runner = CrawlerRunner(s)
    # yield runner.crawl(DetailSpider)
    # # reset root handler
    # logging.root.removeHandler(handler)
    # print("<crwaling detail END...>")
    reactor.stop()


crawl()
reactor.run()
