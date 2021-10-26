from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import random
from csv import writer

driver = webdriver.Chrome(executable_path=r'C:\Users\DR.NOOR KHAN\Week2\chromedriver.exe')
driver.get("https://www.taskrabbit.com/services")
content = driver.page_source
soup = BeautifulSoup(content)

# GETTTING ALL THE CATEGORIES LINKS
allLinks = []
for a in soup.findAll("div" , attrs={"class":"mg-panel__content"}):
    links = a.findAll("li",attrs = {"class":"mg-panel__template-item"})
    for b in links:
        link = b.a["href"]
        allLinks.append(link)

# MAIN SCRAPING PROCESS BEGINS
f = open("items.txt", "r")
serial = int(f.read())
f.close()
print(serial)
f = open("link.txt", "r")
linkNo = int(f.read())
print(linkNo)
f.close()

for url in range(linkNo , len(allLinks)):
    driver.get("https://www.taskrabbit.com"+allLinks[url])
    f = open("items.txt", "w")
    with open('AllProjects.csv', 'a', newline='') as f_object:
        for i in range(1,4):
            time.sleep(2)
            content = driver.page_source
            soup = BeautifulSoup(content)
            c = 1
            for a in soup.findAll("div",attrs = {"class":"task-template__category-taskers-card"}):
                if c < 4 :
                    list_data = []
                    name = a.find("span",attrs = {"class":"task-template__category-taskers-display-name"}).text
                    cost = a.find("span",attrs = {"class":"task-template__category-taskers-rate-display"}).text
                    cost = cost.replace("$" , "")
                    cost = cost.replace("/hr" , "")
                    title = a.find("div",attrs = {"class":"task-template__category-taskers-description-body-mobile"}).text
                    category = soup.find("div",attrs = {"class":"task-template-landing-page__hero__box"}).h1.text
                    reviews = random.randint(0, 500)
                    ratings = round(random.randint(0, 5)+random.random() , 1)
                    delivery = random.randint(1, 10)
                    list_data = [serial,title,category,name,cost,delivery,reviews,ratings]
                    print(list_data)
                    try:
                        writer_object = writer(f_object)
                        writer_object.writerow(list_data)
                        serial+=1
                        f = open("items.txt", "w")
                        f.write(str(serial))
                        f.close


                    except:
                        pass
                    c+=1
            try:
#               HELPS TO PRESS THE NEXT BUTTON
                driver.find_element_by_css_selector('#category_taskers_carousel > div > div:nth-child(2) > div > button.rotating_carousel_navigate--next.task-template__category-taskers-carousel__navigate--next').click()
            except:
                pass
    f_object.close()

    linkNo+=1
    l = open("link.txt", "w")
    l.write(str(linkNo))
    l.close