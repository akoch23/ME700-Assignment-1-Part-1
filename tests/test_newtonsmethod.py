import numpy as np
import src/newtonsmethod.newtonsmethod_main as nms
import pytest
 

def test_calc_residual():

    def func_1(x):
        func_1 = x**4 - 2 + y
        return func_1

    def func_2(x):
        func_2 = y**2 + 1
        return func_2

    residual = [func_1,func_2]

    known = np.array([[],[]])

    
def test_calc_jacobian():

    def df1_dx1(x):
        df1_dx1 = 2*x
        return df1_dx1

    def df1_dx2(x):
        df1_dx2 = 1
        return df1_dx2

    def df2_dx2(x):
        df2_dx2 = 0
        return df2_dx2

    def df2_dx2(x):
        df2_dx2 = 3*y**2
        return df2_dx2


def test_newtons_method():
    
   
