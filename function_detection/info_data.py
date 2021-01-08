import pandas as pd

DIR_PATH_DATA = "F:\programmation\Docker\project_api_Docker\data"
FILE_DATA_CSV = "KDD_clean_database.csv"
list_info_data = []

def information_data(DIR_PATH_DATA, FILE_DATA_CSV):
    df = pd.read_csv(DIR_PATH_DATA + FILE_DATA_CSV)
    
    for col in df.columns:
        list_info_data.append({col: len(df[col])})

    # list_info_data.append({"describe": df.describe()})
    return list_info_data