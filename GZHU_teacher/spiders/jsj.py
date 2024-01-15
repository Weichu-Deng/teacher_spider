import scrapy


# 计算机科学与网络工程学院

class SesSpider(scrapy.Spider):
    name = 'jsj'
    allowed_domains = ['jsj.gzhu.edu.cn']
    start_urls = ['http://jsj.gzhu.edu.cn/szdw1/yszl.htm',
                  'http://jsj.gzhu.edu.cn/szdw1/jsjkxywlgcxysz.htm',
                  'http://jsj.gzhu.edu.cn/szdw1/wlkjxjjsyjysz.htm',
                  'http://jsj.gzhu.edu.cn/szdw1/jskjyjysz.htm',
                  'http://jsj.gzhu.edu.cn/szdw1/rgznyqklyjy.htm']
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//a[@target="_blank"]/@href').extract())
        for link in all_teacher_links:
            if 'http' in link:
                url = link
            else:
                url = 'http://jsj.gzhu.edu.cn' + link[2:]
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jsj.gzhu.edu.cn/info/1122/1327.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('.//h2//text()').extract()
        if name == []:
            name = response.xpath('/html/head/title/text()').extract_first()
            name = name.split("-")[0]
            name = [name]

        post_info = response.xpath('//h3//text()').extract()
        info = response.xpath('//div[@id="vsb_content"]//text()').extract()
        if info == []:
            info = response.xpath('//div[@id="vsb_content_2"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'jsj',
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
