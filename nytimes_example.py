import requests
import xml.etree.ElementTree as ET


url = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"

r = requests.get(url) 

if r.status_code == 200:
    root = ET.fromstring(r.content)

    lista_title_desc = []

    for channel in root:
        children = channel.findall('item')
        for item in children:
            title = item.find('title') 
            descrip = item.find('description')
            lista_title_desc.append((title.text, descrip.text))

    for headline in lista_title_desc:
        print(headline[0],headline[1], end='\n\n',sep='\n\n')