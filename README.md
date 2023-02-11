# Amazon Webscraper

Amazon Product Webscraper that utilizes a mix of Selenium and BeautifulSoup. 


# Why?

I wanted to learn more about python webscraping and what I can do with it

# What you need

You **must** have Selenium and the web driver of your choice installed( I used Chrome).

Make sure to add the web driver to your $PATH

[Selenium Download](https://www.selenium.dev/documentation/webdriver/getting_started/)     

[Chrome Webdriver Download](https://chromedriver.chromium.org/downloads)



# How it works

Simply type main(<product_of_your_choice>) in the script and click run.

The webdriver will connect to the product URL on Amazon and will add 20 pages of data for each search result of that product. 

Data is in the format (product_title, product_price, product_review, num_of_reviews, product_url)

This data is stored in a .csv file that is created within the script for you.


