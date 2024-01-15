import scrapy


# 新闻与传播学院

class SesSpider(scrapy.Spider):
    name = 'xw'
    allowed_domains = ['xw.gzhu.edu.cn']
    start_urls = ['http://xw.gzhu.edu.cn/szll.htm']
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//div[@class="vsb-space"]//a[@target="_blank"]/@href').extract())
        for link in all_teacher_links:
            url = 'http://xw.gzhu.edu.cn/' + link
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//h2/text()').extract()
        post_info = response.xpath('//p[@style="text-align:center;background: #f5f5f5;"]//text()').extract()
        info = response.xpath('//*[@id="vsb_content"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content_2"]//text()').extract()
        if info == []:
            info = response.xpath('//*[@id="vsb_content_500"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'xw',
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
