import os
import json
import tensorflow as tf
from split import split
from itertools import chain
from datetime import datetime
from nasnet import load_network
from data_loader import DataGenerator


PATH = '../../../output/'
SUB_PATH_1 = 'train_32x32/train_32x32'
SUB_PATH_2 = 'valid_32x32/valid_32x32'
BATCH_SIZE = 2
EPOCHS = 20
VIENNA_LEVEL = 2
if __name__ == '__main__':
    with open(os.path.join(PATH, 'results.json'), 'r', encoding='utf-8') as fin:
        data = json.load(fin)
    if VIENNA_LEVEL == 2:
        for d in data:
            d['vienna_codes'] = ['.'.join(code.split(".")[0:2]) for code in d['vienna_codes']]
    labels = list(set(chain.from_iterable([d['vienna_codes'] for d in data])))

    for d in data:
        file = os.path.join(PATH, 'images', SUB_PATH_1, d['file'])
        if os.path.isfile(file):
            d['file'] = file
        else:
            d['file'] = os.path.join(PATH, 'images', SUB_PATH_2, d['file'])

    train_data, valid_data, test_data = split(data)

    model = load_network(labels)
    model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate=0.00002), metrics=['accuracy'])

    train_generator = DataGenerator(train_data, labels, os.path.join(PATH, 'images'), num_classes=len(labels),
                                    batch_size=BATCH_SIZE)
    valid_generator = DataGenerator(valid_data, labels, os.path.join(PATH, 'images'), num_classes=len(labels),
                                    batch_size=BATCH_SIZE)
    test_generator = DataGenerator(test_data, labels, os.path.join(PATH, 'images'), num_classes=len(labels),
                                   batch_size=BATCH_SIZE)

    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor='val_accuracy', min_delta=0, patience=2, verbose=1,
        mode='auto', baseline=None, restore_best_weights=True
    )
    path = os.path.join('output', datetime.now().strftime("%Y%m%d-%H%M%S"))
    os.makedirs(path, exist_ok=True)
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=path, update_freq=1000)
    history = model.fit(train_generator, epochs=EPOCHS, shuffle=True, validation_data=valid_generator,
                        callbacks=[early_stopping, tensorboard_callback])
    test_results = model.evaluate(test_generator)

    model.save('output/model')
    print(history)
    print(test_results)
