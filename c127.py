from selenium import webdriver
from bs4 import BeautifulSoup as BS
import time
import csv

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome('/Users/visheshv/Downloads/C127/chromedriver')
browser.get(start_url)
time.sleep(10)

def scraper():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar magnitude", "discovery_date"]
    planet_data = []
    for i in range(0,2):
        soup = BS(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs= {"class", "exoplanets"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

                print(headers)
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    
    with open('scraper.csv', 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(planet_data)

scraper()

    