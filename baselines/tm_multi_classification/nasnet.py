import tensorflow as tf


def load_network():
    cnn = tf.keras.applications.NASNetLarge(
            input_shape=(800, 800, 3),
            include_top=False,
            weights=None,
            pooling='avg'
    )

    flatten = tf.keras.layers.Flatten()(cnn.layers[-1].output)
    fcn = tf.keras.layers.Dense(2048, activation='relu')(flatten)
    fcn_classification = tf.keras.layers.Dense(1558, activation='sigmoid')(fcn)
    model = tf.keras.Model(inputs=cnn.inputs, output=fcn_classification)
    return model
