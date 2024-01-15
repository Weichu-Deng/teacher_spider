import scrapy


# 电子与通信工程学院

class SesSpider(scrapy.Spider):
    name = 'ece'
    allowed_domains = ['ece.gzhu.edu.cn']
    start_urls = ['http://ece.gzhu.edu.cn/dzytxgcx/js.htm',
                  'http://ece.gzhu.edu.cn/dzytxgcx/fjs.htm',
                  'http://ece.gzhu.edu.cn/dzytxgcx/js1.htm',
                  'http://ece.gzhu.edu.cn/dzytxgcx/sys.htm',
                  'http://ece.gzhu.edu.cn/wlwgcx/js.htm',
                  'http://ece.gzhu.edu.cn/wlwgcx/fjs.htm',
                  'http://ece.gzhu.edu.cn/dzytxgcx/fjs/1.htm',
                  'http://ece.gzhu.edu.cn/wlwgcx/js1.htm',
                  'http://ece.gzhu.edu.cn/wlwgcx/sys.htm',
                  'http://ece.gzhu.edu.cn/szdw1/xzry.htm',
                  'http://ece.gzhu.edu.cn/szdw1/tpry.htm',
                  ]
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//dl/a/@href').extract())
        for link in all_teacher_links:
            url = 'http://ece.gzhu.edu.cn' + link[2:]
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://geo.gzhu.edu.cn/info/1210/4234.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//div[@class="content-title fl"]/h3/text()').extract()
        post_info = response.xpath('//div[@class="content-title fl"]/i/text()').extract()
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
