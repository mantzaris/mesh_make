#!/usr/bin/env python
"""
EX. from .py import fn
#the rows of the mat correspond to the X-axis
#the cols to the Y-axis
#the matrix entries to the Z-axis values
#the first index for the mat is the top left
"""
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#produce a mesh from the mat
def im2mesh( mat):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)

    X_num = mat.shape[0]
    Y_num = mat.shape[1]
    #each X1 row is a repeat, as many rows as Y values
    X1 = np.tile(np.array(range(X_num)),(Y_num,1))
    #each Y1 column is constant
    Y1 = np.transpose(np.tile(np.array(range(Y_num)),(X_num,1)))
    #the structure of the needed points
    Z1 = np.transpose(mat)#np.random.rand(Y_num,X_num)
    print(X1)
    print(Y1)
    print(Z1)
    ax.plot_wireframe(X1, Y1, Z1, rstride=10, cstride=10)
    plt.show()
