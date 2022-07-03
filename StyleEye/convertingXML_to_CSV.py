from xml.etree import ElementTree as ET
from collections import defaultdict
from pathlib import Path
import csv
from pathlib import Path

directory = (r'C:\Users\sadiq\Desktop\StyleEye\xml')

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    headers = ['FinInstrmGnlAttrbts.Id','FinInstrmGnlAttrbts.FullNm','FinInstrmGnlAttrbts.ClssfctnTp','FinInstrmGnlAttrbts.CmmdtyDerivInd','FinInstrmGnlAttrbts.NtnlCcy','Issr']

    writer.writerow(headers)

    xml_files_list = list(map(str,Path(directory).glob('**/*.xml')))
    for xml_file in xml_files_list:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        start_nodes = root.findall('.//START')
        for sn in start_nodes:
            row = defaultdict(str)

            
            for k,v in sn.attrib.items():
                row[k] = v

            for rn in sn.findall('.//FinInstrmGnlAttrbts.Id'):
                row['FinInstrmGnlAttrbts.Id'] = rn.text

            for qu in sn.findall('.//FinInstrmGnlAttrbts.FullNm'):
                row['FinInstrmGnlAttrbts.FullNm'] = qu.text

            for ds in sn.findall('.//FinInstrmGnlAttrbts.ClssfctnTp'):
                row['FinInstrmGnlAttrbts.ClssfctnTp'] = ds.text
                
            for ds in sn.findall('.//FinInstrmGnlAttrbts.CmmdtyDerivInd'):
                row['FinInstrmGnlAttrbts.CmmdtyDerivInd'] = ds.text
                
            for ds in sn.findall('.//FinInstrmGnlAttrbts.NtnlCcy'):
                row['FinInstrmGnlAttrbts.NtnlCcy'] = ds.text
                
            for ds in sn.findall('.//Issr'):
                row['Issr'] = ds.text
                

            # all other tags except set data must be parsed before this.
            for st in sn.findall('.//Issr'):
               for k,v in st.attrib.items():
                   row['set_data_'+ str(k)] = v
               row_data = [row[i] for i in headers]
               writer.writerow(row_data)
               row = defaultdict(str)