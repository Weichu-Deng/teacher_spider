import scrapy


# 地理科学与遥感学院

class SesSpider(scrapy.Spider):
    name = 'geo'
    allowed_domains = ['geo.gzhu.edu.cn']
    start_urls = ['http://geo.gzhu.edu.cn/szdw/zrjs.htm',
                  'http://geo.gzhu.edu.cn/szdw/xjys1.htm',
                  'http://geo.gzhu.edu.cn/szdw/xzgl.htm',
                  'http://geo.gzhu.edu.cn/szdw/sys.htm',
                  'http://geo.gzhu.edu.cn/szdw/bsh.htm'
                  ]
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//div[@class="brief"]//a/@href').extract())
        for link in all_teacher_links:
            url = 'http://geo.gzhu.edu.cn' + link[2:]
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://geo.gzhu.edu.cn/info/1210/4234.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('/html/head/title/text()').extract_first()
        name = name.split('-')[0:-1]
        post_info = []
        info = response.xpath('//div[@id="vsb_content_2"]//text()').extract()
        if info == []:
            info = response.xpath('//div[@id="vsb_content"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': self.name,
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
