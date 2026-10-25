import numpy as np
print(f'Question #1- NumPy version: {np.__version__}\n')

array_1d = np.array([0,1,2,3,4,5,6,7,8,9])
print(f'Question #2- 1D Array: {array_1d}\n')

import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

column_names = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]

iris_df = pd.read_csv(url, header=None, names=column_names)

# Display the first five rows
print(f'Question #3- First five rows of the Iris dataset:\n{iris_df.head()}\n')

first_position = np.where(iris_df["petal_width"] > 1.0)[0][0]
print(f'Question #4- {first_position}\n')

np.random.seed(100)
a = np.random.uniform(1,50, 20)
a[a > 30] = 30
a[a < 10] = 10
print(f'Question #5- {a}')