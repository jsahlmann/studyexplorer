# Start here

This document gives you a path through the available files and explains some features of python.

We have a task to perform. We want to have a list of all medications which were tested in the studies which where registered at clinicaltrials.gov.

## Get the data

Have a look at the file *src/jsa_ctg.py*.

Here you can find how to download files from an URL to a specified destination with python. 

The function wget_url() uses the wget python module.

The page https://clinicaltrials.gov/ct2/resources/download from clinicaltrials.gov describes the available data.

We save the downloaded file AllPublicXML.zip. For the development we take a subset of this file with two folders instead of 437 folders and save it as xml.zip.

## Extract the data

Look into the file *src/jsa_zip.py*.

Here you can see who zipfiles can be handled by python. First, all available file names will be listed with the relative path and then all files will be extracted to a specified path. 

The data from xml.zip will be extracted to a folder *data*.

## Parse the data with regular expressions

The file *src/jsa_regex.py* shows how a file can be searched by a regular expression for a specific term.

We search for the pattern `<mesh-term>.*?</mesh-term>`.

The intervention of the study is documented in this element.

```xml
  <condition_browse>
    <mesh_term>Melanoma</mesh_term>
  </condition_browse>
  <intervention_browse>
    <mesh_term>Aldesleukin</mesh_term>
    <mesh_term>Freund's Adjuvant</mesh_term>
  </intervention_browse>
```

As we can see this pattern is ambigious. It cannot distinguish between condition and intervention. We have to consider the path in the xml file.

## Parse the data with xpath

The file *src/jsa_xml.py* gives an example how an xml file can be parsed using the module xml from python.
Searching for the xpath `intervention_browse/mesh_term`gives the result:

```
Aldesleukin
Freund's Adjuvant
```

By this way we have the interventions as a result.