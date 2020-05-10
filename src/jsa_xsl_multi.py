'''
Transforming all xml files in one folder into html files 
using an xsl file.

One html file per xml file.

https://stackoverflow.com/questions/16698935/how-to-transform-an-xml-file-using-xslt-in-python
'''

import os
import lxml.etree as ET

inputpath = "G:/projekte/studyexplorer/xml_in/"
xsltfile = "G:/projekte/studyexplorer/xsl/ctg_multi.xsl"
outpath = "G:/projekte/studyexplorer/xml_out/"


outfilename = "allitems.html"
outfile = open(outpath + '/' + outfilename, 'w', newline = '')
outfile.write("var1, var2, var3")
for dirpath, dirnames, filenames in os.walk(inputpath):
            for filename in filenames:
                if filename.endswith(('.xml')):
                    dom = ET.parse(inputpath + filename)
                    xslt = ET.parse(xsltfile)
                    transform = ET.XSLT(xslt)
                    newdom = transform(dom)
                    infile = ET.tostring(newdom, pretty_print=True).decode("utf-8")
                    outfile.write(infile)
outfile.close()                    