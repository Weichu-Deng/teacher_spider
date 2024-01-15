import scrapy


# 建筑与城市规划学院

class SesSpider(scrapy.Spider):
    name = 'arch'
    allowed_domains = ['arch.gzhu.edu.cn']
    start_urls = ['http://arch.gzhu.edu.cn/szll/jsdw.htm',
                  'http://arch.gzhu.edu.cn/szll/jsdw/4.htm',
                  'http://arch.gzhu.edu.cn/szll/jsdw/3.htm',
                  'http://arch.gzhu.edu.cn/szll/jsdw/2.htm',
                  'http://arch.gzhu.edu.cn/szll/jsdw/1.htm',
                  'http://arch.gzhu.edu.cn/szll/msfc.htm',
                  'http://arch.gzhu.edu.cn/szll/msfc/1.htm']
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//a[@class="name"]/@href').extract())
        for link in all_teacher_links:
            url = 'http://arch.gzhu.edu.cn/' + link[len(link) - 18:]
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//div[@class="tit"]/h2/text()').extract()
        post_info = response.xpath('//div[@class="time"]//text()').extract()
        info = response.xpath('//*[@id="vsb_content"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content_2"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content_500"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'arch',
            'name': name,
            'post_info': post_info,
            'info': info
        }
        # office=response.xpath('//*[@id="vsb_content_4"]/p[2]/text()').extract_first()
        # Research_areas = response.xpath('//*[@id="vsb_content_4"]/p[3]/text()').extract()
        # Personal_profile = response.xpath('//*[@id="vsb_content_4"]/p[5]/text()').extract()
        # Education_background = response.xpath('').extract()
        # Academic_work_experience = response.xpath('').extract()
        # Teaching_Courses = response.xpath('').extract()
        # Research_Services = response.xpath('').extract()
        # Teaching_Incentives = response.xpath('').extract()
        # Research_results = response.xpath('').extract()
