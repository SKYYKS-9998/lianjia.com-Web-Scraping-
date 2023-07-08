import scrapy

from test1.items import Myitem

class Beijingspider(scrapy.spiders.Spider):
    name = "rent_beijing"                           # 爬虫名称
    allowed_domain = ["bj.lianjia.com/"]            # 允许域名
    start_urls = ["https://bj.lianjia.com/zufang/"] # 起始URL
    first_half = "https://bj.lianjia.com"           # 用于之后的拼接
    block_visited = []                              # 已访问的板块

    # 爬取一个板块的数据
    def parse_block(self, response):
        for each in response.xpath("//*[@id='content']/div[1]/div[1]/*"):
            item = Myitem()
            # 网站种的房屋数据只有两种格式有我们所需的数据
            isad = each.xpath("@data-ad_code").extract_first()
            type = each.xpath("@data-distribution_type").extract_first()
            # 租金、板块和方向可以直接爬取，面积需要将爬取的string转换为float，居数需要从爬取的“X室X厅X卫”提取室数
            if isad != "0" and type == "203500000001":
                item['rent'] = int(each.xpath("div/span/em/text()").extract_first())
                item['block'] = each.xpath("div/p[2]/a[2]/text()").extract_first()
                tmp = each.xpath("div/p[2]/text()[6]").extract_first()
                tmp_filter = filter(str.isdigit, tmp)
                tmp_list = list(tmp_filter)
                tmp_str = "".join(tmp_list)
                item['area'] = int(tmp_str) / 100
                item['direction'] = each.xpath("div/p[2]/text()[7]").extract_first().strip()
                room_tmp = each.xpath("div/p[2]/text()[8]").extract_first()
                room_filter = filter(str.isdigit, room_tmp)
                room_list = list(room_filter)
                item['room'] = int(room_list[0])
                yield item
            elif isad == "0" and type == "203500000001":
                item['rent'] = int(each.xpath("div/span/em/text()").extract_first())
                item['block'] = each.xpath("div/p[2]/a[2]/text()").extract_first()
                tmp = each.xpath("div/p[2]/text()[5]").extract_first()
                tmp_filter = filter(str.isdigit, tmp)
                tmp_list = list(tmp_filter)
                tmp_str = "".join(tmp_list)
                item['area'] = int(tmp_str) / 100
                item['direction'] = each.xpath("div/p[2]/text()[6]").extract_first().strip()
                room_tmp = each.xpath("div/p[2]/text()[7]").extract_first()
                room_filter = filter(str.isdigit, room_tmp)
                room_list = list(room_filter)
                if len(room_list) > 0:
                    item['room'] = int(room_list[0])
                yield item

        # 进行翻页
        cur_str = response.xpath("//*[@id='content']/div[1]/div[2]/@data-curpage").extract_first()
        total_str = response.xpath("//*[@id='content']/div[1]/div[2]/@data-totalpage").extract_first()
        if cur_str is not None:
            cur_page = int(cur_str)
            total_page = int(total_str)
            if cur_page < total_page:   # 未到最后一页
                next_page = response.xpath("//*[@id='content']/div[1]/div[2]/@data-url").extract_first()
                next_page = next_page[:-7]              # 移去最后的“{page}”
                next_page += str(cur_page + 1) + "/"    # 加上下一页的页数
                next_page = self.first_half + next_page # 拼接，继续爬取
                yield scrapy.Request(next_page, callback=self.parse_block, dont_filter=True)

    # 爬取一个区的数据
    def parse_district(self, response):
        for each in response.xpath("//*[@id='filter']/ul[4]/*"):    # 遍历可选的板块
            data_id = each.xpath("@data-id").extract_first()
            if data_id is None or data_id == "0":           # 板块选项的第一个是不限，跳过
                continue
            block_page = each.xpath("a/@href").extract_first()
            if self.block_visited.count(block_page) != 0:   # 已爬取过该板块，跳过
                continue
            self.block_visited.append(block_page)           # 没有爬取过该板块，标识为已爬取
            block_page = self.first_half + block_page       # 爬取板块的后半URL，拼接
            yield scrapy.Request(block_page, callback=self.parse_block, dont_filter=True)

    # 爬取该市的数据
    def parse(self, response):
        for each in response.xpath("//*[@id='filter']/ul[2]/*"):    # 在起始URL遍历可选的区
            data_id = each.xpath("@data-id").extract_first()
            if data_id == "0":  # 区选项中的第一个是“不限”，跳过
                continue
            district_page = each.xpath("a/@href").extract_first()   # 爬取区的后半URL，然后拼接
            district_page = self.first_half + district_page
            yield scrapy.Request(district_page, callback=self.parse_district, dont_filter=True)


class Shanghaispider(scrapy.spiders.Spider):
    name = "rent_shanghai"
    allowed_domain = ["sh.lianjia.com/"]
    start_urls = ["https://sh.lianjia.com/zufang/"]
    first_half = "https://sh.lianjia.com"
    block_visited = []

    def parse_block(self, response):
        for each in response.xpath("//*[@id='content']/div[1]/div[1]/*"):
            item = Myitem()
            isad = each.xpath("@data-ad_code").extract_first()
            type = each.xpath("@data-distribution_type").extract_first()
            if isad != "0" and type == "203500000001":
                item['rent'] = int(each.xpath("div/span/em/text()").extract_first())
                item['block'] = each.xpath("div/p[2]/a[2]/text()").extract_first()
                tmp = each.xpath("div/p[2]/text()[6]").extract_first()
                tmp_filter = filter(str.isdigit, tmp)
                tmp_list = list(tmp_filter)
                tmp_str = "".join(tmp_list)
                item['area'] = int(tmp_str) / 100
                item['direction'] = each.xpath("div/p[2]/text()[7]").extract_first().strip()
                room_tmp = each.xpath("div/p[2]/text()[8]").extract_first()
                room_filter = filter(str.isdigit, room_tmp)
                room_list = list(room_filter)
                item['room'] = int(room_list[0])
                yield item
            elif isad == "0" and type == "203500000001":
                item['rent'] = int(each.xpath("div/span/em/text()").extract_first())
                item['block'] = each.xpath("div/p[2]/a[2]/text()").extract_first()
                tmp = each.xpath("div/p[2]/text()[5]").extract_first()
                tmp_filter = filter(str.isdigit, tmp)
                tmp_list = list(tmp_filter)
                tmp_str = "".join(tmp_list)
                item['area'] = int(tmp_str) / 100
                item['direction'] = each.xpath("div/p[2]/text()[6]").extract_first().strip()
                room_tmp = each.xpath("div/p[2]/text()[7]").extract_first()
                room_filter = filter(str.isdigit, room_tmp)
                room_list = list(room_filter)
                if len(room_list) > 0:
                    item['room'] = int(room_list[0])
                yield item

        cur_str = response.xpath("//*[@id='content']/div[1]/div[2]/@data-curpage").extract_first()
        total_str = response.xpath("//*[@id='content']/div[1]/div[2]/@data-totalpage").extract_first()
        if cur_str is not None:
            cur_page = int(cur_str)
            total_page = int(total_str)
            if cur_page < total_page:
                next_page = response.xpath("//*[@id='content']/div[1]/div[2]/@data-url").extract_first()
                next_page = next_page[:-7]
                next_page += str(cur_page + 1) + "/"
                next_page = self.first_half + next_page
                yield scrapy.Request(next_page, callback=self.parse_block, dont_filter=True)

    def parse_district(self, response):
        for each in response.xpath("//*[@id='filter']/ul[4]/*"):
            data_id = each.xpath("@data-id").extract_first()
            if data_id is None or data_id == "0":
                continue
            block_page = each.xpath("a/@href").extract_first()
            if self.block_visited.count(block_page) != 0:
                continue
            self.block_visited.append(block_page)
            block_page = self.first_half + block_page
            yield scrapy.Request(block_page, callback=self.parse_block, dont_filter=True)

    def parse(self, response):
        for each in response.xpath("//*[@id='filter']/ul[2]/*"):
            data_id = each.xpath("@data-id").extract_first()
            if data_id == "0":
                continue
            district_page = each.xpath("a/@href").extract_first()
            district_page = self.first_half + district_page
            yield scrapy.Request(district_page, callback=self.parse_district, dont_filter=True)


class Guangzhouspider(scrapy.spiders.Spider):
    name = "rent_guangzhou"
    allowed_domain = ["gz.lianjia.com/"]
    start_urls = ["https://gz.lianjia.com/zufang/"]
    first_half = "https://gz.lianjia.com"
    block_visited = []

    def parse_block(self, response):
        for each in response.xpath("//*[@id='content']/div[1]/div[1]/*"):
            item = Myitem()
            isad = each.xpath("@data-ad_code").extract_first()
            type = each.xpath("@data-distribution_type").extract_first()
            if isad != "0" and type == "203500000001":
                item['rent'] = int(each.xpath("div/span/em/text()").extract_first())
                item['block'] = each.xpath("div/p[2]/a[2]/text()").extract_first()
                tmp = each.xpath("div/p[2]/text()[6]").extract_first()
                tmp_filter = filter(str.isdigit, tmp)
                tmp_list = list(tmp_filter)
                tmp_str = "".join(tmp_list)
                item['area'] = int(tmp_str) / 100
                item['direction'] = each.xpath("div/p[2]/text()[7]").extract_first().strip()
                room_tmp = each.xpath("div/p[2]/text()[8]").extract_first()
                room_filter = filter(str.isdigit, room_tmp)
                room_list = list(room_filter)
                item['room'] = int(room_list[0])
                yield item
            elif isad == "0" and type == "203500000001":
                item['rent'] = int(each.xpath("div/span/em/text()").extract_first())
                item['block'] = each.xpath("div/p[2]/a[2]/text()").extract_first()
                tmp = each.xpath("div/p[2]/text()[5]").extract_first()
                tmp_filter = filter(str.isdigit, tmp)
                tmp_list = list(tmp_filter)
                tmp_str = "".join(tmp_list)
                item['area'] = int(tmp_str) / 100
                item['direction'] = each.xpath("div/p[2]/text()[6]").extract_first().strip()
                room_tmp = each.xpath("div/p[2]/text()[7]").extract_first()
                room_filter = filter(str.isdigit, room_tmp)
                room_list = list(room_filter)
                if len(room_list) > 0:
                    item['room'] = int(room_list[0])
                yield item

        cur_str = response.xpath("//*[@id='content']/div[1]/div[2]/@data-curpage").extract_first()
        total_str = response.xpath("//*[@id='content']/div[1]/div[2]/@data-totalpage").extract_first()
        if cur_str is not None:
            cur_page = int(cur_str)
            total_page = int(total_str)
            if cur_page < total_page:
                next_page = response.xpath("//*[@id='content']/div[1]/div[2]/@data-url").extract_first()
                next_page = next_page[:-7]
                next_page += str(cur_page + 1) + "/"
                next_page = self.first_half + next_page
                yield scrapy.Request(next_page, callback=self.parse_block, dont_filter=True)

    def parse_district(self, response):
        for each in response.xpath("//*[@id='filter']/ul[4]/*"):
            data_id = each.xpath("@data-id").extract_first()
            if data_id is None or data_id == "0":
                continue
            block_page = each.xpath("a/@href").extract_first()
            if self.block_visited.count(block_page) != 0:
                continue
            self.block_visited.append(block_page)
            block_page = self.first_half + block_page
            yield scrapy.Request(block_page, callback=self.parse_block, dont_filter=True)

    def parse(self, response):
        for each in response.xpath("//*[@id='filter']/ul[2]/*"):
            data_id = each.xpath("@data-id").extract_first()
            if data_id == "0":
                continue
            district_page = each.xpath("a/@href").extract_first()
            district_page = self.first_half + district_page
            yield scrapy.Request(district_page, callback=self.parse_district, dont_filter=True)

class Shenzhenspider(scrapy.spiders.Spider):
    name = "rent_shenzhen"
    allowed_domain = ["sz.lianjia.com/"]
    start_urls = ["https://sz.lianjia.com/zufang/"]
    first_half = "https://sz.lianjia.com"
    block_visited = []

    def parse_block(self, response):
        for each in response.xpath("//*[@id='content']/div[1]/div[1]/*"):
            item = Myitem()
            isad = each.xpath("@data-ad_code").extract_first()
            type = each.xpath("@data-distribution_type").extract_first()
            if isad != "0" and type == "203500000001":
                item['rent'] = int(each.xpath("div/span/em/text()").extract_first())
                item['block'] = each.xpath("div/p[2]/a[2]/text()").extract_first()
                tmp = each.xpath("div/p[2]/text()[6]").extract_first()
                tmp_filter = filter(str.isdigit, tmp)
                tmp_list = list(tmp_filter)
                tmp_str = "".join(tmp_list)
                item['area'] = int(tmp_str) / 100
                item['direction'] = each.xpath("div/p[2]/text()[7]").extract_first().strip()
                room_tmp = each.xpath("div/p[2]/text()[8]").extract_first()
                room_filter = filter(str.isdigit, room_tmp)
                room_list = list(room_filter)
                item['room'] = int(room_list[0])
                yield item
            elif isad == "0" and type == "203500000001":
                item['rent'] = int(each.xpath("div/span/em/text()").extract_first())
                item['block'] = each.xpath("div/p[2]/a[2]/text()").extract_first()
                tmp = each.xpath("div/p[2]/text()[5]").extract_first()
                tmp_filter = filter(str.isdigit, tmp)
                tmp_list = list(tmp_filter)
                tmp_str = "".join(tmp_list)
                item['area'] = int(tmp_str) / 100
                item['direction'] = each.xpath("div/p[2]/text()[6]").extract_first().strip()
                room_tmp = each.xpath("div/p[2]/text()[7]").extract_first()
                room_filter = filter(str.isdigit, room_tmp)
                room_list = list(room_filter)
                if len(room_list) > 0:
                    item['room'] = int(room_list[0])
                yield item

        cur_str = response.xpath("//*[@id='content']/div[1]/div[2]/@data-curpage").extract_first()
        total_str = response.xpath("//*[@id='content']/div[1]/div[2]/@data-totalpage").extract_first()
        if cur_str is not None:
            cur_page = int(cur_str)
            total_page = int(total_str)
            if cur_page < total_page:
                next_page = response.xpath("//*[@id='content']/div[1]/div[2]/@data-url").extract_first()
                next_page = next_page[:-7]
                next_page += str(cur_page + 1) + "/"
                next_page = self.first_half + next_page
                yield scrapy.Request(next_page, callback=self.parse_block, dont_filter=True)

    def parse_district(self, response):
        for each in response.xpath("//*[@id='filter']/ul[4]/*"):
            data_id = each.xpath("@data-id").extract_first()
            if data_id is None or data_id == "0":
                continue
            block_page = each.xpath("a/@href").extract_first()
            if self.block_visited.count(block_page) != 0:
                continue
            self.block_visited.append(block_page)
            block_page = self.first_half + block_page
            yield scrapy.Request(block_page, callback=self.parse_block, dont_filter=True)

    def parse(self, response):
        for each in response.xpath("//*[@id='filter']/ul[2]/*"):
            data_id = each.xpath("@data-id").extract_first()
            if data_id == "0":
                continue
            district_page = each.xpath("a/@href").extract_first()
            district_page = self.first_half + district_page
            yield scrapy.Request(district_page, callback=self.parse_district, dont_filter=True)


class Quanzhouspider(scrapy.spiders.Spider):
    name = "rent_quanzhou"
    allowed_domain = ["quanzhou.lianjia.com/"]
    start_urls = ["https://quanzhou.lianjia.com/zufang/"]
    first_half = "https://quanzhou.lianjia.com"
    block_visited = []

    def parse_block(self, response):
        for each in response.xpath("//*[@id='content']/div[1]/div[1]/*"):
            item = Myitem()
            isad = each.xpath("@data-ad_code").extract_first()
            type = each.xpath("@data-distribution_type").extract_first()
            if isad != "0" and type == "203500000001":
                item['rent'] = int(each.xpath("div/span/em/text()").extract_first())
                item['block'] = each.xpath("div/p[2]/a[2]/text()").extract_first()
                tmp = each.xpath("div/p[2]/text()[6]").extract_first()
                tmp_filter = filter(str.isdigit, tmp)
                tmp_list = list(tmp_filter)
                tmp_str = "".join(tmp_list)
                item['area'] = int(tmp_str) / 100
                item['direction'] = each.xpath("div/p[2]/text()[7]").extract_first().strip()
                room_tmp = each.xpath("div/p[2]/text()[8]").extract_first()
                room_filter = filter(str.isdigit, room_tmp)
                room_list = list(room_filter)
                item['room'] = int(room_list[0])
                yield item
            elif isad == "0" and type == "203500000001":
                item['rent'] = int(each.xpath("div/span/em/text()").extract_first())
                item['block'] = each.xpath("div/p[2]/a[2]/text()").extract_first()
                tmp = each.xpath("div/p[2]/text()[5]").extract_first()
                tmp_filter = filter(str.isdigit, tmp)
                tmp_list = list(tmp_filter)
                tmp_str = "".join(tmp_list)
                item['area'] = int(tmp_str) / 100
                item['direction'] = each.xpath("div/p[2]/text()[6]").extract_first().strip()
                room_tmp = each.xpath("div/p[2]/text()[7]").extract_first()
                room_filter = filter(str.isdigit, room_tmp)
                room_list = list(room_filter)
                if len(room_list) > 0:
                    item['room'] = int(room_list[0])
                yield item

        cur_str = response.xpath("//*[@id='content']/div[1]/div[2]/@data-curpage").extract_first()
        total_str = response.xpath("//*[@id='content']/div[1]/div[2]/@data-totalpage").extract_first()
        if cur_str is not None:
            cur_page = int(cur_str)
            total_page = int(total_str)
            if cur_page < total_page:
                next_page = response.xpath("//*[@id='content']/div[1]/div[2]/@data-url").extract_first()
                next_page = next_page[:-7]
                next_page += str(cur_page + 1) + "/"
                next_page = self.first_half + next_page
                yield scrapy.Request(next_page, callback=self.parse_block, dont_filter=True)

    def parse_district(self, response):
        for each in response.xpath("//*[@id='filter']/ul[4]/*"):
            data_id = each.xpath("@data-id").extract_first()
            if data_id is None or data_id == "0":
                continue
            block_page = each.xpath("a/@href").extract_first()
            if self.block_visited.count(block_page) != 0:
                continue
            self.block_visited.append(block_page)
            block_page = self.first_half + block_page
            yield scrapy.Request(block_page, callback=self.parse_block, dont_filter=True)

    def parse(self, response):
        for each in response.xpath("//*[@id='filter']/ul[2]/*"):
            data_id = each.xpath("@data-id").extract_first()
            if data_id == "0":
                continue
            district_page = each.xpath("a/@href").extract_first()
            district_page = self.first_half + district_page
            yield scrapy.Request(district_page, callback=self.parse_district, dont_filter=True)