#!/usr/bin/env python
"""
#the rows of the mat correspond to the X-axis
#the cols to the Y-axis
#the matrix entries to the Z-axis values
#the first index for the mat is the top left
#x_pnts and y_pnts are optional positions of these coordinates
"""
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#produce a mesh from the mat
def im2mesh(mat,x_pnts=-1,y_pnts=-1):
    X_num = mat.shape[0]
    Y_num = mat.shape[1]       
    if(isinstance(x_pnts,int)):
        x_pnts = np.array(range(X_num))
    if(isinstance(y_pnts,int)):
        y_pnts = np.array(range(Y_num))    
    X1 = np.tile(x_pnts,(Y_num,1))    
    Y1 = np.transpose(np.tile(y_pnts,(X_num,1)))    
    Z1 = np.transpose(mat)    
    return X1,Y1,Z1


def im2wireframe(mat,x_pnts=-1,y_pnts=-1):
    X1,Y1,Z1 = im2mesh(mat,x_pnts,y_pnts)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')    
    ax.plot_wireframe(X1, Y1, Z1, rstride=10, cstride=10)
    plt.show()
