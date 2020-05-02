'''
Parsing an XML file with ElementTree and saving the some data into an sqlite3 database

Two tables will be created. One for the data with a 1:1 relationship and one for the
data with a 1:n relationship.

Retrieving inserted data from database.

https://www.datacamp.com/community/tutorials/python-xml-elementtree
https://www.sqlitetutorial.net/sqlite-python/creating-database/
https://www.sqlitetutorial.net/sqlite-python/create-tables/
https://stackoverflow.com/questions/22488763/sqlite-insert-query-not-working-with-python
'''
def db_init(db_file):
    '''
    This procedure initializes a database and creates the necessary tables.

    Args:
        db_file (str): path to databasefile
    
    Returns:
        NONE
    '''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
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

        sql1 = ''' INSERT INTO study (nct_id, brief_title)  
                   VALUES (?, ?); '''
        sql2 = ''' INSERT INTO mesh_term (nct_id, param, value) 
                   VALUES (?, ?, ?); '''

        cur = conn.cursor()
        row_study = (nct_id, brief_title)
        cur.execute(sql1, row_study)
        conn.commit() # execute the queries

        for elem in root.findall('intervention_browse/mesh_term'):
            mesh_term = elem.text
            cur = conn.cursor()
            row_mesh_term = (nct_id, 'mesh_term', mesh_term)
            cur.execute(sql2, row_mesh_term)
            conn.commit() # execute the queries
    
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
