import scrapy


# 中南大学

class ZhongnanSpider(scrapy.Spider):
    name = 'zhongnan'
    allowed_domains = ['csu.edu.cn']
    start_urls = ['https://faculty.csu.edu.cn/xk.jsp?urltype=tsites.DisciplineTeacherList&wbtreeid=1003&st=0&id=1121&lang=zh_CN#disciplineteacher']
    count = 0

    def parse(self, response):
        all_teacher_links = set(response.xpath('//a[@class="name"]/@href').extract())
        for link in all_teacher_links:
            url = 'http://arch.gzhu.edu.cn/' + link[len(link) - 18:]
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_info)
        #
        # yield scrapy.Request(url='http://jyxy.gzhu.edu.cn/info/1134/2574.htm', callback=self.parse_info)

    def parse_info(self, response):
        name = response.xpath('//div[@class="tit"]/h2/text()').extract()
        post_info = response.xpath('//div[@class="time"]//text()').extract()
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
            'college': 'arch',
            'name': name,
            'post_info': post_info,
            'info': info
        }
