import re
a='作者：\xa0\xa0 时间：2021-03-05\xa0\xa0 点击数：'
b=re.findall('\d{4}-\d{2}-\d{2}',a)[0]
print(b)