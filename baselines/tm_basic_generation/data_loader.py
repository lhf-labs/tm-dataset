import os
import numpy as np
import tensorflow as tf


class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, data, path, batch_size=32):
        self.data = data
        self.path = path
        self.batch_size = batch_size

    def __len__(self):
        return len(self.data) // self.batch_size

    def __getitem__(self, index):
        # select
        items = self.data[index * self.batch_size:index * self.batch_size + self.batch_size]

        # images
        images = [
            tf.keras.preprocessing.image.img_to_array(
                tf.keras.preprocessing.image.load_img(item, target_size=(256, 256)))
            for item in items]
        images = np.stack(images)

        return images
