#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
get_ipython().run_line_magic('run', 'newtonsmethod_main.ipynb')


x_0 = np.array([1.0, 0.5])
tol = 1e-6
iterations_max = 1000

def func_1(x):
    func_1 = x[0]**2 - x[1]**2 - 1
    return func_1

def func_2(x):
    func_2 = x[0]**3 + x[1]**2
    return func_2

residual = [func_1, func_2]
                      
                      
def df1_dx1(x):
    df1_dx1 = 2*x[0]
    return df1_dx1
def df1_dx2(x):
    df1_dx2 = -2*x[1]
    return df1_dx2
def df2_dx1(x):
    df2_dx1 = 3*x[0]
    return df2_dx1
def df2_dx2(x):
    df2_dx2 = 2*x[1]
    return df2_dx2
        
jacobian = [
    [df1_dx1, df1_dx2],
    [df2_dx1, df2_dx2]
]
                      

result = newtons_method(x_0, residual, jacobian, tol, iterations_max)
print(result)


# In[ ]:




