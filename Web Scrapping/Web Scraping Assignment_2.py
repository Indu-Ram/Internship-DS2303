#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install selenium


# In[ ]:


#Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You 
have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 
jobs data


# In[ ]:





# In[50]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[83]:


driver=webdriver.Chrome(r'Chromedriver.exe')


# In[53]:


driver.get("https://www.naukri.com/")


# In[54]:


# Entering designation and location as required in the question:
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys("Data Analyst")


# In[55]:


Location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
Location.send_keys('Bangalore')


# In[56]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[66]:


# scrapping Job Title from the given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[62]:


# scraping Job Location from the given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    


# In[63]:


#scraping Company name from the given page
company_tags=driver.find_elements(By.XPATH,"//a[@class='subTitle ellipsis fleft']")
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
            


# In[75]:


exp_tags=driver.find_elements("xpath",'//li[@class="fleft grey-text br2 placeHolderLi experience"]')

for i in exp_tags[0:10]:
    job_exp.append(i.text)
    job_exp.append(experience)


# In[76]:


print(len(job_title),len(job_location),len(company_name),len(job_exp))


# In[79]:


import pandas as pd
df=pd.DataFrame({'Title':job_title[:10],'Location':job_location[:10],'Company Name':company_name[:10]})
df


# In[ ]:


#Q2.:Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You 
have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.


# In[17]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[20]:


#Opening the naukri page on automated chrome browser
driver.get('https://www.naukri.com/')


# In[21]:


# Entering designation and location as required in the question:
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys("Data Scientist")


# In[22]:


Location=driver.find_element(By.XPATH,"//html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
Location.send_keys('Bangalore')


# In[23]:


#Making empty list
job_title=[]
job_location=[]
company_name=[]


# In[24]:


# scrapping Job Title from the given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[ ]:





# In[25]:


# scraping Job Location from the given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    


# In[40]:


#scraping Company name from the given page
company_tags=driver.find_elements(By.XPATH,"//a[@class='subTitle ellipsis fleft']")
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[42]:


print(len(job_title),len(job_location),len(company_tags))


# In[80]:


import pandas as pd
import numpy as np
df2=pd.DataFrame ({'Title':job_title,'Location':job_location,'Company Name':company_tags[:10]})
df2


# In[ ]:


#Q3.


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[3]:


driver=webdriver.Chrome(r'Chromedriver.exe')


# In[5]:


#Opening the naukri page on automated chrome browser
driver.get('https://www.naukri.com/')


# In[7]:


# Entering designation and location as required in the question:
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys("Data Scientist")


# In[13]:


Location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
Location.send_keys('Delhi/NCR')


# In[14]:


# Let us perforem search operation.
search = driver.find_element(By.CLASS_NAME, "qsbSubmit")
search.click()


# In[10]:


# scraping Job Location from the given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    


# In[11]:


# scrapping Job Title from the given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[126]:


sal_3=driver.find_elements("xpath",'//li[@class="fleft grey-text br2 placeHolderLi salary"]')
salary_3=[]
for i in sal_3:
    salary_3.append(i.text)


# In[136]:


loc_tags3=driver.find_elements("xpath",'//li[@class="fleft grey-text br2 placeHolderLi location"]')
job_location=[]
for i in loc_tags3:
    job_location.append(i.text) 


# In[133]:


company = driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
company_name = []
for i in company:
    company_name.append(i.text)


# In[15]:


print(len(job_title),len(job_location),len(company_tags))


# In[134]:


import pandas as pd
df=pd.DataFrame({'Title':job_title[:10],'Location':job_location[:10],'Company Name':company_name[:10],'Salary':salary_3[:10]})
df


# In[ ]:


#Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
1. Brand
2. ProductDescription
3. Price


# In[138]:


url='https://www.flipkart.com/'
driver.get(url)


# In[141]:


#Enter sunglasses in search icon.
search=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search.send_keys('sunglasses')


# In[142]:


click=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
click.click()


# In[143]:


page_url = [] # a list containg url's of every page
url = driver.find_elements(By.XPATH,"//nav[@class='yFHi8N']//a")
for i in url:
    page_url.append(i.get_attribute('href'))
    
name=[]
des=[]
price=[]

for i in page_url[:3]:
    driver.get(i)
    title=driver.find_elements(By.CLASS_NAME,"_2WkVRV")
    for i in title:
         name.append(i.text)
            
    desc=driver.find_elements(By.CLASS_NAME,'IRpwTa')
    for i in desc:
        des.append(i.text)
        
    amount=driver.find_elements(By.CLASS_NAME,'_30jeq3')
    for i in amount:
            price.append(i.text)


# In[144]:


name=name[:100]
des=des[:100]
price=price[:100]

df3=pd.DataFrame({'Name':name,'Description':des,'Price':price})
df3


# In[ ]:


#Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: 
https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market 
place=FLIPKART


# In[145]:


url='https://www.flipkart.com/apple-iphone-11-black-64-gb-includes-earpods-power-adapter/product-reviews/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKCTSVZAXUHGREPBFGI&marketplace=FLIPKART'
driver.get(url)


# In[146]:


all_reviews=driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div/div')
all_reviews.click()


# In[147]:


page_url = [] # a list containg url's of every page
url = driver.find_elements(By.XPATH, "//nav[@class='yFHi8N']//a")
for i in url:
    page_url.append(i.get_attribute('href'))

len(page_url)


# In[148]:


rating=[]
review=[]
fullre=[]
for i in page_url:
    driver.get(i)
    rate=driver.find_elements(By.XPATH, '//div[@class="_3LWZlK _1BLPMq"]')
    for i in rate:
        rating.append(i.text)
    rev=driver.find_elements(By.CLASS_NAME, "_2-N8zT")
    for i in rev:
        review.append(i.text)
    fr=driver.find_elements(By.CLASS_NAME, "t-ZTKy")
    for i in fr:
        fullre.append(i.text)


# In[149]:


rating=rating[:100]
review=review[:100]
fullre=fullre[:100]

df4=pd.DataFrame({'Rating':rating,'Review Summary':review,'Full Review':fullre})
df4


# In[ ]:


#Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the 
search field.
You have to scrape 3 attributes of each sneaker:
1. Brand
2. ProductDescription
3. Price
As shown in the below image, you have to scrape the above attributes.


# In[152]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[156]:


driver=webdriver.Chrome(r'Chromedriver.exe')


# In[158]:



driver.get('https://www.flipkart.com/')
search=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search.send_keys('sneakers')


# In[161]:


click=driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
click.click()


# In[162]:


page_url = [] # a list containg url's of every page
url = driver.find_elements(By.XPATH, "//nav[@class='yFHi8N']//a")
for i in url:
    page_url.append(i.get_attribute('href'))
    
name=[]
des=[]
price=[]

for i in page_url[:3]:
    driver.get(i)
    title=driver.find_elements(By.CLASS_NAME,"_2WkVRV")
    for i in title:
         name.append(i.text)
            
    desc=driver.find_elements(By.CLASS_NAME,'IRpwTa' or 'IRpwTa _2-ICcC')
    for i in desc:
        des.append(i.text)
        
    amount=driver.find_elements(By.CLASS_NAME,'_30jeq3')
    for i in amount:
        price.append(i.text)
        
        
name=name[:100]
des=des[:100]
price=price[:100]

df5=pd.DataFrame({'Name':name,'Description':des,'Price':price})
df5


# In[ ]:


#Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then 
set CPU Type filter to “Intel Core i7” as shown in the below image:


# In[163]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[164]:


driver.get("https://www.amazon.in/")


# In[165]:


Laptop = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
Laptop.send_keys('Laptop')


# In[166]:


search=driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search.click()


# In[173]:


rating=[]
rat=driver.find_elements(By.XPATH, '//a[@class="a-popover-trigger a-declarative"]')
for i in rat:
    rating.append(i.text)
rating=rating[0:10]    


# In[174]:


title=[]
tle=driver.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in tle:
    title.append(i.text) 
title=title[0:10] 


# In[175]:


price=[]
pre=driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
for i in pre:
    price.append(i.text) 
price=price[0:10]   


# In[176]:


df6=pd.DataFrame({'Rating':rating,'Title':title,'Price':price})
df6


# In[ ]:


#Q8: Write a python program to scrape data for Top 1000 Quotes of All Time.
The above task will be done in following steps:
1. First get the webpagehttps://www.azquotes.com
2. Click on TopQuot
3.Than scrap a)Quote b)Author c)Types of quotes


# In[177]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[ ]:





# In[178]:


driver.get("https://www.azquotes.com/")


# In[180]:


Top_Quotes =driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
Top_Quotes.click()


# In[181]:


quotes=[]
qte=driver.find_elements(By.XPATH, '//a[@class="title"]')
for i in qte:
    quotes.append(i.text)
quotes=quotes[0:100]  


# In[182]:


Author=[]
atr=driver.find_elements(By.XPATH, '//div[@class="author"]')
for i in atr:
    Author.append(i.text)
Author=Author[0:100]   


# In[183]:


Type=[]
typ=driver.find_elements(By.XPATH, '//div[@class="tags"]')
for i in typ:
    Type.append(i.text)
Type=Type[0:100]   


# In[184]:


df7=pd.DataFrame({'Quotes':quotes,'Author':Author,'Type_Of_Quotes':Type})
df7


# In[ ]:


#Q9: Write a python program to display list of respected former Prime Ministers of India(i.e. Name, Born-Dead, 
Term of office, Remarks) from https://www.jagranjosh.com/.
This task will be done in following steps:
1. First get the webpagehttps://www.jagranjosh.com/
2. Then You have to click on the GK option
3. Then click on the List of all Prime Ministers of India
4. Then scrap the mentioned data and make theDataFrame


# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[2]:


driver=webdriver.Chrome(r'Chromedriver.exe')


# In[3]:


driver.get("https://www.jagranjosh.com/")


# In[5]:


GK =driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[5]/div/div[1]/header/div[2]/ul/li[2]/div/a[6]')


# In[9]:


PM =driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[10]/div/div/ul/li[2]/a')


# In[42]:


Name=[]
nme=driver.find_elements(By.XPATH, '//td[@style="width: 150px; height: 80px;"]')
for i in nme:
    Name.append(i.text)
Name=Name[:]  


# In[43]:


Born_Dead=[]
bd=driver.find_elements(By.XPATH, '//td[@style="width: 105px; height: 80px;"]')
for i in bd:
    Born_Dead.append(i.text)
Born_Dead=Born_Dead[:] 


# In[28]:


df9=pd.DataFrame({'Name':Name, 'Born_Dead':Born_Dead})
df9


# In[ ]:


#Q10: Write a python program to display list of 50 Most expensive cars in the world (i.e. 
Car name and Price) from https://www.motor1.com/
This task will be done in following steps:
1. First get the webpagehttps://www.motor1.com/
2. Then You have to click on the List option from Dropdown menu on leftside.
3. Then click on 50 most expensive carsin the world..
4. Then scrap the mentioned data and make the dataframe


# In[10]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[11]:


driver.get("https:www.motor1.com")


# In[12]:


List =driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div[1]/div')
List.click()


# In[15]:


another =driver.find_element(By.XPATH, '/html/body/div[3]/div[5]')
another.click()


# In[16]:


Name=[]
nme=driver.find_elements(By.XPATH, '//h3[@class="subheader"]')
for i in nme:
    Name.append(i.text)
Name=Name[:] 


# In[17]:


df8=pd.DataFrame({'Name':Name})
df8


# In[ ]:




