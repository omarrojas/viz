import sqlite3
import json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect('db.sqlite3')
connection.row_factory = dict_factory

def tp2_data(con, countryname, weekday):

    cursorObj = con.cursor()
    if (weekday == "All"):
        cursorObj.execute("""
                SELECT demora15min, range_order, sum(attendees) attendees
                    FROM SalidaTarea2
                    WHERE country_name = ?
                    GROUP BY demora15min, range_order 
            """, (countryname,))
    else:
        cursorObj.execute("""
                SELECT demora15min, range_order, sum(attendees) attendees
                    FROM SalidaTarea2
                WHERE country_name = ? 
                  AND now_week_day = ?
                GROUP BY demora15min, range_order 
        """, (countryname, weekday,))

    data = cursorObj.fetchall()
    return json.dumps(data)
