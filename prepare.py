import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


##Iris prepped dataset  
def split_iris_data(df):
    '''
    Take in a df and return train, validate and test df; stratify on species'''

    #splits df in to train_validate and test using traing_test_split()
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.species)


    #stratify on species to get an equal number of species
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123, stratify=train_validate.species)

    return train, validate, test

def prep_iris(df):
    '''
    Takes in the mysql dataframe and returns a clean dataframe
    Arguments: df - a pandas dataframe with the expected feature names and columns
    Return: clean_df - a dataframe with the cleaning operations performed on it
    '''
    #Drop duplicates
    df.drop_duplicates(inplace=True)
    #drop the columns
    df= df.drop(columns='species_id')
    df.rename(columns = {'species_name':'species'}, inplace = True)
    #create dummy variables of the species name
    dummy_df = pd.get_dummies(df[['species']], dummy_na=False, drop_first=[True])
    # Concatenate my dummy_df to my data
    df= pd.concat([df, dummy_df], axis=1)

    #split data into train/validate/test using split_data function
    train, validate, test = split_iris_data(df)
    
    return train, validate, test
    
    #____________________________________________________________________________________

##Titanic prepped dataset
def clean_titanic_data(df):
    '''
    Takes in a titanic dataframe and returns a clean dataframe
    Arguments: df - a pandas dataframe with the expected feature names and columns
    Return: clean_df - a dataframe with the cleaning operations performed on it
    '''
    #Drop duplicates
    df.drop_duplicates(inplace=True)
    #Drop columns
    columns_to_drop=['embarked', 'class', 'passenger_id', 'deck']
    data = df.drop(columns=columns_to_drop) #saved as a new variable so as not to mess up original data
    #Encoding categorical variables
    dummy_df = pd.get_dummies(data[['sex', 'embark_town']], dummy_na=False, drop_first=[True, True])
    data= pd.concat([data, dummy_df], axis=1)
    return data.drop(columns=['sex','embark_town'])

    df = acquire.get_titanic_data()
    clean_df= clean_titanic_data(df)
    clean_df

    train, test = train_test_split(clean_df, 
                               train_size = 0.8, 
                               stratify = clean_df.survived, 
                               random_state=1234) #note, stratify is ONLY used on categorical columns


     #Need to add train, validate, test

    #____________________________________________________________________________________

##Telco prepped dataset
def clean_telco_data(df):
    '''
    Takes in the Telco dataset and cleans & prepares for test, validation and training purposes for exploration on the data of past churned customers.
    '''
    #create new column to describe contract types
    df["contract_type"].replace({0: "month_to_month", 1: "one_year", 2: "two_years"}, inplace=True)
    #drop duplicates
    df.drop_duplicates(inplace=True)
    #encoding columns:
    dummy_df = pd.get_dummies(df[['gender', 'dependents', 'partner', 'contract_type', 'payment_type']], dummy_na=False, drop_first=[True, True, True, True])
    #concat to original
    df_telco = pd.concat([df, dummy_df], axis=1)
    return df_telco
