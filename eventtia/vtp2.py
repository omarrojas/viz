import sqlite3
import json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect('db.sqlite3')
connection.row_factory = dict_factory

def tp2_data(con, countryname):

    cursorObj = con.cursor()

    cursorObj.execute("""
            SELECT * 
              FROM SalidaTarea2
              WHERE country_name = ?
        """, (countryname,))

    data = cursorObj.fetchall()
    return json.dumps(data)

    #return {"records":list(cursorObj.fetchall())}

#salida = sql_fetch(connection, 'Mexico')

#print(salida)
