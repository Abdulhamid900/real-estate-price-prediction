from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def save_property_links():
    driver = webdriver.Chrome()
    driver.get('https://www.immoweb.be/en/search/apartment/for-sale?countries=BE')
    
    #cookie_button = driver.find_element(By.XPATH,"//button[@id='uc-btn-accept-banner']")
    #cookie_button.click()

    soup = BeautifulSoup(driver.page_source,'html.parser')
    listings = soup.find_all("a",class_="card__title-link")

    property_links = []
    for elem in soup.find_all("a",class_="card__title-link"):
        property_links.append(elem.get("href"))
    return property_links