import scrapy


# 体育学院

class SesSpider(scrapy.Spider):
    name = 'pess'
    allowed_domains = ['pess.gzhu.edu.cn']
    start_urls = ['http://pess.gzhu.edu.cn/szdw/jsml1/tyjyx.htm',
                  'http://pess.gzhu.edu.cn/szdw/jsml1/tyjyx/2.htm',
                  'http://pess.gzhu.edu.cn/szdw/jsml1/tyjyx/1.htm',
                  'http://pess.gzhu.edu.cn/szdw/jsml1/shtyx.htm',
                  'http://pess.gzhu.edu.cn/szdw/jsml1/shtyx/1.htm',
                  'http://pess.gzhu.edu.cn/szdw/jsml1/ggtyb.htm',
                  'http://pess.gzhu.edu.cn/szdw/jsml1/ggtyb/2.htm',
                  'http://pess.gzhu.edu.cn/szdw/jsml1/ggtyb/1.htm',
                  'http://pess.gzhu.edu.cn/szdw/sssds.htm',
                  'http://pess.gzhu.edu.cn/szdw/sssds/2.htm',
                  'http://pess.gzhu.edu.cn/szdw/sssds/1.htm']
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//ul[@class="cleafix"]/li/a/@href').extract())
        for link in all_teacher_links:
            url = 'http://pess.gzhu.edu.cn' + link[len(link) - 19:]
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://pess.gzhu.edu.cn/info/1148/2895.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//h1/text()').extract()
        post_info = response.xpath('//h3//text()').extract()
        info = response.xpath('//*[@id="vsb_content_501"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content_2"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'pess',
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
