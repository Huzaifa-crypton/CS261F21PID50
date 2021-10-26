from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
from selenium import webdriver
import random
from csv import writer

driver = webdriver.Chrome(executable_path=r'C:\Users\DR.NOOR KHAN\Week2\chromedriver.exe')
driver.get("https://www.peopleperhour.com/categories")
content = driver.page_source
soup = BeautifulSoup(content)
categoriesLinks = []
for a in soup.findAll('a' , attrs = {"class":"image-cards__link⤍Tiles⤚3Gn9j"}):
    categoriesLinks.append(a['href'])
categoriesLinks    

driver = webdriver.Chrome(executable_path=r'C:\Users\DR.NOOR KHAN\Week2\chromedriver.exe')
subCategoriesLinks = []
f = open("items.txt", "r")
serial = int(f.read())
f.close()
print(serial) 
# LOOP TO OPEN EACH CATEGORY
for j in range(6,len(categoriesLinks)):
    driver.get("https://www.peopleperhour.com"+categoriesLinks[j])
    content = driver.page_source
    soup = BeautifulSoup(content)
#     LOOP TO GET ALL THE SUBCATEGORY LINKS OF THE CURRENT CATEGORY
    for a in soup.findAll("a", attrs = {"class":"image-cards__link⤍Tiles⤚3Gn9j"}):
        subCategoriesLinks.append(a['href'])
#   loop to ITERATE THROUGH EACH SUBLINK
    for sublink in subCategoriesLinks:
        time.sleep(1)
        driver.get("https://www.peopleperhour.com"+sublink)
        content = driver.page_source
        soup = BeautifulSoup(content)
        try:
            category = soup.findAll("div",attrs = {"class":"small u-mgb--0 breadcrumbs__item⤍Breadcrumbs⤚Z550c breadcrumb__item⤍Breadcrumb⤚33GDg"})
            category = category[len(category)-1].text
        except:
            category = "Not Found"
        #       category  = soup.find("span",attrs = {"class":"related-categories__title--selected⤍RelatedCategories⤚1u799"}).text
        #       FINDING THE TOTAL PAGES OF THE SUBCATEGORY
        try:
            pgNumList = soup.find('ul',attrs = {"class":"pagination__list⤍SimplePagination⤚123NJ"})
            split_details = list(pgNumList.stripped_strings)
            subCategoryPages = int(split_details[len(split_details)-1])
        except:
            subCategoryPages = 1
        #       LOOP TO OPEN THE NEXT PAGES OF THE SUBCATEGORY
        for i in range(1 , subCategoryPages+1):
            with open('AllProjects.csv', 'a', newline='') as f_object:
                driver.get("https://www.peopleperhour.com"+sublink+"?exp=2&page="+str(i))
                url = "https://www.peopleperhour.com"+sublink+"?exp=2&page="+str(i)
                f = open("link.txt", "w")
                f.write(url)
                f.close()
                content = driver.page_source
                soup = BeautifulSoup(content)
                for a in soup.findAll('div',attrs = {"class":"card⤍HourlieTile⤚3DrJs"}):
                    try:
                        title = a.find("h2" , attrs = {"class":"title-nano card__title⤍HourlieTile⤚5LQtW"}).text.capitalize()
                    except:
                        title = "Not Found"
                    try:
                        name = a.find("span" , attrs={"class":"card__username⤍HourlieTileMeta⤚1hJNR"}).text.replace("&nbsp;" , "")
                    except:
                        name ="Not Found"
                    category = category
                    try:
                        delivery = a.find("span" , attrs={"class":"nano card__shipment⤍HourlieTile⤚AjgW3"}).span.text.replace("delivered in " , "")
                        delivery = delivery.replace(" day" , "").replace("s","")
                    except:
                        delivery = '0'
                    try:
                        cost = a.find('div',attrs = {"class":"u-txt--right card__price⤍HourlieTileMeta⤚3su1s"}).span.span.text.replace("$","")
                    except:
                        cost = 0
                    ratingsAndReviews = a.find('span',attrs = {"class":"card__freelancer-ratings⤍HourlieTileMeta⤚1zn5P"}).text.split()
                    if (len(ratingsAndReviews)!=0 ):
                        ratings = ratingsAndReviews[0]
                        reviews = ratingsAndReviews[1].replace("(","")
                        reviews = reviews.replace(")","")
                    else:
                        ratings = 0
                        reviews = 0
                        
                    list_data = [serial,title,category,name,cost,delivery,reviews,ratings]
                    print(serial,title , name , category , delivery , cost , ratings , reviews)
                    try:
                        writer_object = writer(f_object)
                        writer_object.writerow(list_data)
                        serial+=1
                        f = open("items.txt", "w")
                        f.write(str(serial))
                        f.close
                    except:
                        pass

            f_object.close()