import scrapy


# 法学院（律师学院）

class SesSpider(scrapy.Spider):
    name = 'lsxy'
    allowed_domains = ['fx.gzhu.edu.cn']
    start_urls = ['http://fx.gzhu.edu.cn/szll/js.htm',
                  'http://fx.gzhu.edu.cn/szll/fjs.htm',
                  'http://fx.gzhu.edu.cn/szll/js1.htm',
                  'http://fx.gzhu.edu.cn/szll/jnxjsz.htm',
                  'http://fx.gzhu.edu.cn/szll/llfxjys.htm',
                  'http://fx.gzhu.edu.cn/szll/msfjys.htm',
                  'http://fx.gzhu.edu.cn/szll/ssfjys.htm',
                  'http://fx.gzhu.edu.cn/szll/xsfjys.htm',
                  'http://fx.gzhu.edu.cn/szll/gjfjys.htm',
                  'http://fx.gzhu.edu.cn/szll/rqyjy.htm',
                  'http://fx.gzhu.edu.cn/szll/xsds.htm',
                  'http://fx.gzhu.edu.cn/szll/zsds.htm']
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//a[@target="_blank"]/@href').extract())
        for link in all_teacher_links:
            url = 'http://fx.gzhu.edu.cn' + link[2:]
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//table[@class="winstyle61884"]//td[@align="center"]/text()').extract_first()
        name = [name]
        post_info = response.xpath('//span[@class="timestyle61884"]/text()').extract()
        info = response.xpath('//td[@class="contentstyle61884"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content_2"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'lsxy',
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
