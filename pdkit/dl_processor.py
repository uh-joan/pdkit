import numpy as np
import random as rn

from pdkit.models import RCL
from pdkit.utils import window_features

from keras.optimizers import sgd, adam
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau

from keras.utils import to_categorical


class QoIProcessor(object):
    def __init__(self,
                 input_shape=(150, 4),
                 labels=2,
                 output_activation='sigmoid'):
        
        self.model = RCL( input_shape=input_shape,
                          rec_conv_layers=[
                              [
                                  [(32, 9), (2, 1), 0.5, 0.5],
                                  [(32, 9), (2, 1), 0.5, 0.5],
                                  [(32, 9), (2, 1), 0.5, 0.5, 6]
                              ],
                              [
                                  [(64, 9), (2, 1), 0.5, 0.5],
                                  [(64, 9), (2, 1), 0.5, 0.5],
                                  [(64, 9), (2, 1), 0.5, 0.5, 6]
                              ]

                          ],
                          dense_layers=[(512, 0.0, 0.5),
                                        (512, 0.0, 0.5)],
                          padding='same',
                          optimizer=adam(lr=0.001),
                          output_layer=[labels, output_activation]
                       )
    
    def window_data(self, x, y=None, window_size=100, overlap=10):
        
        idx = window_features(np.arange(x.shape[0]), window_size, overlap)
        
        features = x[idx]
        if y:
            labels = [y] * idx.shape[0]
            return features, labels
        
        return features