import sqlite3
import sqlalchemy as sa
from sqlalchemy.types import Integer, Text, String, DateTime

engine = sa.create_engine('sqlite:///deathstar.db')
connection = engine.connect()


def insert_crewman(crew_name, crew_type):
    sql = """ INSERT INTO crew (crewman_name, crew_type_id, boarding_date, offboarding_date)
    VALUES ('{}', {},'{}', Null) """.format(crew_name, crew_type, '2022-05-04')
    engine.execute(sql)


def get_crew_types():
    type_dic = {}
    sql="SELECT * FROM crew_type"
    result = engine.execute(sql)
    result_arry = [list(ele) for ele in result.fetchall()]
    for x in result_arry:
        type_dic[x[1]] = x[0]
    return type_dic


def truncate_crews():
    sql = """ DELETE FROM crew """
    engine.execute(sql)

if __name__ == '__main__':

    outline = [
        {"type": "Storm Trooper", "quantity": 1000},
        {"type": "Crewman", "quantity": 100},
        {"type": "Pilot", "quantity": 20},
    ]

    truncate_crews()

    crew_types = get_crew_types()
    for o in outline:
        for x in range(0, o["quantity"]):
            new_name = "{0}_{1}".format(o['type'].replace(" ", "_").lower(), x)
            insert_crewman(new_name, crew_types[o['type']])
