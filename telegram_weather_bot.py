import time
from telegram import ChatAction
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler

import sys
import os
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import tqdm
from tqdm.notebook import tqdm

dict = {}
dict1 = {}
# Step 1. 크롬 웹브라우저 실행
path = "chromedriver.exe"  # 윈도우는 "chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument( '--headless' )
chrome_options.add_argument( '--log-level=3' )
chrome_options.add_argument( '--disable-logging' )
chrome_options.add_argument( '--no-sandbox' )
chrome_options.add_argument( '--disable-gpu' )


driver = webdriver.Chrome(path)
# 사이트 주소는 노르웨이 날씨
driver.get('https://www.yr.no/place/South_Korea/Busan/Busan/')

time.sleep(2)


BOT_TOKEN = 'your telegram token'

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def cmd_task_buttons(update, context):
    task_buttons = [[
        InlineKeyboardButton('1.오늘 날씨', callback_data=1)
        , InlineKeyboardButton('2.내일 날씨', callback_data=2)
    ], [
        InlineKeyboardButton('3.예보', callback_data=3)
    ]]

    reply_markup = InlineKeyboardMarkup(task_buttons)

    context.bot.send_message(
        chat_id=update.message.chat_id
        , text='날씨'
        , reply_markup=reply_markup
    )


def cb_button(update, context):
    query = update.callback_query
    data = query.data

    context.bot.send_chat_action(
        chat_id=update.effective_user.id
        , action=ChatAction.TYPING
    )

    if data == '3':
        for i in range(1,5):
            # 시간
            Today_time = driver.find_element_by_xpath("""//*[@id="ctl00_ctl00_contentBody"]/div[2]/div[2]/table[3]/tbody/tr[{0}]/td[1]""".format(i))
            Today_time_text = Today_time.text

            # 날씨
            Today_w = driver.find_element_by_xpath("""//*[@id="ctl00_ctl00_contentBody"]/div[2]/div[2]/table[3]/tbody/tr[{0}]/td[2]""".format(i))
            Today_w_text = Today_w.text

            # 온도
            Today_tem = driver.find_element_by_css_selector("table:nth-child(3) > tbody > tr:nth-child({0}) > td:nth-child(3)".format(i))
            Today_tem_text = Today_tem.text

            # 강수량
            Today_p = driver.find_element_by_css_selector("table:nth-child(3) > tbody > tr:nth-child({0}) > td:nth-child(4)".format(i))
            Today_p_text = Today_p.text
        
            Today_total = Today_time_text+" "+Today_w_text+" "+Today_tem_text+" "+Today_p_text
            context.bot.send_message(
                chat_id=update.effective_chat.id
                , text=Today_total
               
        )
    # else:
        #오늘 날씨
      #  Today_data= driver.find_element_by_css_selector("table:nth-child(1) > caption")
       # Today_data_text = Today_data.text
        #context.bot.edit_message_text(
       #     chat_id=update.effective_chat.id
        #    , text='[{}] 로딩중입니다.'.format(data)
            
       # )

    if data == '1':
            # 오늘 날씨
            # Today_data= driver.find_element_by_css_selector("table:nth-child(1) > caption")
            # Today_data_text = Today_data.text
        for j in range(1,5):
                # 시간
            Today_time = driver.find_element_by_xpath("""//*[@id="ctl00_ctl00_contentBody"]/div[2]/div[2]/table[1]/tbody/tr[{0}]/td[1]""".format(j))
            Today_time_text = Today_time.text

                # 날씨
            Today_w = driver.find_element_by_xpath("""//*[@id="ctl00_ctl00_contentBody"]/div[2]/div[2]/table[1]/tbody/tr[{0}]/td[2]""".format(j))
            Today_w_text = Today_w.text

                # 온도
            Today_tem = driver.find_element_by_css_selector("table:nth-child(1) > tbody > tr:nth-child({0}) > td:nth-child(3)".format(j))
            Today_tem_text = Today_tem.text

                # 강수량
            Today_p = driver.find_element_by_css_selector("table:nth-child(1) > tbody > tr:nth-child({0}) > td:nth-child(4)".format(j))
            Today_p_text = Today_p.text
        
            Today_total = Today_time_text+" "+Today_w_text+" "+Today_tem_text+" "+Today_p_text
            context.bot.send_message(
                chat_id=update.effective_chat.id
                , text=Today_total
            )
    elif data == '2':
        for k in range(1,5):
                # 시간
            Today_time = driver.find_element_by_xpath("""//*[@id="ctl00_ctl00_contentBody"]/div[2]/div[2]/table[2]/tbody/tr[{0}]/td[1]""".format(k))
            Today_time_text = Today_time.text

                # 날씨
            Today_w = driver.find_element_by_xpath("""//*[@id="ctl00_ctl00_contentBody"]/div[2]/div[2]/table[2]/tbody/tr[{0}]/td[2]""".format(k))
            Today_w_text = Today_w.text

                # 온도
            Today_tem = driver.find_element_by_css_selector("table:nth-child(2) > tbody > tr:nth-child({0}) > td:nth-child(3)".format(k))
            Today_tem_text = Today_tem.text

                # 강수량
            Today_p = driver.find_element_by_css_selector("table:nth-child(2) > tbody > tr:nth-child({0}) > td:nth-child(4)".format(k))
            Today_p_text = Today_p.text
        
            Today_total = Today_time_text+" "+Today_w_text+" "+Today_tem_text+" "+Today_p_text
            context.bot.send_message(
                chat_id=update.effective_chat.id
                , text=Today_total
            )




def crawl_navernews():
    time.sleep(5)
    print('오늘날씨 로딩완료.')


def crawl_zigbang():
    time.sleep(5)
    print('내일날씨 로딩완료')


task_buttons_handler = CommandHandler('tasks', cmd_task_buttons)
button_callback_handler = CallbackQueryHandler(cb_button)

dispatcher.add_handler(task_buttons_handler)
dispatcher.add_handler(button_callback_handler)

updater.start_polling()
updater.idle()
