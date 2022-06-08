import sqlite3
import sqlalchemy as sa
from sqlalchemy.types import Integer, Text, String, DateTime
import pandas as pd

engine = sa.create_engine('sqlite:///deathstar.db')
connection = engine.connect()

# An example of a function which selects from the db
def select_star():
    sql = """SELECT * FROM CREW"""
    result = engine.execute(sql)
    result_arry = [list(ele) for ele in result.fetchall()]
    result_keys = result.keys()
    df = pd.DataFrame(result_arry, columns=result_keys)
    return df


# should be the only query you need for the dashboard
def get_pie_data(crew_type_dd, start_date, end_date):
    
    # SUGGESTION Handle crew_type_dd 

    # INSERT YOUR SQL HERE 
    sql=""""""

    #print(sql)
    result = engine.execute(sql)
    result_arry = [list(ele) for ele in result.fetchall()]
    result_keys = result.keys()
    df = pd.DataFrame(result_arry, columns=result_keys)
    return df