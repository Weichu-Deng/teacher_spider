import scrapy


# 生命科学学院

class SesSpider(scrapy.Spider):
    name = 'lifesciences'
    allowed_domains = ['lifesciences.gzhu.edu.cn']
    start_urls = ['http://lifesciences.gzhu.edu.cn/bksjy/szll/zgzc.htm',
                  'http://lifesciences.gzhu.edu.cn/bksjy/szll/zgzc/1.htm',
                  'http://lifesciences.gzhu.edu.cn/bksjy/szll/fgzc.htm',
                  'http://lifesciences.gzhu.edu.cn/bksjy/szll/fgzc/2.htm',
                  'http://lifesciences.gzhu.edu.cn/bksjy/szll/fgzc/1.htm',
                  'http://lifesciences.gzhu.edu.cn/bksjy/szll/zjzc.htm',
                  'http://lifesciences.gzhu.edu.cn/bksjy/szll/zjzc/2.htm',
                  'http://lifesciences.gzhu.edu.cn/yjsjy/dsjj.htm']
    count = 0

    def parse(self, response):
        all_teacher_links1 = set(response.xpath('//ul[@class="tit-list"]//a/@href').extract())
        all_teacher_links2 = set(response.xpath('//li[@class="cleafix"]//a/@href').extract())
        all_teacher_links = all_teacher_links1 | all_teacher_links2
        for link in all_teacher_links:
            url = 'http://lifesciences.gzhu.edu.cn' + link[len(link) - 19:]
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//h2/text()').extract()
        post_info = response.xpath('//div[@style="margin-top: 20px;"]/text()').extract()
        info = response.xpath('//*[@id="vsb_content"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content_2"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content_4"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content_500"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'lifesciences',
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
