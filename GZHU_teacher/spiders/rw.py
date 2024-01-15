import scrapy


# 人文学院

class SesSpider(scrapy.Spider):
    name = 'rw'
    allowed_domains = ['rw.gzhu.edu.cn']
    start_urls = ['http://rw.gzhu.edu.cn/szdw1/szll.htm',
                  'http://rw.gzhu.edu.cn/szdw1/szll/4.htm',
                  'http://rw.gzhu.edu.cn/szdw1/szll/3.htm',
                  'http://rw.gzhu.edu.cn/szdw1/szll/2.htm',
                  'http://rw.gzhu.edu.cn/szdw1/szll/1.htm', ]
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//a[@target="_blank"]/@href').extract())
        for link in all_teacher_links:
            if 'http' in link:
                url = link
            else:
                url = 'http://rw.gzhu.edu.cn' + link[len(link) - 19:]
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('/html/body/div[4]/div/div[2]/form/div/div[1]/text()').extract()
        post_info = response.xpath('/html/body/div[4]/div/div[2]/form/div/div[2]/text()').extract()
        info = response.xpath('//div[@id="vsb_content"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'rw',
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
