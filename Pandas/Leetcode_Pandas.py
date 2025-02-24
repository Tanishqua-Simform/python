# Dt. 21st Feb, 2025
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

# Dt. 24th Feb, 2025
# 2880. Select Data

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]