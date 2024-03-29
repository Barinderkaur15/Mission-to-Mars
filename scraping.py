#!/usr/bin/env python
# coding: utf-8

def scrape_all():
    # In[1]:
    # Import Splinter and BeautifulSoup
    from splinter import Browser
    from bs4 import BeautifulSoup
    import pandas as pd

    # In[2]:
    # Windows users
    executable_path ={'executable_path':'chromedriver.exe'}
    Browser=Browser('chrome',**executable_path,headless=False)
    # In[3]:
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    Browser.visit(url)
    # Optional delay for loading the page
    Browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    # In[4]:
    html = Browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    slide_elem = news_soup.select_one('ul.item_list li.slide')
    # In[5]:
    slide_elem.find("div", class_='content_title')
    # In[6]:
    # Use the parent element to find the first `a` tag and save it as `news_title`
    news_title = slide_elem.find("div", class_='content_title').get_text()
    news_title
    # In[7]:
    # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
    news_p
    # "### Featured Images"
    # In[8]:
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    Browser.visit(url)
    # In[9]:
    # Find and click the full image button
    full_image_elem = Browser.find_by_id('full_image')
    full_image_elem.click()
    # In[10]:
    # Find the more info button and click that
    Browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = Browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    # In[11]:
    # Parse the resulting html with soup
    html = Browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    # In[12]:
    # Find the relative image url
    img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    img_url_rel
    # In[13]:
    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    img_url
    # In[14]:
    df = pd.read_html('http://space-facts.com/mars/')[0]
    df.columns=['description', 'value']
    df.set_index('description', inplace=True)
    df
    # In[15]:
    #to comnvert df into html
    df.to_html()
    # In[16]:
    Browser.quit()

    # return dictionary
    return name_of_dictionary