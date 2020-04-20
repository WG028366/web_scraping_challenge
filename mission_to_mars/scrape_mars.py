#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup
import time


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)


# In[4]:


html = browser.html
soup = bs(html, "html.parser")

time.sleep(10)

results = soup.body.find_all('div', class_= 'content_title')
news_title_list = []
for result in results:
    title = result.text
    news_title_list.append(title)
    
news_title = news_title_list[1]


# In[5]:


news_title


# In[6]:


results = soup.body.find_all('div', class_= 'article_teaser_body')
news_p_list = []
for result in results:
    p = result.text
    news_p_list.append(p)
time.sleep(10)
news_p = news_p_list[0]


# In[7]:


news_p


# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)


# In[9]:


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
soup = bs(html, "html.parser")


# In[ ]:





# In[ ]:





# In[10]:


time.sleep(10)
results = soup.body.find_all('a', class_='button fancybox')
for result in results:
        image = result.get('data-fancybox-href')   
        featured_image_url = "https://www.jpl.nasa.gov" + image


# In[11]:


featured_image_url


# In[ ]:





# In[12]:


# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
url = 'https://twitter.com/marswxreport?lang=en'


# In[13]:


browser.visit(url)
time.sleep(10)


# In[14]:


html = browser.html
soup = bs(html, 'html.parser')


# In[ ]:





# In[15]:


tweets = soup.find_all('div', class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")


# In[16]:


tweet_list = []

for tweet in tweets:
    weather = tweet.text
    tweet_list.append(weather)
    

mars_weather = tweet_list[0]
mars_weather


# In[ ]:





# In[17]:


# executable_path = {'executable_path': 'chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=False)
url = "https://space-facts.com/mars/"
browser.visit(url)
html = browser.html


# In[18]:


table = pd.read_html(url)
mars_facts = table[2]


# In[19]:


mars_facts


# In[20]:


mars_facts.to_html('mars_facts.html')


# In[ ]:





# In[21]:


url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)
html = browser.html
time.sleep(10)


# In[22]:


soup = bs(html, 'html.parser')
hemisphere_image_urls = []
root_url = 'https://astrogeology.usgs.gov'
#find links to go to individual hemisphere pages
hemispheres = soup.find_all('div', class_='item')


# In[ ]:





# In[23]:


#loop to reach each individual hemisphere page
for h in hemispheres:
    title = h.find('h3').text
    pre_img_url = h.find('a', class_='itemLink product-item')['href']
    browser.visit(root_url + pre_img_url)
    time.sleep(10)
    pre_img_html = browser.html
    soup = bs(pre_img_html, 'html.parser')
    #create a new result and loop for our newly visited page, pull link and append dictionary into list
    results =soup.find_all('div', class_='wide-image-wrapper')
    for r in results:
        img_url = root_url + r.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({'title': title, 'image url': img_url})
        


# In[ ]:





# In[ ]:





# In[ ]:




