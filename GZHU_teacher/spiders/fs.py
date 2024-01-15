import scrapy


# 外国语学院

class SesSpider(scrapy.Spider):
    name = 'fs'
    allowed_domains = ['fs.gzhu.edu.cn']
    start_urls = ['http://fs.gzhu.edu.cn/szdw/jsbs1/js.htm',
                  'http://fs.gzhu.edu.cn/szdw/jsbs1/bs.htm',
                  'http://fs.gzhu.edu.cn/szdw/jsxr.htm',
                  'http://fs.gzhu.edu.cn/szdw/jsbs1/bs/1.htm']
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//li/a[@target="_blank"]/@href').extract())
        for link in all_teacher_links:
            url = 'http://fs.gzhu.edu.cn' + link[5:]
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//h3/text()').extract()
        post_info = response.xpath('//div[@style="text-align:center;margin-top:15px;"]/em/text()').extract()
        post_info = ''.join(post_info)
        info = response.xpath('//div[@id="vsb_content"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'fs',
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
