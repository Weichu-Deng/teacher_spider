import scrapy


# 数学与信息科学学院

class SesSpider(scrapy.Spider):
    name = 'maths'
    allowed_domains = ['maths.gzhu.edu.cn']
    start_urls = ['http://maths.gzhu.edu.cn/szdw.htm',
                  'http://maths.gzhu.edu.cn/szdw/3.htm',
                  'http://maths.gzhu.edu.cn/szdw/2.htm',
                  'http://maths.gzhu.edu.cn/szdw/1.htm'
                  ]
    count = 0
    a = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//ul[@class="list-teacher"]//a[@target="_blank"]/@href').extract())
        self.a += len(all_teacher_links)
        for link in all_teacher_links:
            url = 'http://maths.gzhu.edu.cn' + link[2:]
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//h1/text()').extract()
        post_info = response.xpath('//div[@class="info"]/span/text()').extract()
        info = response.xpath('//div[@class="article-text"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count, 'a', self.a)
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
