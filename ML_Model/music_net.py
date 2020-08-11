import tensorflow as tf 
from tensorflow.keras import layers, models,

class MusicNet(tf.keras.Sequential()):

    def __init__(self,input_dim:int):
        self.model = models.Sequential()
        self.model.add(layers.Conv2D(input_dim,(3,3), activation='relu',input_shape=(input_dim,3,3)))
        self.model.add(layers.MaxPooling2D((2,2)))
        self.model.add(layers.Conv2D(input_dim*2,(3,3),activation='relu'))
        self.model.add(layers.MaxPooling2D((2,2)))
        self.model.add(layers.Conv2D(input_dim*2,(3,3),activation='relu'))
        return
    
    def model(self):
        return self.model
    
    def compile(self):
        self.model.compile()
        return