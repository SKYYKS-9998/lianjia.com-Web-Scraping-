from scrapy import cmdline

# 同时只能爬一个，其他的暂时变为注释
cmdline.execute("scrapy crawl rent_beijing".split())
# cmdline.execute("scrapy crawl rent_shanghai".split())
# cmdline.execute("scrapy crawl rent_guangzhou".split())
# cmdline.execute("scrapy crawl rent_shenzhen".split())
# cmdline.execute("scrapy crawl rent_quanzhou".split())

