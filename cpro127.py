from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("D:\daksh_reddy\whjr\c127 web scraping\chromedriver")
browser.get(START_URL)
time.sleep(10)

headers = ["Name","Distance","Mass","Radius"]
stars_data = []

def scrape():
    
    for i in range(0,452):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for tr_tag in soup.find_all("tr",attrs = {"class","exoplanet"}):
            td_tags = tr_tag.find_all("td")

            temp_list = []
            for index,tr_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_tr_tag = td_tags[0]
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_tr_tag.find_all("a",href = True)[0]["href"])
            stars_data.append(temp_list)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)