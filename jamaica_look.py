# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 09:28:45 2022

@author: RONNY
"""
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import time 
from bs4 import BeautifulSoup
import pandas as pd
ser=Service("E:\\scrapers\geckodriver")
op=webdriver.FirefoxOptions()
driver=webdriver.Firefox(service=ser,options=op)

keyword="Jamaica producers"

def start_request(keyword,p):
    driver.get(f"https://jamaica.loopnews.com/search-results/search?keys={keyword}&domain=All&sort_by=created&sort_order=DESC&page={p}")
    soup = BeautifulSoup(driver.page_source, 'lxml')
    data = soup.select('.block-system-main-block')
    links = []
    for i in data:
        url = i.select('p')
        for u in url:
            url2 = u.findAll('a')
            for j in url2:
                url3 = j.get('href')
                url4 = 'https://jamaica.loopnews.com' + url3
                if url4 not in links:
                    links.append(url4)
    
    parse_pages(links)

def parse_pages(links):
    for u in links:
        driver.get(u)
        driver.execute_script("window.scrollTo(0, document.body.Height);")
        time.sleep(1)
        soup=BeautifulSoup(driver.page_source, 'lxml')
        article_db={"Date":[],"Title":[], "Content":[]}
        
        date_created=soup.select_one('span.auther-dte').text
        title=soup.select_one('h1').text
        content=[]
        cont=soup.select('.article-description')
        for i in cont:
            block=i.findAll('p')
            for p in block:
                block2=p.text
                content.append(block2)
        
        article_db["Date"].append(date_created)

        article_db["Title"].append(title)
        article_db["Content"].append(content)
        article_db=pd.DataFrame(article_db)    
        article_db.to_csv(f"E:/clients/alade/jamaicaLoop/LoopData/{keyword}.csv", mode='a', index=False, header=False)


def main():
    for p in range(0,62):
        start_request(keyword,p)
        

    

if __name__ == "__main__":
    main()
