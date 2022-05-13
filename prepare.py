import pandas as pd


##Iris prepped dataset
def prep_iris(df):
    '''
    Takes in the mysql dataframe and returns a clean dataframe
    Arguments: df - a pandas dataframe with the expected feature names and columns
    Return: clean_df - a dataframe with the cleaning operations performed on it
    '''
    #Drop duplicates
    df.drop_duplicates(inplace=True)
    #drop the columns
    columns_to_drop = ['species_id']
    #rename df so it does not interfere with og df
    sepal_data = df.drop(columns=columns_to_drop) 
    sepal_data.rename(columns = {'species_name':'species'}, inplace = True)
    #create dummy variables of the species name
    dummy_df = pd.get_dummies(sepal_data[['species']], dummy_na=False, drop_first=[True])
    # Concatenate my dummy_df to my data
    sepal_data1= pd.concat([sepal_data, dummy_df], axis=1)
    return sepal_data1

    #Need to add train, validate, test

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
