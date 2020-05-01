'''
Parsing an XML file with ElementTree and saving the some data into an sqlite3 database

Two tables will be created. One for the data with a 1:1 relationship and one for the
data with a 1:n relationship.

Exporting to CSV

https://www.datacamp.com/community/tutorials/python-xml-elementtree
https://www.sqlitetutorial.net/sqlite-python/creating-database/
https://www.sqlitetutorial.net/sqlite-python/create-tables/
'''
def db_init(db_file):
    '''

    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        select_create_table_study = ''' CREATE TABLE IF NOT EXISTS study (
	        id integer PRIMARY KEY AUTOINCREMENT,
	        nct_id text NOT NULL,
	        brief_title text NOT NULL
        )
        '''
        select_create_table_mesh_term = ''' CREATE TABLE IF NOT EXISTS mesh_term (
	        id integer PRIMARY KEY AUTOINCREMENT,
	        nct_id text NOT NULL,
	        param text NOT NULL,
	        value text
        )
        '''
        c = conn.cursor()
        c.execute(select_create_table_study)
        c.execute(select_create_table_mesh_term)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def db_fill(db_file, f):
    '''
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        tree = ET.parse(f)
        root = tree.getroot()
        nct_id = root.find('id_info/nct_id').text
        brief_title = root.find('brief_title').text

        sql1 = ''' INSERT INTO study(nct_id, brief_title)  
                   VALUES(?, ?) '''
        sql2 = ''' INSERT INTO mesh_term(nct_id, param, value) 
                   VALUES(?, ?, ?) '''
        cur = conn.cursor()
        row_study = (nct_id, brief_title)
        print(sql1)
        cur.execute(sql1, row_study)
        print(nct_id, brief_title)
        print(cur.lastrowid)

        for elem in root.findall('intervention_browse/mesh_term'):
            mesh_term = elem.text
            cur = conn.cursor()
            row_mesh_term = (nct_id, 'mesh_term', mesh_term)
            print(sql2)
            cur.execute(sql2, row_mesh_term)
            print(nct_id, 'mesh_term', mesh_term)
            print(cur.lastrowid)
    
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def db_select(db_file):
    '''
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        sql1 = ''' SELECT * FROM study
        '''
        sql2 = ''' SELECT * FROM mesh_term
        '''

        cur = conn.cursor()
        cur.execute(sql1)
        rows = cur.fetchall()
        for row in rows:
            print(row)        
    
        cur = conn.cursor()
        cur.execute(sql2)
        rows = cur.fetchall()
        for row in rows:
            print(row)        

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    import sqlite3
    from sqlite3 import Error
    import xml.etree.ElementTree as ET
    db_init('G:/projekte/studyexplorer/data/ctg.db')
    db_fill('G:/projekte/studyexplorer/data/ctg.db', 
    'G:/projekte/studyexplorer/data/NCT0001xxxx/NCT00019994.xml')
    db_select('G:/projekte/studyexplorer/data/ctg.db')
