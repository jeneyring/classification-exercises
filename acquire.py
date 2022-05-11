### iris_db
import pandas as pd
import matplotlib as plt
import numpy as np
import env
import os
    
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_iris_data():
    filename = 'iris_db.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql('SELECT * FROM measurements JOIN species WITH species_id', get_connection('iris_db'))
        
        df.to_csv(filename)

        return df


sheet_url = 'https://docs.google.com/spreadsheets/d/1zozkbdAJBIovrqqaE7k0rC2dlKcaI9sA7BsSnJ7eAtg/edit#gid=1023018493'    

csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

df_googlesheet = pd.read_csv(csv_export_url)
df_googlesheet.head()
