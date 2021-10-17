import os
import numpy as np
import tensorflow as tf


class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, data, labels, path, num_classes, batch_size=32):
        self.data = data
        self.labels = labels
        self.path = path
        self.num_classes = num_classes
        self.batch_size = batch_size

    def __len__(self):
        return len(self.data) // self.batch_size

    def __getitem__(self, index):
        # select
        items = self.data[index * self.batch_size:index * self.batch_size + self.batch_size]

        # images
        images = [
            tf.keras.preprocessing.image.img_to_array(
                tf.keras.preprocessing.image.load_img(os.path.join(self.path, item['file']), target_size=(331, 331)))
            for item in items]
        images = np.stack(images)

        # labels
        labels = list()
        for item in items:
            label = np.isin(self.labels, item['vienna_codes']).astype(float)
            labels.append(label)
        labels = np.stack(labels)

        return images, labels
