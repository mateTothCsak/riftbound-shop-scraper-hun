from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from data.scraperEnums import *

def main():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-agent=Mozilla/5.0 ... Chrome/120.0 Safari/537.36") # against bot detectors
    driver = webdriver.Chrome(options=options)
    

    #eg. Meta scraping
    driver.get(Shops.META.website + Shops.META.riftbound_path)
    print("Page title:", driver.title)
    
    # Example: extract something
    products =  driver.find_elements(By.CLASS_NAME, "webshop-list-item")
    for product in products:
        # we could also get the a href link to the product here
        innerBox = product.find_element(By.CLASS_NAME, "flex-column")
        
        name = innerBox.find_elements(By.TAG_NAME, "div")[0].find_element(By.TAG_NAME, "a").text
        availability = innerBox.find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "span")[1].text
        price = innerBox.find_elements(By.TAG_NAME, "div")[2].find_element(By.TAG_NAME, "h5").text
        print(name)
        print(availability)
        print(price)
    
    driver.quit()

if __name__ == "__main__":
    main()
