import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from tomlkit import value
from bs4 import BeautifulSoup

def get_characteristics(property_url):
    driver = webdriver.Chrome()
    driver.get(property_url)
    #cookie_button = driver.find_element(By.XPATH, "//button[@id='uc-btn-accept-banner']")
    #cookie_button.click()
    path = "//script[@type='text/javascript' and (contains(text(), 'window.classified'))]"
    characteristics = driver.find_element(By.XPATH,path)
    inner_txt = characteristics.get_attribute('innerText')
    inner_txt = re.sub('window.classified =','',inner_txt) 
    inner_txt = re.sub(';','',inner_txt)
    parsed_json = json.loads(inner_txt)
    
    #characteristics of property
    dic = {}

    dic['location'] =parsed_json['property']['location']['locality']
    dic['type'] =parsed_json['property']['type']   
    dic['subtype'] = parsed_json['property']['subtype']
    dic['price'] = parsed_json['price']['mainDisplayPrice']
    dic['room'] = parsed_json['property']['bedroomCount']
    dic['living_area'] = 'None'
    dic['kitchen'] = parsed_json['property']['kitchen']['type']

    return dic