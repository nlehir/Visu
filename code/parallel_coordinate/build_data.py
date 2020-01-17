import numpy as np

column_1 = np.random.uniform(3, 5, 10)

noise_2 = np.random.normal(0, 0.01, 10)
column_2 = 4*column_1+noise_2

noise_3 = np.random.normal(0, 0.1, 10)
column_3 = 50 - 2*column_2+noise_3

noise_4 = np.random.normal(0, 5, 10)
column_4 = 10+column_1+noise_4

data = np.column_stack((column_1, column_2))
data = np.column_stack((data, column_3))
data = np.column_stack((data, column_4))

np.save("data", data)
