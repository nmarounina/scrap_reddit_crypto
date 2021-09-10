# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = "https://www.reddit.com/r/CryptoCurrency/"
response=requests.get(url, headers=headers)




soup=BeautifulSoup(response.content, "lxml")

#print(soup.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())


for item in soup.select(".Post"):
    try:
        print("----------------------------------------")
        print(item.select("._3jOxDPIQ0KaOWpzvSQo-1s")[0].get_text())
        print(item.select("._eYtD2XCVieq6emjKBH3m")[0].get_text())
        print(item.select(".FHCV02u6Cp2zYL0fhQPsO")[0].get_text())
        url2=item.select("._2INHSNB8V5eaWp4P0rY_mE a[href]")[0]['href']
        response2=requests.get(url, headers=headers)
        

    except Exception as e:
        #raise e
        print("")
        

print("\n")
print("\n")
#print( soup.get_text() )
