import tensorflow as tf 
from tensorflow.keras import layers, models,

import matplotlib.pyplot as plt

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
        self.model().compile(optimizer='adam',
                            loss= tf.keras.losses.SparseCategoricalCrossEntropy(from_logits=True),
                            metrics=['accuracy'])
        return
    
    def history(self, train_images, train_labels, epochs, test_images, test_labels):

        return self.model.fit(train_images, train_labels, epochs=epochs, 
                    validation_data=(test_images, test_labels))
    
    def plot_model(self, train_images, train_labels, epochs, test_images, test_labels):
        history= self.history( train_images, train_labels, epochs, test_images, test_labels)
        plt.plot(history.history['accuracy'], label='accuracy')
        plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.ylim([0.5, 1])
        plt.legend(loc='lower right')


        test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
        return test_loss, test_acc
