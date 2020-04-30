'''
Parsen eines XML-Dokuments mit ElementTree

https://www.datacamp.com/community/tutorials/python-xml-elementtree
'''
def search_xml(f, xs):
    tree = ET.parse(f)
    root = tree.getroot()
    res = []
    for elem in root.findall(xs):
        res.append(elem.text)
    return res


if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    res = search_xml('G:/projekte/studyexplorer/data/NCT00000102.xml', 'intervention_browse/mesh_term')
    for elem in res:
        print(elem)
