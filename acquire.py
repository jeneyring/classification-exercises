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

def google_sheets():
    sheet_url = 'https://docs.google.com/spreadsheets/d/1zozkbdAJBIovrqqaE7k0rC2dlKcaI9sA7BsSnJ7eAtg/edit#gid=1023018493'
    csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    df_googlesheet = pd.read_csv(csv_export_url)
    return df_googlesheet

def excel_file():
    excel_sheet="Jennifer Eyring - jemison_spreadsheet_exercises.xlsx"
    df_excel = pd.read_excel(excel_sheet)
    return df_excel


def get_titanic_data():
    new_titanic_data=
    if os.path.isfile('titanic_df.csv'):
        df = pd.read_csv('titanic_df.csv', index_col=0)
    else:
        df = new_titanic_data()

        df.to_csv('titanic_df.csv')