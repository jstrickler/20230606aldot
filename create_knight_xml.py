import lxml.etree as et

DATAFILE_PATH = "DATA/knights.txt"

def main():
    root = et.Element('knights')

    with open(DATAFILE_PATH) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight = et.SubElement(root, "knight", title=title)
            knight_color = et.SubElement(knight, "color")
            knight_color.text = color
            et.SubElement(knight, "quest").text = quest
            et.SubElement(knight, "comment").text = comment
            et.SubElement(knight, "name").text = name

    raw_xml = et.tostring(root, pretty_print=True, xml_declaration=True)
    xml_string = raw_xml.decode()
    print(xml_string)

    doc = et.ElementTree(root)
    doc.write("knights.xml", pretty_print=True, xml_declaration=True)



if __name__ == "__main__":
    main()