import xml.etree.ElementTree as ET

def indent(elem, level=0):
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        for child in elem:
            indent(child, level+1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i
    return elem

def export_to_xml(df, output_path):
    root = ET.Element('movies')

    for _, row in df.iterrows():
        movie_elem = ET.SubElement(root, 'movie')
        for col in df.columns:
            child = ET.SubElement(movie_elem, col)
            child.text = str(row[col])

    root = indent(root)
    tree = ET.ElementTree(root)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
