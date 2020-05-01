'''
Parsing an XML file with ElementTree and saving the some data as CSV file

Two files will be created. One for the data with a 1:1 relationship and one for the
data with a 1:n relationship.

Exporting to CSV

https://www.datacamp.com/community/tutorials/python-xml-elementtree
http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-xml-to-csv-using-python/
'''
def search_xml_csv(f):
    tree = ET.parse(f)
    root = tree.getroot()
    csv_header = []
    csv_row = []
    nct_id = root.find('id_info/nct_id').text
    csv_header.append('nct_id')
    csv_row.append(nct_id)
    brief_title = root.find('brief_title').text
    csv_header.append('brief_title')
    csv_row.append(brief_title)

    # open a file for writing
    study_data = open('G:/projekte/studyexplorer/data/temp_info.csv', 'w', newline = '')

    # create the csv writer object
    csvwriter = csv.writer(study_data, delimiter = ',',  quotechar = '"', quoting=csv.QUOTE_ALL, lineterminator="\r\n")
    csvwriter.writerow(csv_header)
    csvwriter.writerow(csv_row)

    study_data.close()
    
    # open a file for writing
    study_data = open('G:/projekte/studyexplorer/data/temp_mesh.csv', 'w', newline = '')

    # create the csv writer object
    csvwriter = csv.writer(study_data, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_ALL, lineterminator="\r\n")
    csv_header = ['nct_id', 'param', 'value']
    csvwriter.writerow(csv_header)

    for elem in root.findall('intervention_browse/mesh_term'):
        mesh_term = elem.text
        csv_row = [nct_id, 'mesh_term', mesh_term]
        csvwriter.writerow(csv_row)
    
    study_data.close()


if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    import csv
    search_xml_csv('G:/projekte/studyexplorer/data/NCT0001xxxx/NCT00019994.xml')
