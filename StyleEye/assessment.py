import requests
import xml.etree.ElementTree as ET


response = requests.get('https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100')
root = ET.fromstring(response.text)
for i in root.findall('result'):
    for j in i.findall('doc'):
        for k in j:
            link = j.find('.//str[@name="download_link"]').text
            print(link)
            req = requests.get(link)
            with open('.xml', 'wb') as file:
             file.write(response.content)
             file.close()