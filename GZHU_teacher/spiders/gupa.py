import scrapy


# 公共管理学院

class SesSpider(scrapy.Spider):
    name = 'gupa'
    allowed_domains = ['gupa.gzhu.edu.cn']
    start_urls = ['http://gupa.gzhu.edu.cn/szll/zfglx1/js.htm',
                  'http://gupa.gzhu.edu.cn/szll/zfglx1/fjs.htm',
                  'http://gupa.gzhu.edu.cn/szll/zfglx1/zljs.htm',
                  ]
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//div[@class="main_rpicL"]/a/@href').extract())
        for link in all_teacher_links:
            url = 'http://gupa.gzhu.edu.cn' + link[5:]
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//h2/text()').extract()
        post_info = response.xpath('//div[@class="main_contit"]/p/text()').extract()
        info = response.xpath('//div[@class="main_conDiv"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'gupa',
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
