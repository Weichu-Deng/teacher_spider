import scrapy


# 土木工程学院

class SesSpider(scrapy.Spider):
    name = 'tm'
    allowed_domains = ['tm.gzhu.edu.cn']
    start_urls = ['http://tm.gzhu.edu.cn/szdw/ys.htm',
                  'http://tm.gzhu.edu.cn/szdw/bssds.htm',
                  'http://tm.gzhu.edu.cn/szdw/jsxx.htm']
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//ul/li/a[@target="_blank"]/@href').extract())
        for link in all_teacher_links:
            url = 'http://tm.gzhu.edu.cn' + link[2:]
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//h3/text()').extract()
        post_info = response.xpath('//p[@style="float:left"]/span/text()').extract()
        info = response.xpath('//*[@id="vsb_content"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content_2"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'tm',
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
