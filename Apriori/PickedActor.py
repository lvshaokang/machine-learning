from efficient_apriori import apriori
from lxml import etree
import time
from selenium import webdriver
import csv

driver = webdriver.Chrome()
director = u'周星驰'
file_name = './' + director + '.csv'
base_url = 'https://movie.douban.com/subject_search?search_text=' + director + '&cat=1002&start='
out = open(file_name, 'w', newline='', encoding='utf-8-sig')
csv_write = csv.writer(out, dialect='excel')


def download(request_url):
    driver.get(request_url)
    time.sleep(1)
    html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    html = etree.HTML(html)
    movie_lists = html.xpath(
        "/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']")
    name_lists = html.xpath(
        "/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']")
    num = len(movie_lists)
    if num > 15:
        movie_lists = movie_lists[1:]
        name_lists = name_lists[1:]
    for (movie, name_list) in zip(movie_lists, name_lists):
        if name_list.text is None:
            continue
        print(name_list.text)
        names = name_list.text.split('/')
        if names[0].strip() == director:
            names[0] = movie.text
            csv_write.writerow(names)
    print('OK')
    if num >= 15:
        return True
    else:
        return False


start = 0
while start < 10000:
    request_url = base_url + str(start)
    flag = download(request_url)
    if flag:
        start = start + 15
    else:
        break
out.close()
print('finished')