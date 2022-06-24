import os
import base64
# from time import sleep
import time

from selenium.webdriver.chrome.options import Options
# from fake_useragent import UserAgent

from selenium.webdriver.common.by import By

WAIT_TIME = 200
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
driver.get("https://www.fender.com/en-US/mod-shop/mod-shop-stratocaster/0181900706.html")

time.sleep(10)
element = WebDriverWait(driver, WAIT_TIME).until (
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".close.popup-close"))
)
element.click()

time.sleep(60)
element = WebDriverWait(driver, WAIT_TIME).until (
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#fluidConfigure .fc-view-list:nth-child(1)"))
)
element.click()

time.sleep(30)
canvas_img = WebDriverWait(driver, WAIT_TIME).until (
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#fc-webgl-canvas")))

# canvas = driver.find_element_by_css_selector("canvas")
time.sleep(10)
canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas_img)
canvas_png = base64.b64decode(canvas_base64)
# save to a file
with open(r"FRONT-Color-Black.png", 'wb') as f:
    f.write(canvas_png)


time.sleep(3)
element = WebDriverWait(driver, WAIT_TIME).until (
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#fluidConfigure .fc-view-list:nth-child(2)"))
)
element.click()

time.sleep(10)
canvas_img = WebDriverWait(driver, WAIT_TIME).until (
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#fc-webgl-canvas")))

# canvas = driver.find_element_by_css_selector("canvas")
time.sleep(10)
canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas_img)
canvas_png = base64.b64decode(canvas_base64)
# save to a file
with open(r"BACK-Color-Black.png", 'wb') as f:
    f.write(canvas_png)

