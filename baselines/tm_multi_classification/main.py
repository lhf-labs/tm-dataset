import os
import json
from itertools import chain
from nasnet import load_network
from data_loader import DataGenerator

'''
TODO:
specify path
train valid test split
train valid test generators
tensorboard
early stopping
save model
'''


PATH = ''
BATCH_SIZE = 32
EPOCHS = 20
if __name__ == '__main__':
    with open(os.path.join(PATH, 'results.json'), 'r', encoding='utf-8') as fin:
        data = json.load(fin)
    labels = list(set(chain.from_iterable([d['vienna_codes'] for d in data])))

    model = load_network()
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    data_generator = DataGenerator(data, labels, os.path.join(PATH, 'images'), num_classes=len(labels),
                                   batch_size=BATCH_SIZE)


    history = model.fit(data_generator, epochs=EPOCHS, shuffle=True, )

