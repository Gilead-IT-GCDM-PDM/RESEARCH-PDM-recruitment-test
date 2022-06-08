import sqlite3
import sqlalchemy as sa
from sqlalchemy.types import Integer, Text, String, DateTime
import pandas as pd
import csv

engine = sa.create_engine('sqlite:///deathstar.db')
connection = engine.connect()

# A helpful bit of python for getting a dict of crew types
"""
    type_dic = {}
    sql="SELECT * FROM crew_type"
    result = engine.execute(sql)
    result_arry = [list(ele) for ele in result.fetchall()]
    for x in result_arry:
        type_dic[x[1]] = x[0]
"""

# A helpful bit of python for reading a csv
"""
    passenger_manifest = []
    with open(csv_name, newline='') as csvfile:
        passenger_manifest = []
        reader = csv.DictReader(csvfile)
        for row in reader:
            passenger_manifest.append(row)
"""

# BUILD SOME FUNCTIONS TO WRITE YOUR DATA
# REMEMBER: open and close your dates, make sure your crew_type_id is right. 


if __name__ == '__main__':
    # two file names 
    # shuttle_2022_06_01.csv
    # shuttle_2022_06_08.csv

    # CALL FUNCTIONS HERE to fill out your tables and update the db