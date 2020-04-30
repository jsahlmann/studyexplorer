# Start here

This document gives you a path through the available files and explains some features of python.

## Get the data

Have a look at the file *src/jsa_ctg.py*.

Here you can find how to download files from an URL to a specified destination with python. 

The function wget_url uses the wget python module.

The page https://clinicaltrials.gov/ct2/resources/download from clinicaltrials.gov describes the available data.

## Extract the data

Look into the file *src/jsa_zip.py*.

Here you can see who zipfiles can be handled by python. First, all available file names will be listed with the relative path and then all files will be extracted to a specified path. The sample zipfile does not contain all data. It is only a very small subset.