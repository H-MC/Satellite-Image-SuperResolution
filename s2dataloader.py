# %% [code]
import glob, cv2
import numpy as np
import mxnet as mx
import tensorflow as tf
from PIL import Image
from tensorflow import keras


# Subclassed iterable from keras.utils.Sequence
class Dataseq(keras.utils.Sequence):
    def __init__(self,
                 fnList,
                 scale,
                 batch_size=4,
                 shuffle=False):       
        self.batch_size = batch_size
        self.fnList = fnList
        self.findx = np.arange(len(fnList))
        self.shuffle = shuffle
        self.on_epoch_end()
        self.scale = scale
        self.shape = np.array(Image.open(fnList[0])).shape[0]
        self.resize = np.int(self.shape/self.scale)
        
    def __len__(self):
        return len(self.fnList) // self.batch_size
                      
    def __getitem__(self, bindx):
        for i in range(self.batch_size):
            j = self.findx[bindx*self.batch_size + i]
            file = f'{self.fnList[j]}'
            
            # Create high and low resolution image
            img = mx.image.imdecode(open(file,'rb').read())
            imgh = img.asnumpy()
            imgl = mx.image.imresize(img, self.resize, self.resize, interp=cv2.INTER_LINEAR).asnumpy()
            
            # Change to float32
            imgh = tf.cast(imgh, tf.float32)
            imgl = tf.cast(imgl, tf.float32)
            
            # Expand dimension
            imgh = tf.expand_dims(imgh, axis=0)
            imgl = tf.expand_dims(imgl, axis=0)
            
            if i == 0:
                batch_imgl = imgl
                batch_imgh = imgh
            else:
                batch_imgl = tf.concat([batch_imgl, imgl], 0)
                batch_imgh = tf.concat([batch_imgh, imgh], 0)
    
        return batch_imgl, batch_imgh
    
    def on_epoch_end(self):
        if self.shuffle: np.random.shuffle(self.findx)
            
    def __add__(self, that):
        fnList = list(set(self.fnList) + set(that.fnList))
        self.fnList = fnList
        self.findx = np.arange(len(fnList))
        return self
    
    def __sub__(self, that):
        fnList = list(set(self.fnList) - set(that.fnList))
        self.fnList = fnList
        self.findx = np.arange(len(fnList))
        return self

    
# Collect filenames into a list
def readfiles(datapath):
    list_file = glob.iglob(datapath)
    fnlist = []
    for filename in list_file:
        fnlist.append(filename)
    
    return fnlist


def get_sentinel2_data(filepath, scale=2, batch_size=4):

    filepath = filepath + '/*.png'
    list_train = readfiles(filepath)
    
    train_ds = Dataseq(list_train, scale=scale, batch_size=batch_size)
    
    return train_ds, list_train

