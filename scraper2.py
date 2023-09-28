import selenium
import re
import os
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
#Url = "https://www.windguru.cz/279709"

def Web_scraping(Urlz):
    chrome_options = Options()
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urlz)
    assert "Windguru" in driver.title
    driver.implicitly_wait(15)
    for _ in range(5):
        element = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[2]/div[4]/div[1]/table/tbody/tr[2]/td/span')))
        element.click()
    parent_element = driver.find_element(By.XPATH, '/html/body/div[8]/div[2]/div[4]/div[1]/div[2]/table/tbody')
    day_elements = parent_element.find_elements(By.ID, 'tabid_0_0_dates')
    wind_elements = parent_element.find_elements(By.ID, 'tabid_0_0_WINDSPD')
    over_wind_elements = parent_element.find_elements(By.ID, 'tabid_0_0_GUST')
    titlez = driver.title
    return day_elements, wind_elements, over_wind_elements, titlez
    driver.quit()

def string_elements_clean_up(data):
    day_array_mid = []
    day_info = []
    day_array_mid = data.text.split(" ")
    for elements in day_array_mid:
        day_info.append(elements.replace("\n", ".").replace("..", "."))
    return day_info
    

def int_elements_clean_up(data):
    edited_string = data.text.replace(", ", "")
    input_array = []
    input_array = edited_string #minimalizuje kod i niechce mi sie go robic pieknym jeszcze bardziej  
    new_array = []
    for element in input_array:
        if not str(element).isspace():
            new_array.append(element)
            
    int_array = [int(value) for value in new_array]  

    return int_array

def Data_clean_up(URL):
    wind_normal = []
    wind_gust = []
    day_elements, wind_elements, over_wind_elements, titlez = Web_scraping(URL)
    title = titlez.replace("Windguru - ", "")
    day_info = string_elements_clean_up(day_elements[0])
    wind_normal = int_elements_clean_up(wind_elements[0])
    wind_gust = int_elements_clean_up(over_wind_elements[0])
    return day_info, wind_normal, wind_gust, title