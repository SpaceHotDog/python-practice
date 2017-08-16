#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup

__author__ = "Engine Bai"
url = "https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228"

driver = webdriver.Chrome(executable_path="./driver/chromedriver")
driver.get(url)
content_element = driver.find_element_by_class_name("postArticle-content")
content_html = content_element.get_attribute("innerHTML")

soup = BeautifulSoup(content_html, "html.parser")
p_tags = soup.find_all("p")
for p in p_tags:
    print(p.prettify())
driver.close()
