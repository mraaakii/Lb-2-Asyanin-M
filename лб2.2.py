import xml.dom.minidom as minidom

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()
char_codes = []
values = []
elements = dom.getElementsByTagName('Valute')

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    char_code = child.firstChild.data
                    char_codes.append(char_code)

            if child.tagName == 'Value':
                if child.firstChild.nodeType == 3:
                    value = child.firstChild.data
                    values.append(value)
print(char_codes)
print(values)
xml_file.close()