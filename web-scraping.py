# THE TYPES OF APPS: SSR(SERVER SIDE RENDERED) APPS OR CSR(CLIENT SIDE RENDERED)

import requests # requests is a module that helps us communicate with servers from python.
from bs4 import BeautifulSoup as BS

# url = "https://jumia.com.ng/smartphones/"
# headers = requests.utils.default_headers()
# headers.update({
#     "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
# })
# my_response = requests.get(url, headers)
# print(my_response)
# print(my_response.status_code)
# first_soup = BS(my_response.content, features = "lxml")
# print(first_soup)
# second_soup = first_soup.find("div", attrs = {"class" : "-paxs row _no-g _4cl-3cm-shs"})
# list_of_soups = second_soup.find_all("article", {"class" : "prd _fb col c-prd"})
# print(list_of_soups)
# for soup in list_of_soups:
    # print(soup.prettify())
    # phone_details = soup.find("a")
    # try:
    #     phone_brand = phone_details.get("data-brand")
    #     print(phone_brand)
    # except:
    #     phone_brand = None

    # try:
    #     phone_description = phone_details.get("data-name")
    #     print(phone_description)
    # except:
    #     phone_description = None

    # try:
    #     old_div = soup.find("div", attrs = {"class" : "old"})
    #     phone_old_price = int((old_div.text).lstrip("₦ ").replace(",", ""))
    #     print(phone_old_price)
    # except:
    #     phone_old_price = None
    
    # try:
    #     new_div = soup.find("div", attrs = {"class": "prc"})
    #     phone_new_price = int((new_div.text).lstrip("₦ ").replace(",", ""))
    #     print(phone_new_price)
    # except:
    #     phone_new_price = None

    # try:
    #     discount = soup.find("div", attrs = {"class": "tag _dsct _sm"})
    #     disc = discount.text
    #     print(disc)
    # except:
    #     disc = None
    
    # try:
    #     rating = soup.find("div", attrs = {"class": "stars _s"})
    #     rating = (rating.text).strip(" out of 5")
    #     rate = float(rating)
    #     print(rate)
    # except:
    #     rating = None

    # break
