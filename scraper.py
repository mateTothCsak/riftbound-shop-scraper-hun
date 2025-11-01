from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def main():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://webscraper.io/test-sites/e-commerce/allinone")
    print("Page title:", driver.title)
    
    # Example: extract something
    # content = driver.find_element("css selector", "h1").text
    # print(content)
    
    driver.quit()

if __name__ == "__main__":
    main()
