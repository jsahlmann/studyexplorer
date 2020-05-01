'''
Parsing an XML file with ElementTree

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
    res = search_xml('G:/projekte/studyexplorer/data/NCT0001xxxx/NCT00019994.xml', 'intervention_browse/mesh_term')
    n = 0
    for elem in res:
        n += 1
        print(n, elem)
