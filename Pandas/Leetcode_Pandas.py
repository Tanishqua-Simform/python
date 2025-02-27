## Dt. 21st Feb, 2025
# 2877. Create a DataFrame from List

import pandas as pd

def createDataframe(student_data: list) -> pd.DataFrame:
    s_id, s_age = [], []
    for s in student_data:
        s_id.append(s[0])
        s_age.append(s[1])
    
    data = {
        'student_id': s_id,
        'age': s_age
    }
    
    df = pd.DataFrame(data)
    return df

# 2878. Get the Size of a DataFrame

def getDataframeSize(players: pd.DataFrame) -> list:
    return [players.shape[0], players.shape[1]]

# 2879. Display the First Three Rows

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

## Dt. 24th Feb, 2025
# 2880. Select Data

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]

## Dt. 27th Feb, 2025
# 2881. Create a New Column

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 2 * employees['salary']
    return employees

# 2882. Drop Duplicate Rows

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers

# 2883. Drop Missing Data

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset='name', inplace=True)
    return students

# 2885. Rename Columns

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }, inplace=True)
    return students

# 2887. Fill Missing Data

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(value=0, inplace=True)
    return products

# 2888. Reshape Data: Concatenate

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    merged = pd.concat([df1, df2])
    return merged