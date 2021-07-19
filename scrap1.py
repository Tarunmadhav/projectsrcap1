from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
Start_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(Start_URL)
time.sleep(10)
def scrape():
    headers=["Name","designation","distance","spectler_class","Mass","Radius"]
    planetdata=[]
        
    with open("projectscrap/scrapper1.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)
scrape()

