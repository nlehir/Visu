"""
    add another feature to the dataset
"""
# create a simple fish dataset
import numpy as np

nb_data = 400

# we consider binary weights
fish_features = np.random.randint(2, size=(nb_data, 2))

# length in centimeters
tuna_length = np.random.normal(45, 6, (nb_data,))
salmon_length = np.random.normal(30, 6, (nb_data,))
fish_length = np.concatenate((tuna_length, salmon_length))

# weight in kilograms
tuna_weight = np.random.normal(6, 3, (nb_data,))
salmon_weight = np.random.normal(4, 1, (nb_data,))
fish_weight = np.concatenate((tuna_weight, salmon_weight))

# put all the features together
fish_features = np.column_stack((fish_length, fish_weight))
fish_class = np.concatenate((np.zeros(nb_data), np.ones(nb_data)))

# save the data to python files
np.save("data/fish_features_blurred", fish_features)
np.save("data/fish_class_blurred", fish_class)
