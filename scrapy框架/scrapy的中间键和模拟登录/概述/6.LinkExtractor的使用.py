from scrapy.linkextractors import LinkExtractor

url = "/political/politics/index?id=463520"

le = LinkExtractor(allow=r'Items/')  # allow后面的是正则表达式

# le.extract_links(response=)

