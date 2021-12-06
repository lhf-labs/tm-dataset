import os
import json
import tensorflow as tf
from split import split
from itertools import chain
from datetime import datetime
from dcgan import DCGAN
from data_loader import DataGenerator

PATH = '../../../images_test/'
BATCH_SIZE = 32
EPOCHS = 20
if __name__ == '__main__':
    data = list()
    for root, dirs, files in os.walk(PATH, topdown=False):
        for name in files:
            data.append(os.path.join(root, name))

    train_data, valid_data, test_data = split(data)

    train_generator = DataGenerator(train_data, os.path.join(PATH, 'images'), batch_size=BATCH_SIZE)
    valid_generator = DataGenerator(valid_data, os.path.join(PATH, 'images'), batch_size=BATCH_SIZE)
    test_generator = DataGenerator(test_data, os.path.join(PATH, 'images'), batch_size=BATCH_SIZE)

    DCGAN().train(epochs=EPOCHS, train_generator=train_generator, valid_generator=valid_generator,
                  test_generator=test_generator, batch_size=BATCH_SIZE, save_interval=1)
