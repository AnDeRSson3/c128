from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("")
scraped_data=[]
stars_data=[]
def scrape():
    soup=BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table = soup.find("table", attrs={"class":"wikitable"})
    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = row.find_all("td")
        temp_list=[]
        print(table_cols)
        for col_data in table_cols:
            text=col_data.text.strip()
            print(text)
            temp_list.append(text)
    scraped_data.append(temp_list)

    

    for i in range(0,len(scraped_data)):
        Star_names= scraped_data[i][1]
        Distance=[i][3]
        Mass=[i][5]
        Radius=[i][6]
        Lum=[i][7]
        required_data = [Star_names, Distance, Mass, Radius, Lum]
        stars_data.append(required_data)


scrape()
headers = ["Star_name", "Distance", "Mass", "Radius", "Luminosity"]
star_df_1=pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")
        