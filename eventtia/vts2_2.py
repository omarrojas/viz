import sqlite3
import json

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect('db.sqlite3')
connection.row_factory = dict_factory

def ts2_2_data(con,  countryname, weekday):
    cursorObj = con.cursor()
    if (weekday == "All"):
        cursorObj.execute("""
                SELECT country_name, nom_week_day, demora15min, range_order, sum(attendees) attendees
                    FROM SalidaTarea2
                    GROUP BY range_order, country_name, nom_week_day, demora15min
                    ORDER BY range_order, country_name, nom_week_day
            """, )
    else:
        cursorObj.execute("""
                SELECT country_name, nom_week_day, demora15min, range_order, sum(attendees) attendees
                    FROM SalidaTarea2
                    WHERE country_name = ? 
                        AND nom_week_day = ?
                    GROUP BY range_order, country_name, nom_week_day, demora15min
                    ORDER BY range_order, country_name, nom_week_day
        """, (countryname, weekday,))

    data = cursorObj.fetchall()
    return json.dumps(data)
