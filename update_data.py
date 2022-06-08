import sqlite3
import sqlalchemy as sa
from sqlalchemy.types import Integer, Text, String, DateTime
import pandas as pd
import csv

engine = sa.create_engine('sqlite:///deathstar.db')
connection = engine.connect()

def write_crew(passenger_manifest):
    type_dic = {}
    sql="SELECT * FROM crew_type"
    result = engine.execute(sql)
    result_arry = [list(ele) for ele in result.fetchall()]
    for x in result_arry:
        type_dic[x[1]] = x[0]

    for p in passenger_manifest:
        if p['crew_type'] in type_dic.keys():
            sql = """ INSERT INTO crew (crewman_name, crew_type_id, boarding_date, offboarding_date)
                        VALUES ('{}', {},'{}', Null) """.format(p['crewman_name'], type_dic[p['crew_type']], p['boarding_date'])
            result = engine.execute(sql)


def load_csv(csv_name):
    passenger_manifest = []
    with open(csv_name, newline='') as csvfile:
        passenger_manifest = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            passenger_manifest.append(row)

    write_crew(passenger_manifest)

if __name__ == '__main__':
    load_csv('shuttle_2022_06_01.csv')