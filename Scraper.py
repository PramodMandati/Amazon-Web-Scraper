import selenium
import bs4
import requests
from selenium import webdriver


def scrape_this_url():
    global driver
    div=driver.find_element_by_css_selector('div.s-result-list.s-search-results.sg-row')
    div2=div.find_elements_by_css_selector('div.sg-col-20-of-24.s-result-item.sg-col-0-of-12.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-12-of-16.sg-col-24-of-28')
    with open('c:/users/anile/desktop/Scraper.txt','a') as f:
        for i in div2:
            try:
                #price_div=i.find_element_by_css_selector('a.a-size-base.a-link-normal.s-no-hover.a-text-normal')
                price_div=i.find_element_by_class_name('a-price')
                product_name=i.find_element_by_tag_name('h2')
                f.write(product_name.text+' ---- '+'Rs.'+price_div.text.split('\n')[0][1:])
                f.write('\n\n')
            except Exception as e:  
                pass
       
            


url=input('enter the first page url to scrape:\n')
pages=int(input('enter the no.of pages to scrape:\n'))

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
options.add_argument('--silent')
options.add_argument('--log-level=OFF')
options.add_argument('no-sandbox')

driver = webdriver.Chrome(r"E:\Projects\Python\Amazon\Chrome\chromedriver_win32\chromedriver.exe",options=options)




while pages>0:
    driver.get(url)
    btn2=driver.find_element_by_class_name('a-pagination')
    btn3=btn2.find_elements_by_tag_name('li')
    page_break=False
    page_url=None
    scrape_this_url()
    for i in btn3:
        try:
            if i.get_attribute('class')=='a-selected':
                page_break=True
                continue
            if page_break:
                url_div=i.find_element_by_tag_name('a')
                url=url_div.get_attribute('href')
                pages-=1
                break
        except:
            print('error')

print('done!')
driver.quit()
#https://www.amazon.in/s?k=laptop&ref=nb_sb_noss



