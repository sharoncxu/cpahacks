import re
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException

def login(driver):
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    email = driver.find_element_by_name('session_key')
    email.send_keys('13hy22@queensu.ca')
    password = driver.find_element_by_name('session_password')
    password.send_keys('OBFUSCATED')
    password.submit()

def scrapeProfile(driver,URL,dict):
    driver.get(URL)
    time.sleep(10)
    exp = driver.find_elements_by_xpath('//section[@id = "experience-section"]/ul//li//div//div//a//div[2]')
    print(exp)
    for item in exp:
        try:
            print(item.find_element_by_tag_name('h3').text)
        except NoSuchElementException:
            print("null")
        try:
            print(item.find_elements_by_tag_name('p')[1].text)
        except NoSuchElementException:
            print("null")
        try:
            print(item.find_element_by_xpath('.//div//h4//span[2]').text)
        except NoSuchElementException:
            print("null")
        try:
            print(item.find_element_by_xpath('./h4//span[2]').text)
        except NoSuchElementException:
            print("null")
        print("\n")
            
    # Loop through each company they worked at:
    #experience = driver.find_elements_by_class_name('pv-profile-section__card-item-v2')
    #print(len(experience))
    #for job in experience:
        #info = job.get_attribute('innerHTML')
        #company = re.search("(?<=<img alt=\")\w*", info)
        #job_title = re.search("(?<=<h3 class=\"t-16 t-black t-bold\">).*(?=<)", info)
        #start_date = re.search("(?<=<img alt=")\w*", info)
        #end_date = re.search("(?<=<img alt=")\w*", info)
        #print(company)
        #print(job_title)
    #dict["URL"].append(URL)
    # dict["Company"].append()
    #print(dict)

def main():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path="C:/Users/Huiyi/Desktop/chromedriver.exe", options=option)
    login(driver)
    user_data_dict = {"URL": [], "Company": [], "Job Title": [], "Start Period": [], "End Period": [], "Location": []}
    scrapeProfile(driver,"https://www.linkedin.com/in/peter-kachan-6641ab128/",user_data_dict)
    #print(pd.DataFrame.from_dict(user_data_dict))

main()
