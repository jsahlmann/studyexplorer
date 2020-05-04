'''
Transforming all xml files in one folder into html files 
using an xsl file


https://stackoverflow.com/questions/16698935/how-to-transform-an-xml-file-using-xslt-in-python
'''

import os
import lxml.etree as ET

inputpath = "G:/projekte/studyexplorer/xml_in/"
xsltfile = "G:/projekte/studyexplorer/xsl/ctg_single.xsl"
outpath = "G:/projekte/studyexplorer/xml_out/"


for dirpath, dirnames, filenames in os.walk(inputpath):
            for filename in filenames:
                if filename.endswith(('.xml', '.txt')):
                    dom = ET.parse(inputpath + filename)
                    xslt = ET.parse(xsltfile)
                    transform = ET.XSLT(xslt)
                    newdom = transform(dom)
                    infile = ET.tostring(newdom, pretty_print=True).decode("utf-8")
                    outfilename = filename.replace('.xml', '.html')
                    outfile = open(outpath + "/" + outfilename, 'w')
                    outfile.write(infile)
                    outfile.close()