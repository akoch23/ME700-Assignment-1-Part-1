#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def calc_residual(x, residual):

    R_rows = np.size(residual)
    
    R = np.zeros(R_rows)

    iterations = 0
    for func in residual:
        R[iterations] = func(x)
        iterations += 1
        
    return R

def calc_jacobian(x, jacobian):
    J_rows = np.size(jacobian, 0)
    J_cols = np.size(jacobian, 1)
    
    J = np.zeros((J_rows, J_cols))
    
    iterations = 0
    for rows in range(J_rows):
        for cols in range(J_cols):  # Added the inner loop for columns
            J[rows, cols] = jacobian[rows][cols](x)
            
    return J


def newtons_method(x, residual, jacobian, tol, iterations_max):
    
    if np.size(residual) > 1:
        R = calc_residual(x,residual)
        J = calc_jacobian(x, jacobian)
        J_inv = np.linalg.inv(J)
        
    else:
        R = residual(x)
        J = jacobian(x)
        J_inv = np.linalg.inv(J)

    
    iter = 1
    while np.linalg.norm(R) > tol and iter <= iterations_max:
        x = x - np.dot(J_inv, R)
        if np.size(residual) > 1:
            R = calc_residual(x, residual)
            J = calc_jacobian(x, jacobian)
            J_inv = np.linalg.inv(J)
        else:
            R = residual(x)
            J = jacobian(x)
            J_inv = np.linalg.inv(J)
            
        iter += 1
        
        if iter > iterations_max:
            print("ERROR: Maximum number of iterations exceeded.")
    
    result = print("By iteration ", iter, "the solution is: ", x)
    return x


# In[ ]:




