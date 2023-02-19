# Import the necessary libraries
import re
import json
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Define a function to extract the characteristics from a property URL
def get_characteristics(property_url):
    driver = webdriver.Chrome()
    driver.get(property_url)

    # Define an XPath expression to find the script tag containing the characteristics JSON
    path = "//script[@type='text/javascript' and (contains(text(), 'window.classified'))]"
    
    # Find the script tag using the XPath expression
    characteristics = driver.find_element(By.XPATH, path)
    
    # Extract the inner text of the script tag
    inner_txt = characteristics.get_attribute('innerText')
   
    # Remove some extra text from the inner text
    inner_txt = re.sub('window.classified =', '', inner_txt)
    inner_txt = re.sub(';', '', inner_txt)

    # Extract the JSON text using regex
    match = re.search(r'({.*})', inner_txt)
   
    # If the JSON text was found extract characteristics
    if match:
        json_text = match.group(1)
        parsed_json = json.loads(json_text)
        location = parsed_json['property']['location']['province']
        post_code = parsed_json['property']['location']['postalCode']
        property_type = parsed_json['property']['type']
        price = parsed_json['price']['mainDisplayPrice']
        room_count = parsed_json['property']['bedroomCount']
        heat = parsed_json['property']['energy']['heatingType']
        
        # Store the characteristics in dictionary
        characteristics_dict = {
            'location': location,
            'type': property_type,
            'price': price,
            'room': room_count,
            'zip':post_code,
            'heattype':heat
        }
        return characteristics_dict
    
    # If the JSON text was not found, print a message and return None
    else:
        print(f"JSON not found for URL: {property_url}")
        return None

# Open input CSV file for reading and the output CSV file for writing
with open('input.csv', 'r') as input_file, open('output.csv', 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Iterate over each row in the input file and extract the property URL from the row
    for row in reader:
        url = row[0]
        try:
            characteristics = get_characteristics(url)

            # If characteristics successfully extract write to output file
            if characteristics:
                writer.writerow([characteristics['location'], characteristics['type'], characteristics['price'], characteristics['room'], characteristics['zip'], characteristics['heattype']])
        
        # If exception print error message and continue
        except Exception as e:
            print(f"Failed to process URL: {url} ({str(e)})")
            continue
