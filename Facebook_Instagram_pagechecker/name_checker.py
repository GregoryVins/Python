#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import csv


def init_driver():
    """
    Settings. Initialization driver without graphical window and load images.
    """
    options = webdriver.ChromeOptions()
    prefs = {'profile.managed_default_content_settings.images': 2}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    return driver


def fb_cheker(name: str, data: str):
    """
    Check nickname in website.
    :returns:   - "?" if user's page blocked or hidden
                - "-" if user's page already taken
                - "name" if address empty
    """
    for nick in data.split():
        if nick.lower() in 'facebook':
            return '?'
        elif nick in 'Страница':
            return name
    return '-'


facebook_url = 'https://www.facebook.com/'
instagram_url = 'https://www.instagram.com/'

with open('names.txt')as read_file:
    nicknames = read_file.read().split()  # read names from file

login = '<YOUR LOGIN>'
password = '<YOUR PASSWORD>'

with open('result.csv', 'a') as file:  # init row in table
    writer = csv.writer(file)
    writer.writerow(['request', 'facebook url', 'instagram url', ])

browser = init_driver()  # run driver
browser.get(facebook_url)  # go to usl
browser.find_element_by_id('email').send_keys(login)  # find the input area and write login
browser.find_element_by_id('pass').send_keys(password)  # and password
browser.find_element_by_id('loginbutton').click()  # find the button and click
time.sleep(2)  # We must wait for the content to load.

result = []  # We will be save data in this variable

for nickname in nicknames:
    td = [nickname]
    browser.get(f'{facebook_url}{nickname}')  # go to page
    time.sleep(2)  # loading data
    respone = browser.title  # getting title
    td.append(
        f'{facebook_url}{fb_cheker(nickname, respone)}' if nickname == fb_cheker(nickname, respone) else fb_cheker(
            nickname,
            respone))  # ternary operator, sorry for this
    result.append(td)  # add in temporary variable

position = 0  #

browser.get(instagram_url)  # go to instagram website
browser.implicitly_wait(2)  # waiting

btns = browser.find_elements_by_tag_name('button')  # get all buttons, because instagram have random name-classes
browser.implicitly_wait(2)
btns[1].click()  # we hava to click in second button "Join in as <facebook account>"
browser.implicitly_wait(2)

for nickname in nicknames:  # analogous iterates
    browser.get(f'{instagram_url}{nickname}')
    time.sleep(2)
    respone = browser.title
    print(respone, f'{instagram_url}{nickname}')
    result[position].append('-' if nickname in respone else f'{instagram_url}{nickname}')
    position += 1

with open('result.csv', 'a') as file:  # save in CSV file
    writer = csv.writer(file)
    for i in result:
        writer.writerow(i)

browser.quit()  # Close browser
