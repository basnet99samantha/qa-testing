import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url_location = 'URL_List.xlsx'


def read_excel():
    reader = pd.read_excel(url_location)
    for row, column in reader.iterrows():
        url = column["URL"]
        site = column["Site Name"]
        sn = column["SN"]
        print(sn, site, url)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(url)
        try:
            assert site in driver.title
        except AssertionError:
            print("Title don't match")
        else:
            print("Title matched")


if __name__ == '__main__':
    read_excel()
