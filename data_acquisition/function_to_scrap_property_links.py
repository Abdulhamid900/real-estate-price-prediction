# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv

# Define a function to save property links
def save_property_links():
    driver = webdriver.Chrome()
    
    #creat list to save the links and for loop over pages to get links
    property_links = []
    for page_num in range(1, 300):
        url = f'https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&page={page_num}'
        driver.get(url)
        # Close the cookie banner if it exists
        try:
            cookie_button = driver.find_element(By.XPATH, "//button[@id='uc-btn-accept-banner']")
            cookie_button.click()
        except:
            pass

        # Parse html source of the current page using Beautiful Soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all property listing on current page
        listings = soup.find_all("a",class_="card__title-link")

        # Loop through each listing and extract URL of property 
        for elem in soup.find_all("a",class_="card__title-link"):
            property_links.append(elem.get("href"))

    # Save the property links to CSV file
    with open('property_links.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Link'])
        for link in property_links:
            writer.writerow([link])
    return property_links
