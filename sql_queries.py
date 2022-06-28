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
def get_pie_data(crew_type_dd, start_date):
    
    if crew_type_dd == "All":
        filter_type = ""
    elif crew_type_dd == "Crewmen":
        filter_type = "and crew_type.is_vip is Null"
    elif crew_type_dd == "VIP":
        filter_type = "and crew_type.is_vip = 'Y'"
    else:
        filter_type = ""

    sql = """select crew_type.crew_type as crew_type, count(crew.crewman_name) as crew_count from crew
left join crew_type
on crew.crew_type_id = crew_type.crew_type_id
where crew.boarding_date <= '{1}'
and (crew.offboarding_date is Null or crew.offboarding_date >= '{1}')
{0}
group by crew_type.crew_type""".format(filter_type, start_date)

    print(sql)
    result = engine.execute(sql)
    result_arry = [list(ele) for ele in result.fetchall()]
    result_keys = result.keys()
    df = pd.DataFrame(result_arry, columns=result_keys)
    return df