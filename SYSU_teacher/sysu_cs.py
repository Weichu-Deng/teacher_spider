import multiprocessing
import time

import pandas as pd
from selenium import webdriver


def get_links(url='https://cse.sysu.edu.cn/personnel/teachers'):
    browser = webdriver.Firefox()
    browser.get(url)
    count = 0
    while (True):
        all_teacher = browser.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div/ul/li/a')
        count += 1
        if all_teacher != [] or count >= 20:
            break
        else:
            time.sleep(1)

    links = []
    for teacher in all_teacher:
        links.append(teacher.get_attribute('href'))
    links = set(links)
    browser.close()
    return links


def get_detail(url=['https://cse.sysu.edu.cn/content/6791'], q=multiprocessing.Queue()):
    browser = webdriver.Firefox()
    res = []
    for i in url:
        browser.get(i)
        count = 0
        while (True):
            name = browser.find_elements_by_xpath('/html/body/div[2]/div/section/h1')
            main_content = browser.find_elements_by_xpath('// *[ @ id = "block-system-main"]')
            try:
                name = name[0].text
                main_content = main_content[0].text
            except:
                pass
            count += 1
            if name != [] or count >= 20:
                break
            else:
                time.sleep(1)
        temp = (name, i, time.strftime("%Y-%m-%d %H:%M:%S"), main_content)
        res.append(temp)

    browser.close()
    print(res)
    q.put(res)
    return res


if __name__ == '__main__':
    links = list(get_links())
    # links=links[:8]
    res = []
    n = 12  # n并行进程数,电脑内存小调整并行进程数
    N = links.__len__() // n
    links = [links[i:i + N] for i in range(0, len(links), N)]
    if len(links) > n:
        links[-2] = links[-1] + links[-2]
        links.pop()

    process_list = []
    q = multiprocessing.Queue()
    jobs = []
    for i in range(n):
        p = multiprocessing.Process(target=get_detail, args=(links[i], q))
        jobs.append(p)
        p.start()

    results = [q.get() for j in jobs]
    res = pd.DataFrame(results)
    for i in range(1, len(results)):
        results[0] = results[0] + results[i]
    res = pd.DataFrame(results[0])
    res.columns = ['姓名', '个人链接', '爬取时间', '详情']
    res.to_csv("SYSU_teacher/sysu_cs.csv")
