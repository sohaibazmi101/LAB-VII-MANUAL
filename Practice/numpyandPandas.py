import numpy as np
import pandas as pd

np.random.seed()
emp = pd.DataFrame({
    'Ages': np.random.randint(22, 60, 8),
    'Salary': np.random.uniform(30000, 80000, 8).round(1)
})
print(emp)
emp.loc[emp['Ages'] < 30, 'Salary'] = emp.loc[emp['Ages'] < 30, 'Salary'] * 110/100
emp.loc[emp['Ages'] < 30, 'Salary'] = emp.loc[emp['Ages'] > 50, 'Salary'] * 95/100
print(emp)

# Problem 2 Random Temparature

city = pd.DataFrame({
    'temp': np.random.uniform(25, 40, 7).round(1)
})
print(city)
print(f"Maximum: {city.max()}")
print(f"Minimum Temp: {city.min()}")
print(f"Average: {city.mean()}")

# Problem 3 mix

students = pd.DataFrame({
    'study_hrs': np.random.randint(5, 50, 6),
    'sleep_hrs': np.random.uniform(4, 9, 6).round(1)
})
print(students)

students.loc[students['study_hrs'] > 30, 'sleep_hrs'] = np.random.uniform(4, 6, sum(students['study_hrs'] > 30)).round(1)
students.loc[students['study_hrs'] < 10, 'sleep_hrs'] = np.random.uniform(7, 9, sum(students['study_hrs'] < 10)).round(1)
print("Students Data:\n", students)
