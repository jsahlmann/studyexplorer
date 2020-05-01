'''
Searching for medication in xml files.

The medication can be found as an element named <mesh-term>.

The regex searches for this element.

<mesh_term>.*?</mesh_term>

https://stackoverflow.com/questions/10477294/how-do-i-search-for-a-pattern-within-a-text-file-using-python-combining-regex
'''


def search_regex_file(fileName):
    print(fileName)
    pattern = re.compile("<mesh_term>.*?</mesh_term>")
    i = 0
    line = 0
    for i, line in enumerate(open(fileName)):
        for match in re.finditer(pattern, line):
            print('Found on line %s: %s' % (i + 1, match.group()))


if __name__ == "__main__":
    import os
    import re
    import jsa_listdir

    dirName = 'G:/projekte/studyexplorer/data/NCT0001xxxx'

    xml_list = jsa_listdir.getListOfFiles(dirName)
    n = 0
    for elem in xml_list:
        n += 1
        print("Datei: ", n, elem)
        search_regex_file(elem)