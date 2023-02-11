from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from bs4 import BeautifulSoup
import time


def get_url(search_term):
    """Generate a URL based on given search_term"""
    url = "https://www.amazon.com/s?k={}&crid=EQKLP450J60W&sprefix=protein+bars%2Caps%2C109&ref=nb_sb_noss_1"
    search_term = search_term.replace(' ', '+')
    url = url.format(search_term)
    url += '&page={}'
    return url


def extract_data(product):
    atag = product.h2.a
    product_title = atag.text.strip()
    product_url = 'https://www.amazon.com' + atag.get('href')
    parent_price_tag = product.find('span', 'a-price')
    try:
        product_price = parent_price_tag.find('span', 'a-offscreen').text.strip()
    except AttributeError:
        product_price = 'No Price Listed'
    try:
        product_review = product.i.text
        num_ratings = product.find('span', 'a-size-base s-underline-text').text
    except AttributeError:
        product_review = 'N/A'
        num_ratings = '0'
    result = (product_title, product_price, product_review, num_ratings, product_url)
    return result


def main(search_term):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    url = get_url(search_term)
    data = []
    for page in range(1,21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        products = soup.findAll('div', {'data-component-type': 's-search-result'})
        for product in products:
            data.append(extract_data(product))

    driver.close()
    with open('products.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Price', 'Rating', 'Rating Count', 'URL'])
        writer.writerows(data)

main('desk light')