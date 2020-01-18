#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time, sys, os, json, random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.keys import Keys


urls = [
    "http://gagusuri.kr/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://gagusuri.kr/%EC%A7%88%EB%AC%B8&%EB%8B%B5%EB%B3%80/write",
	"http://gagusoori.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://g-house.kr/Q&A/write",
    "http://g-house.kr/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://friendsmusic.co.kr/Q&A/write",
    "http://fork08.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://fngresearch.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://fakorea.net/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    
    "http://eunjintailor.com/%EA%B3%A0%EA%B0%9D%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://es0482.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://eps-hightech.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://egbio.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://egss.co.kr/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",    
    "http://elove1004.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    
    "http://www.earning.co.kr/%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://earkeeper.net/%EC%9D%B4%EB%B2%A4%ED%8A%B8%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://eagonmaru.com/Q&A/write",
    "http://e-bfk.co.kr/%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dyscrew.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://dyradi.com/%EC%98%A8%EB%9D%BC%EC%9D%B8%EB%AC%B8%EC%9D%98/write",
    "http://dynusu.com/%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dyt55.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://www.dyboiler.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dy04.net/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dy04.net/QnA/write",
    "http://dwnamecard.com/%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dwtreeart.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "https://dwtank.com/%EA%B3%A0%EA%B0%9D%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dw3579.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dwta.co.kr/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://duct04.net/%EC%98%A8%EB%9D%BC%EC%9D%B8%EB%AC%B8%EC%9D%98/write",
    "http://duckseung.com/board_4/write",
    "http://www.ducksanb.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://dslift.com/%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dssnap.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dsscience.co.kr/Q&A/write",
    "http://drone2626.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    
    "http://drmnf.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://ds5755.com/Q&A/write",
    "http://dresource.co.kr/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dreammeat.co.kr/%EC%9E%90%EB%A3%8C%EC%8B%A4/write",
    "http://dsglobal.net/23/write_form",
    "http://dsglass.kr/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dsdobi.kr/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://ds-boiler.com/QNA/write",
    "http://donmidam.co.kr/%EC%9D%B4%EC%9A%A9%ED%9B%84%EA%B8%B0/write",
    "http://donmidam.co.kr/%EC%98%A8%EB%9D%BC%EC%9D%B8%EB%AC%B8%EC%9D%98/write_form",
    "http://doosanfm.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://doshutter.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://doshutter.com/Q%EF%BC%86A/write",
    "http://ds-mc.co.kr/%EC%98%A8%EB%9D%BC%EC%9D%B8%EB%AC%B8%EC%9D%98/write_form",
    "http://dongsanawning.com/%EA%B2%AC%EC%A0%81%EB%AC%B8%EC%9D%98/write_form",
    
    "http://dongjins.net/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dongjineng.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dongjin8677.com/Free-Board/write",
    "http://dongho04.com/%EB%AC%BB%EA%B3%A0%EB%8B%B5%ED%95%98%EA%B8%B0/write",
    "http://dongbuex.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://dongbob.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://donga8433.com/%EA%B3%A0%EA%B0%9D%EC%84%BC%ED%84%B0/write",
    "http://gagusuri.kr/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://gagusuri.kr/%EC%A7%88%EB%AC%B8&%EB%8B%B5%EB%B3%80/write",
    "http://gaemiint.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://gaonsemiconductor.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://gaonsemiconductor.com/%EC%9E%90%EB%A3%8C%EC%8B%A4/write",
    "http://gagagallery.com/Notice/write",
    "http://gan-ho.co.kr/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://ahsung.biz/freeboard/write",
    "http://ganasts.com/%EC%9E%90%EC%9C%A0%EA%B2%8C%EC%8B%9C%ED%8C%90/write",
    "http://gasketpacking.com/Q&A/write",
    "http://gana-in.com/%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/write",
    "http://gana0429.com/%EC%9E%90%EB%A3%8C%EC%8B%A4/write",
]

fp = open("data/phone.json")
data = json.load(fp)
fp.close()

print (data)

driver = webdriver.Firefox()

for i,url in enumerate(urls):

    print ("###########################")
    print (url)
    driver.get(url)
    
    time.sleep(1)

    name_element = driver.find_element_by_xpath('//*[@id="tf_name"]')
    name_element.clear()
    name_element.send_keys(data["publisher"])

    pass_element = driver.find_element_by_xpath('//*[@id="tf_pwd"]')
    pass_element.clear()
    pass_element.send_keys("password")

    title_element = driver.find_element_by_xpath('//*[@id="tf_subject"]')
    title_element.clear()
    title_element.send_keys(data["subject"])

    try:
        # Switch to iframe
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

        content_element = driver.find_element_by_xpath('//body')
        if content_element:
            driver.execute_script("arguments[0].scrollIntoView();", content_element)
            content_element.click()            
            print ("IFRAME FOUND")
        time.sleep(0.3)
        content_element.send_keys(data["content"])

        # Switch to main page back
        driver.switch_to.default_content()
    except:
        print ("IFRAME NOT FOUND")
        content_element = driver.find_element_by_xpath('//textarea')
        content_element.clear()
        content_element.send_keys(data["content"])

    try:
        tag_element = driver.find_element_by_xpath('//*[@id="tf_tag"]')
        tag_element.clear()
        tag_element.send_keys(data["subject"].replace(" | ",","))
    except:
        pass

    ok_element = driver.find_element_by_xpath('//*[@type="submit"]')
    driver.execute_script("arguments[0].scrollIntoView();", ok_element)
    time.sleep(0.3)
    ok_element.click()

    time.sleep(3)

    try:
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
    except:
        pass


    