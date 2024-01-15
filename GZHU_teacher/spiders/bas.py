import scrapy


# 管理学院

class SesSpider(scrapy.Spider):
    name = 'bas'
    allowed_domains = ['bas.gzhu.edu.cn']
    start_urls = ['http://bas.gzhu.edu.cn/newszll/js/gcglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js/cxyzlx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js/rlzyglyscyxx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js/wlyyyglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js/sjkxydzswx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js/lyyjdglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js/hzglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js/hjx.htm',
                  'http://bas.gzhu.edu.cn/newszll/fjsnew/gcglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/fjsnew/cxyzlx.htm',
                  'http://bas.gzhu.edu.cn/newszll/fjsnew/rlzyglyscyxx.htm',
                  'http://bas.gzhu.edu.cn/newszll/fjsnew/wlyyyglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/fjsnew/sjkxydzswx.htm',
                  'http://bas.gzhu.edu.cn/newszll/fjsnew/lyyjdglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/fjsnew/hzglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/fjsnew/hjx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js1/gcglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js1/cxyzlx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js1/rlzyglyscyxx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js1/wlyyyglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js1/sjkxydzswx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js1/lyyjdglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js1/hzglx.htm',
                  'http://bas.gzhu.edu.cn/newszll/js1/hjx.htm',
                  ]
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//html/body/div[3]/div[2]/div[2]/div/div/div[3]//li/a/@href').extract())
        for link in all_teacher_links:
            if 'http' in link:
                url = link
            else:
                url = 'http://bas.gzhu.edu.cn' + link[5:]
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//h1/text()').extract()
        post_info = []
        info = response.xpath('//div[@id="vsb_content"]//text()').extract()
        if info == []:
            self.count += 1
            print("爬取失败的URL", response.url)
        print('未爬取：', self.count)
        print(info)
        yield {
            'college': 'bas',
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
