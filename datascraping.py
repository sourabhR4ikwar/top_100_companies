from bs4 import BeautifulSoup
import pandas as pd
import requests


df = pd.read_excel("Excel_Files/Data_from_statista.xlsx","Sheet1")
userAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
for x in range(0,len(df.index)):
    try:
        soup = BeautifulSoup(requests.get("https://www.google.com/search?q="+df.iloc[x, 0]+"+headquarters",headers=userAgent).text, "html.parser")
        headquarters = soup.find("div",{"class":"Z0LcW"}).get_text()
        soup = BeautifulSoup(requests.get("https://www.google.com/search?q="+headquarters+"+coordinates",headers=userAgent).text,"html.parser")
        location = soup.find("div", {"class":"Z0LcW"}).get_text()
        df.loc[x, "HeadQuarters"] = headquarters
        df.loc[x, "Location"] = location
        print(df.iloc[x, 0],"|",headquarters,"|", location)
        df.to_excel("Excel_Files/Output.xlsx")
    except AttributeError:
        pass
