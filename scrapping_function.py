# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
# Windows users
def scrape_all():
executable_path ={'executable_path':'chromedriver.exe'}
Browser=Browser('chrome',**executable_path,headless=False)
news_title, news_paragraph = mars_news(browser)
def mars_news(Browser):
   # Visit the mars nasa news site
   url = 'https://mars.nasa.gov/news/'
   browser.visit(url)
   # Optional delay for loading the page
   browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')
   try:
    slide_elem = news_soup.select_one('ul.item_list li.slide')
    slide_elem.find("div", class_='content_title')
   # Use the parent element to find the first <a> tag and save it as  `news_title`
    news_title = slide_elem.find("div", class_='content_title').get_text()
   # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
   except AttributeError:
    return None, None
   return news_title, news_p
def featured_image(browser):
    try:
   # find the relative image url
   img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    except AttributeError:
       return None
def mars_facts():
    try:
      # use 'read_html" to scrape the facts table into a dataframe
      df = pd.read_html('http://space-facts.com/mars/')[0]
    except BaseException:
      return: None
    return df.to_html()
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())