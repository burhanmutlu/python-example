from xml.etree.ElementTree import tostring
from openpyxl import load_workbook
import pandas as pd
import xlsxwriter
import requests
from bs4 import BeautifulSoup

workbook = xlsxwriter.Workbook('bos.xlsx')
worksheet = workbook.add_worksheet()

for i in range(215):
    excel_data = pd.read_excel('linkler.xlsx',index_col=0)
    data = excel_data.index[i-1]
    url = data
    response = requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi,"html.parser")
    isim =soup.find_all("div",{"class":"product-description"})
    
    if (str(isim).count("<p>") <= 1 ):
        worksheet.write('B'+ str(i) , "aciklama yok veya az")
    i = int(i)
workbook.close()