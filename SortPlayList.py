import os
import xml.etree.ElementTree as ET

import regex
from natsort import natsorted

base_dir = r'C:\Users\kevinz\Desktop\e-learning'
base_file = r'CSS - The Complete Guide (incl. Flexbox, Grid and Sass).smpl'


def getFile():
    file_path = os.path.join(base_dir, base_file)
    tree = ET.parse(file_path)
    root = tree.getroot()
    item_data = [item.attrib for item in root.iter('Item')]

    for item in natsorted(item_data, key=lambda x: regex.search('\d+\.\d+', x['Name']).group(0)):
        #print(item)
        ET.Element("Item", item)
    tree.write('temp.smpl')

if __name__ == "__main__":
    getFile()
