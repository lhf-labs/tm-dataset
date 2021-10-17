import tensorflow as tf


def load_network(labels):
    cnn = tf.keras.applications.NASNetLarge(
            input_shape=(331, 331, 3),
            include_top=False,
            weights='imagenet',
            pooling='avg'
    )

    flatten = tf.keras.layers.Flatten()(cnn.layers[-1].output)
    fcn = tf.keras.layers.Dense(2048, activation='relu')(flatten)
    fcn_classification = tf.keras.layers.Dense(len(labels), activation='sigmoid')(fcn)
    model = tf.keras.Model(inputs=cnn.inputs, outputs=fcn_classification)

    for layer in model.layers[:20]:
        layer.trainable = False
    for layer in model.layers[20:]:
        layer.trainable = True

    return model
