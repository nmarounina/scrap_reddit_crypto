#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import streamlit as st

#read the main page first
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = "https://old.reddit.com/r/CryptoCurrency/new"
response=requests.get(url, headers=headers)

soup=BeautifulSoup(response.content, "lxml")

time.sleep(0.1)


# In[2]:


from datetime import datetime, timedelta

now=datetime.utcnow()
limit_time = now-timedelta(hours=5, minutes=0)
#limit_time_post=now-timedelta(days=2, hours=0, minutes=0)


# In[3]:


#Create a dictionnary to count the occurence of cryptocurrency names
f=open("list_cc_names.dat", "r")

dict_cc={}
for name in f:
    #print(name,name[0:-1], len(name))
    
    if len(name)>1:
        dict_cc[name[0:-1].lower()]=0
    


# In[4]:



#get the url of comments and creates a new soup object for the entire comment section

for comments_tag in soup.find_all("a", class_="bylink comments may-blank", href=True):

    url_comm = comments_tag['href']
    post_all=comments_tag.parent.parent.parent
    post_nb_of_comments=comments_tag.string


    #post_time=post_all.time["title"]
    #post_time_obj=datetime.strptime(post_time, "%a %b %d %H:%M:%S %Y %Z" )

    r_comm = requests.get(url_comm, headers=headers)
    soup_comm = BeautifulSoup(r_comm.text, "lxml")
    print(url_comm)
    print(post_nb_of_comments)
    print("\n")
    

    #Get the post text
    try :
        post_text=soup_comm.find("div", class_="expando").getText()

        for word in post_text.split():      
            if word.lower() in dict_cc:
                dict_cc[word.lower()]+=1
    except:
        print("#") #some posts have no text



    #Then, let's get all of the comments:
    comms_for_post=soup_comm.find_all("div", class_="entry unvoted")

    for commt in comms_for_post:

        try:

            time_string=commt.time["title"]
            time_obj=datetime.strptime(time_string, "%a %b %d %H:%M:%S %Y %Z" )

            if time_obj>limit_time:

                text=commt.find("div", class_="md").getText()
                #print(time_obj,text)

                for word in text.split() :#.string.split():

                    if word.lower() in dict_cc:
                        dict_cc[word.lower()]+=1


        except:
            print("*")
    time.sleep(.01)
    print("\n")


# In[5]:



newdict={}
for entry in dict_cc:
    if dict_cc[entry] != 0:
        
        print(entry,dict_cc[entry])
        newdict[entry]=dict_cc[entry]


# In[6]:


from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud


#colormaps that look good:
#"copper"
#BrBG
#PuOr
#twilight (little confusing tho)
wc = WordCloud(background_color="white",width=1000,height=1000, colormap="copper",
               relative_scaling=0.5,normalize_plurals=False, font_path='SFCompactRounded').generate_from_frequencies(dict_cc)
plt.imshow(wc)
plt.axis("off")


# In[9]:


# In[9]:


cloud=wc.to_file("./images/cloud.png")
image=Image.open("./images/cloud.png")
st.image(image,width=700)

plt.clf()
plt.figure(figsize=(30, 10))
plt.rcParams.update({"font.size": 40})
plt.xticks(rotation=45)
plt.bar(newdict.keys(), newdict.values(),color="brown", )
st.pyplot(plt)

# In[ ]:




