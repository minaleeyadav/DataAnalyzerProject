import pandas as pd

data = {
    'Name': ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown', 'Jessica White', 
             'George Black', 'Sarah Green', 'Robert Blue', 'Laura Yellow', 'Mark Orange'],
    'Age': [28, 34, 22, 45, 29, 52, 31, 39, None, 41],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 
               'Male', 'Female', 'Male', 'Female', 'Male'],
    'Occupation': ['Engineer', 'Doctor', 'Student', 'Teacher', 'Designer', 
                   'Manager', 'Scientist', 'Artist', 'Writer', 'Chef'],
    'Salary': [50000, 75000, None, 55000, 47000, 90000, 80000, 35000, 40000, 48000],
    'YearsExperience': [5, 10, 1, 20, 4, 25, 7, 8, None, 15]
}

df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)
