# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import os
import re

class GzhuTeacherPipeline:
    base_dir = '结果文件' + os.sep
    def save_data_csv(self,college,item):
        if not os.path.isdir(self.base_dir):
            os.makedirs(self.base_dir)
        file_path = self.base_dir + os.sep + '{}.csv'.format(college)
        if not os.path.isfile(file_path):
            is_first_write = 1
        else:
            is_first_write = 0
        with open(file_path, 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            if is_first_write:
                writer.writerow(['姓名', '发布时间', '详情'])
            if item['post_info']!=[]:
                try:
                    time = re.findall('\d{4}-\d{2}-\d{2}', ''.join(item['post_info']))[0]
                except IndexError:
                    try:
                        time = re.findall('\d{4}年\d{2}月\d{2}日', ''.join(item['post_info']))[0]
                    except IndexError:
                        time = re.findall('\d{4}/\d{2}/\d{2}', ''.join(item['post_info']))[0]
            else:
                time=''
            info=item['info']
            str = '\n'
            for i in range(0, len(info) - 1):
                if str in info[i] and str in info[i + 1]:
                    info[i] = ''
            try:
                writer.writerow([item['name'][0], time, ''.join(info)])
            except:
                print("写入失败",item)


    def process_item(self, item, spider):
        if item['college']=='ses':
            self.save_data_csv(college='经济与统计学院',item=item)
        if item['college']=='jyxy':
            self.save_data_csv(college='教育学院(师范学院)',item=item)
        if item['college']=='fs':
            self.save_data_csv(college='外国语学院',item=item)
        if item['college'] == 'gupa':
            self.save_data_csv(college='公共管理学院', item=item)
        if item['college'] == 'maths':
            self.save_data_csv(college='数学与信息科学学院', item=item)
        if item['college'] == 'geo':
            self.save_data_csv(college='地理科学与遥感学院', item=item)
        if item['college'] == 'ece':
            self.save_data_csv(college='电子与通信工程学院', item=item)
        if item['college'] == 'tm':
            self.save_data_csv(college='土木工程学院', item=item)
        if item['college'] == 'cxcy':
            self.save_data_csv(college='创新创业学院', item=item)
        if item['college'] == 'lsxy':
            self.save_data_csv(college='法学院（律师学院）', item=item)
        if item['college'] == 'pess':
            self.save_data_csv(college='体育学院', item=item)
        if item['college'] == 'xw':
            self.save_data_csv(college='新闻与传播学院', item=item)
        if item['college'] == 'yywd':
            self.save_data_csv(college='音乐舞蹈学院', item=item)
        if item['college'] == 'spee':
            self.save_data_csv(college='物理与材料科学学院', item=item)
        if item['college'] == 'lifesciences':
            self.save_data_csv(college='生命科学学院', item=item)
        if item['college'] == 'jsj':
            self.save_data_csv(college='计算机科学与网络工程学院', item=item)
        if item['college'] == 'environ':
            self.save_data_csv(college='环境科学与工程学院', item=item)
        if item['college'] == 'marxism':
            self.save_data_csv(college='马克思主义学院', item=item)
        if item['college'] == 'rw':
            self.save_data_csv(college='人文学院', item=item)
        if item['college'] == 'bas':
            self.save_data_csv(college='管理学院', item=item)
        if item['college'] == 'art':
            self.save_data_csv(college='美术与设计学院', item=item)
        if item['college'] == 'hhu':
            self.save_data_csv(college='化学化工学院', item=item)
        if item['college'] == 'jd':
            self.save_data_csv(college='机械与电气工程学院', item=item)
        if item['college'] == 'arch':
            self.save_data_csv(college='建筑与城市规划学院', item=item)
        if item['college'] == 'gjjyxy':
            self.save_data_csv(college='国际教育学院（卫斯理安学院）', item=item)
        return item
