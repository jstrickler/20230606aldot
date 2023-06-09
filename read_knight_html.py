import lxml.etree as et

doc = et.parse('knights.xml')

for knight in doc.findall('.//knight'):
    title = knight.get('title')
    name = knight.findtext('name')
    color = knight.findtext('color')
    print(f"{title:4s} {name:10s} {color}")