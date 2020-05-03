'''

'''

import os
import lxml.etree as ET

inputpath = "G:/projekte/studyexplorer/xml_in/"
xsltfile = "G:/projekte/studyexplorer/xsl/test2.xsl"
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