from selenium import webdriver
import os
import django
from time import sleep

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "angelhack.settings")
django.setup()

from market.models import Market

def crawling():
    url = 'http://www.sbiz.or.kr/sijangtong/nation/sijang/readSijangList.do?menu_type_a=A&menu_cms=&menu_id=010100#searchBtn'
    driver = webdriver.Chrome('C:/Program Files/chromedriver_win32/chromedriver.exe')
    driver.get(url)
    sleep(5)
    for num in range(1, 3118, 2):
        market_name = driver.find_element_by_css_selector(f'#sijangList > table > tbody > tr:nth-child({num}) > td > table > tbody > tr > td:nth-child(1) > span > a').text
        try:
            market = Market.objects.get(name=market_name)
        except:
            continue

        xpath = f'//*[@id="sijangList"]/table/tbody/tr[{num}]/td/table/tbody/tr/td[1]/span/a'
        search_result = driver.find_element_by_xpath(xpath)
        search_result.click()
        sleep(0.1)

        parking_num = int(driver.find_element_by_css_selector('#tab1 > table > tbody > tr:nth-child(9) > td:nth-child(2)').text[6])
        toilet_num = int(driver.find_element_by_css_selector('#tab1 > table > tbody > tr:nth-child(10) > td').text[6])

        market.parking = parking_num
        market.toilet = toilet_num
        market.save()
    
if __name__ == "__main__":
    crawling()