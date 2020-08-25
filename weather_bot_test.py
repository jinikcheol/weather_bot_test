import sys
import os
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import tqdm
from tqdm.notebook import tqdm

dict = {}
#Step 1. 크롬 웹브라우저 실행
path = "chromedriver.exe"   # 윈도우는 "chromedriver.exe"

driver = webdriver.Chrome(path)
# 사이트 주소는 노르웨이 날씨
driver.get('https://www.yr.no/place/South_Korea/Busan/Busan/')

time.sleep(2)

for i in range(1,4):
    # 날짜
    Today_data= driver.find_element_by_css_selector("table:nth-child({}) > caption".format(i))
    Today_data_text = Today_data.text
    print(Today_data_text)
    for j in range(1,3):
        # 시간
        Today_time = driver.find_element_by_xpath("""//*[@id="ctl00_ctl00_contentBody"]/div[2]/div[2]/table[{0}]/tbody/tr[{1}]/td[1]""".format(i,j))
        Today_time_text = Today_time.text

        # 날씨
        Today_w = driver.find_element_by_xpath("""//*[@id="ctl00_ctl00_contentBody"]/div[2]/div[2]/table[{0}]/tbody/tr[{1}]/td[2]""".format(i,j))
        Today_w_text = Today_w.text

        # 온도
        Today_tem = driver.find_element_by_css_selector("table:nth-child({0}) > tbody > tr:nth-child({1}) > td:nth-child(3)".format(i,j))
        Today_tem_text = Today_tem.text

        # 강수량
        Today_p = driver.find_element_by_css_selector("table:nth-child({0}) > tbody > tr:nth-child({1}) > td:nth-child(4)".format(i,j))
        Today_p_text = Today_p.text

        print(Today_time_text)
        print(Today_w_text)
        print(Today_tem_text)
        print(Today_p_text)
        
