'''
jsa_ctg.py

The study data can be downloaded from the website clinicaltrials.gov.
The size is about 1.6 GB als zipped file.

For the download we use the wget module of python which has to be installed via 

pip install wget

Details concerning other examples of downloading files can be found at
https://dzone.com/articles/simple-examples-of-downloading-files-using-python
'''

def wget_url(url, dest):
    '''
    Use of the wget modul of python
    
    '''
    wget.download(url, dest)

if __name__ == "__main__":
    import wget
    my_url = 'https://www.python.org/static/img/python-logo@2x.png'
    my_dest = 'G:/projekte/clinicaltrials/pythonLogo.png'
    # url = 'https://clinicaltrials.gov/AllPublicXML.zip'
    # dest = 'G:/projekte/clinicaltrials/CurrentPublicXML.zip'
    wget_url(my_url, my_dest)
