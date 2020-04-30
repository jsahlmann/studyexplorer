'''
Unzipping of a zip files with the python module zipfile

https://thispointer.com/python-how-to-unzip-a-file-extract-single-multiple-or-all-files-from-a-zip-archive/
https://thispointer.com/python-how-to-get-the-list-of-all-files-in-a-zip-archive/
'''

from zipfile import ZipFile
	
# Create a ZipFile Object and load sample.zip in it
with ZipFile('G:/projekte/studyexplorer/xml.zip', 'r') as zipObj:
    # Get list of files names in zip
    listOfiles = zipObj.namelist()
    # Iterate over the list of file names in given list & print them
    n = 0
    for elem in listOfiles:
       n += 1
       print(n, elem)
    # Extract all files to specified path
    zipObj.extractall("C:/temp/")



'''
def 


if __name__ == "__main__":
    from zipfile import ZipFile

'''