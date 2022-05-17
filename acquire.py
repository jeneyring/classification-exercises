### iris_db
import pandas as pd
import matplotlib as plt
import numpy as np
import env
import os
    
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
#_________________________________________________
#iris_db from mysql 

def get_iris_data():
    '''
    This function reads the iris data from the Codeup db into a df.
    '''
    sql_query = """
                SELECT 
                    species_id,
                    species_name,
                    sepal_length,
                    sepal_width,
                    petal_length,
                    petal_width
                FROM measurements
                JOIN species USING(species_id)
                """

    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('iris_db'))

    return df
#_________________________________________________________________________________
#google sheet 'Telco churn data'

sheet_url = 'https://docs.google.com/spreadsheets/d/1zozkbdAJBIovrqqaE7k0rC2dlKcaI9sA7BsSnJ7eAtg/edit#gid=1023018493'    

csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

df_googlesheet = pd.read_csv(csv_export_url)
df_googlesheet.head()

def google_sheets():
    sheet_url = 'https://docs.google.com/spreadsheets/d/1zozkbdAJBIovrqqaE7k0rC2dlKcaI9sA7BsSnJ7eAtg/edit#gid=1023018493'
    csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    df_googlesheet = pd.read_csv(csv_export_url)
    return df_googlesheet
#__________________________________________________________________________________
#Excel version of Telco churn data

def excel_file():
    excel_sheet="Jennifer Eyring - jemison_spreadsheet_exercises.xlsx"
    df_excel = pd.read_excel(excel_sheet)
    return df_excel

#_________________________________________________________________________________
#Titanic data

def new_titanic_data():
    '''
    This function reads the titanic data from the Codeup db into a df,
    write it to a csv file, and returns the df.
    '''
    # Create SQL query.
    sql_query = 'SELECT * FROM passengers'
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('titanic_db'))
    
    return df



def get_titanic_data():
    '''
    This function reads in titanic data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('titanic_df.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('titanic_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = new_titanic_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('titanic_df.csv')
        
    return df

#______________________________________________________
#Train dataset data
'''
This dataset is named "Train" and reads in a dataset connected to titanic_df (includes
the names of titanic passengers). Pulled from a csv file
'''
def get_train_data():
    sheet_url = 'https://docs.google.com/spreadsheets/d/1Uhtml8KY19LILuZsrDtlsHHDC9wuDGUSe8LTEwvdI5g/edit#gid=341089357'    
    csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    df_train = pd.read_csv(csv_export_url)
    return df_train

#_________________________________________________________
#Codeup Duck data
'''
This dataset is for Evaluation exercises and reads the dataset connected to Exercise 3
'''

def get_duckies_data():
    if os.path.isfile('c3.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('c3.csv')
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = get_duckies_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('c3.csv')
        
    return df