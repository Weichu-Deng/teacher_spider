import scrapy


# 创新创业学院

class SesSpider(scrapy.Spider):
    name = 'cxcy'
    allowed_domains = ['cxcy.gzhu.edu.cn']
    start_urls = ['http://cxcy.gzhu.edu.cn/list5.jsp?urltype=tree.TreeTempUrl&wbtreeid=1043',
                  'http://cxcy.gzhu.edu.cn/list5.jsp?a138266t=2&a138266p=2&a138266c=10&urltype=tree.TreeTempUrl&wbtreeid=1043',
                  'http://cxcy.gzhu.edu.cn/list5.jsp?urltype=tree.TreeTempUrl&wbtreeid=1044',
                  'http://cxcy.gzhu.edu.cn/list5.jsp?a138266t=2&a138266p=2&a138266c=10&urltype=tree.TreeTempUrl&wbtreeid=1044'
                  ]
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//a[@target="_blank"]/@href').extract())
        for link in all_teacher_links:
            url = 'http://cxcy.gzhu.edu.cn/' + link[:]
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//h3[@class="title"]/text()').extract()
        # post_info=response.xpath('//p[@style="float:left"]/span/text()').extract()
        post_info = []
        info = response.xpath('//*[@id="vsb_content"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'cxcy',
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
