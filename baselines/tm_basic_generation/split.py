import numpy as np


def split(data, ratio=0.02):
    data = np.array(data)
    valid_test_n = int(len(data) * ratio)
    indices = np.arange(len(data))

    valid_indices = np.random.choice(indices, valid_test_n)
    valid_data = data[valid_indices]
    indices = indices[~np.isin(indices, valid_indices)]

    test_indices = np.random.choice(indices, valid_test_n)
    test_data = data[test_indices]
    indices = indices[~np.isin(indices, test_indices)]

    train_data = data[indices]
    return train_data, valid_data, test_data
