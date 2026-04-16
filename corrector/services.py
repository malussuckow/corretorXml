import xml.etree.ElementTree as ET

#def ler_arquivoXml():
tree = ET.parse('testexml/Conceitual_1.xml')
root = tree.getroot()
#print(root.tag)
#print(root.attrib)
for elem in root:
    print(elem.tag, elem.attrib)






if __name__ == "__main__":    ler_arquivoXml()