import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time 
from datetime import date
import datetime

import pandas_datareader as pdr
import yfinance as yf

# Undertrading data  
end = date.today()
print(end)

import pandas_datareader.data as web 
start = datetime.datetime(2010,1,1)
end = datetime.datetime(2013,1,27)

gdp = web.DataReader('GDP','fred',start, end)
gdp.GDP/gdp.GDP.shift(4)-1  

#Inflation 
cpi = web.DataReader('CPILFESL','fred', start)
cpi.head()

#OTRA FORMAA D TRAER DATOS MAS FINANCIEROS
spx = pdr.get_data_stooq('^SPX') #Research on internet 
spx.head()
spx['shift1'] = spx['Close']/spx['Close'].shift(-1)-1 #Expresa la volatilidad 

spx.columns
spx = spx.reset_index()
datetime.datetime.strftime() #there is a error  AQUI

#que es estacionario o no y que es estocastico o no?


#Phyton cursour (como bajar daos y scraper)

#pague to scrape

#Scrape sacrapear data (acceder a la pagina y saar datos) 200 queremos
 #Install librari to make a scrape 
url = "https://tradingeconomics.com/united-states/indicators"
print(url)
#Make requests
import requests
requests.get(url)
#call an agent (inspect)

import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
response = requests.get(url,headers=headers)

if response.status_code == 200: #(debugger)
  print("OK")
  soup = BeautifulSoup(response.content,"html.parser")
  table_div = soup.find("div", classs_="tab-content")  #tab-content
  table = table_div.find("table")
  
  df =pd.read_html(str(table))[0]
  print(df)
  df.to_cvs("data.cvs", index = False)

else:
    print("Falled")