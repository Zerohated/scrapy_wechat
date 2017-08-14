
from urllib import parse


name = "account"
keyword = '团购'
keyword_url = parse.quote(keyword)
print(keyword_url)
