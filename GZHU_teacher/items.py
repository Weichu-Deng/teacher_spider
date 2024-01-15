# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GzhuTeacherItem(scrapy.Item):
    name = scrapy.Field()  # 名字
    title=scrapy.Field() # 职称
    Email = scrapy.Field() # 电子邮件
    office = scrapy.Field()  # 办公室
    Research_areas = scrapy.Field()  # 研究领域
    Personal_profile = scrapy.Field()  # 个人简介
    Education_background = scrapy.Field()  # 教育背景
    Academic_work_experience = scrapy.Field()  # 学术工作经历
    Teaching_Courses = scrapy.Field()  # 教授课程
    Research_Services = scrapy.Field()  # 科研服务
    Teaching_Incentives = scrapy.Field()  # 教学奖励
    Research_results = scrapy.Field()  # 研究成果

