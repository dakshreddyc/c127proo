from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("D:\daksh_reddy\whjr\c127 web scraping\chromedriver")
browser.get(START_URL)
time.sleep(10)

headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude",
"discovery_date","hyperlink","planet_type","planet_radius","orbital_radius","eccentricity"]
planet_data = []

def scrape():
    
    for i in range(0,452):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs = {"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")

            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag = li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a",href = True)[0]["href"])
            planet_data.append(temp_list)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
   # with open("scraper.csv","w") as f:
        #csvwriter = csv.writer(f)
        #csvwriter.writerow(headers)
        #csvwriter.writerows(planet_data)

def scrape_more_data():
    pass

scrape()

for data in planet_data:
    scrape_more_data(data[5])
    with open("scraper.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

