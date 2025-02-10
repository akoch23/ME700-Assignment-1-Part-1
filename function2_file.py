#!/usr/bin/env python
# coding: utf-8

# In[3]:


def newton_function_1(x: float):
    # Example Parabolic Function
    # Given a float value, will substitute it for variables in below equation and return value. Used to determine the values of f(a), f(b), and f(c) 
    function_1 = (x)**3 - 4*(x**2) + 1
    return function_1


# In[4]:


def newton_function_1_prime(x: float):
    # Derivative of newton_function_1
    function_1_prime = 3*(x**2) - 8*(x)
    return function_1_prime


# In[ ]:


def newton_function_2(x: float):
    # Example Parabolic Function
    function_2 = (x)**7 - 1000
    return function_2


# In[ ]:


def newton_function_2_prime(x: float):
    # Derivative of newton_function_2
    function_2_prime = 7*(x**6)
    return function_2_prime


# In[ ]:


def newton_function_3(x: float):
    # Example Parabolic Function
    function_3 = x**5 - 5*x + 3
    return function_3


# In[ ]:


def newton_function_3_prime(x: float):
    # Derivative of newton_function_3
    function_3_prime = 5*(x**4) - 5
    return function_3_prime


# In[ ]:


def newton_function_4(x: float):
    # Simple Mechanics Problem: A ball is thrown straight up, from 3 meter above the ground with a velocity of approximately 14 m/s. When will it hit the ground? (Test a x_0 value near 10)
    function_4 = -5*(x**2) + 14*x + 3
    return function_4


# In[ ]:


def newton_function_4_prime(x: float):
    # Derivative of newton_function_4
    function_4_prime = -10*x + 14
    return function_4_prime


# In[ ]:


# def newton_function_5(x: float):
    # Example Parabolic Function
    # Given a float value, will substitute it for variables in below equation and return value. Used to determine the values of f(a), f(b), and f(c) 
   # function_5 = x**5 - 5*x + 3
   # return function_5


# In[ ]:


# def newton_function_5_prime(x: float):
    # Derivative of base_function_1
    # Given a float value, will substitute it for variables in below equation and return value. Used to determine the values of f(a), f(b), and f(c) 
   # function_5_prime = 5*(x**4) - 5
   # return function_5_prime


# In[5]:


def newton_method(x:float, i:float):
    for iterations in range(0,i):
        y = main_function(x)
        z = prime_function(x)
    
        x_n = x - (y/z)
        print(f"Iteration {iterations + 1}: x_{iterations + 1} = {x_n}, f(x)= {main_function(x)}")
        x = x_n
    return x_n

