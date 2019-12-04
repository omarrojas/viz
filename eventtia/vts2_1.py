import sqlite3
import json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect('db.sqlite3')
connection.row_factory = dict_factory

def ts2_1_data(con, attendeetypename):
    cursorObj = con.cursor()
    if (attendeetypename == "All"):
        cursorObj.execute("""
                SELECT attendee_type_name, demora15min, range_order, sum(attendees) attendees
                    FROM SalidaTarea2
                    GROUP BY attendee_type_name, demora15min, range_order 
                    ORDER BY attendee_type_name, range_order
            """, )
    else:
        cursorObj.execute("""
                SELECT attendee_type_name, demora15min, range_order, sum(attendees) attendees
                    FROM SalidaTarea2
                    WHERE attendee_type_name = ? 
                    GROUP BY attendee_type_name, demora15min, range_order 
                    ORDER BY attendee_type_name, range_order
        """, (attendeetypename,))

    data = cursorObj.fetchall()
    return json.dumps(data)
