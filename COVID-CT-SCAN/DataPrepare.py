import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd

covid = os.listdir('Explo/DataSet/COVID')
non_covid = os.listdir('Explo/DataSet/non-COVID')

# print(len(covid), len(non_covid))

lst_X = []
lst_y = []

def Prepare (folder_name, label, img_size, img_shape):
    '''
    Given the folder ('folder_name'), the function accesses
    the images in the folder, converts them into gray scale,
    resizes them according to the given shape and size ('img_size'
    and 'img_shape'), stores the pixels in a numpy array. Further 
    it appends the flattend_pixels into the list 'lst_X' and the
    corresponding label to 'lst_y'.
    '''
    str = ""
    if folder_name == covid:
        str = "COVID"
    else:
        str = "non-COVID"
    for images in folder_name:
        path = 'Explo/DataSet/' + str + '/' + images
        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        reshaped = cv2.resize(gray, img_shape)
        pixels = np.array(reshaped)
        pixels_flat = np.reshape(pixels, img_size)
        lst_X.append(pixels_flat)
        lst_y.append(label)

Prepare(covid, 1, 10000, (100, 100))
Prepare(non_covid, 0, 10000, (100, 100))

# print(len(X), len(X[0]), len(y))

arr_X = np.array(lst_X, dtype = np.uint8)
arr_y = np.array(lst_y, dtype = np.uint8)

'''
arr = X[0]
arr = np.reshape(arr, (50, 50))
cv2.imshow('1', arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
''' 

df_X = pd.DataFrame(arr_X)
df_X.to_csv('Explo/X100.csv')
df_y = pd.DataFrame(arr_y)
df_y.to_csv('Explo/y100.csv')
