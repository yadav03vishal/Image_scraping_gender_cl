
from selenium import webdriver
import urllib.request
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.myntra.com/men-tshirts')
# driver.get('https://www.myntra.com/tshirts?f=Gender%3Amen%20women%2Cwomen')


body = driver.find_element(By.CSS_SELECTOR, 'body')
for _ in range(20):  
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  


product_elements = driver.find_elements(By.CSS_SELECTOR, "img.img-responsive")


if not os.path.exists('myntra_images'):
    os.makedirs('myntra_images')


for i, product in enumerate(product_elements):
    image_url = product.get_attribute('src')
    print(image_url)
    image_path = os.path.join('myntra_images', f'men_image_{i}.jpg')
    urllib.request.urlretrieve(image_url, image_path)

driver.close()
driver.quit()
