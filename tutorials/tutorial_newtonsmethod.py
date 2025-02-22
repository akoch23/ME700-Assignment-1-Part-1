
NOTE: PLEASE USE/PASTE ONLY THE CODE FOR A SINGULAR EXAMPLE AT A TIME, DO NOT ATTEMPT TO RUN THE ENTIRE FILE.
----------------------------------------------------------------------------------------------------------------------------
# Import necessary pacakges
import numpy as np
import newtonsmethod_main as nms

# Example 1: Simple System of Polynomial Equations #1

# Define functions and user inputs
x = np.array([1.0, 0.5]) # Initial guess
tol = 1e-6 # Tolerance value
iterations_max = 1000 # Maximum iterations

# Defining function(s) of interest (for Residual) and its derivative(s) (for Jacobian)
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

# Call Newton's Method solver function from main solver file and print result
result = nms.newtons_method(x, residual, jacobian, tol, iterations_max)
print(result)

---------------------------------------------------------------------------------------------------------------------------------
# Import necessary pacakges
import numpy as np
import newtonsmethod_main as nms

# Example 2: Simple Polynomial Equation

# Define functions and user inputs
x = np.array([2])
tol = 1e-8
iterations_max = 1000

# Defining function(s) of interest (for Residual) and its derivative(s) (for Jacobian)
def residual(x):
    residual = x**3 + x - 2
    return residual
                                            
def jacobian(x):
    jacobian = 3*(x**2) + 1
    return jacobian

# Call Newton's Method solver function from main solver file and print result
result = nms.newtons_method(x, residual, jacobian, tol, iterations_max)
print(result)

-----------------------------------------------------------------------------------------------------------------------------
# Import necessary pacakges
import numpy as np
import newtonsmethod_main as nms

# Example 3: Spring Energy Equation:

# Define functions and user inputs
x = np.array([2])
tol = 1e-8
iterations_max = 1000

# Define other necessary constants: k = spring constant, x_0 = initial displacement, U_s = spring potential energy
k  = 10
x_0 = 0.1
U_s = 0.05 J

# Defining function(s) of interest (for Residual) and its derivative(s) (for Jacobian)
def residual(x):
    residual = 1/2 * k * (x_0**2 - x**2) - U_s
    return residual
                                            
def jacobian(x):
    jacobian = k*x
    return jacobian

# Call Newton's Method solver function from main solver file and print result
result = nms.newtons_method(x, residual, jacobian, tol, iterations_max)
print(result)

-----------------------------------------------------------------------------------------------------------------------------
# Import necessary pacakges
import numpy as np
import newtonsmethod_main as nms

# Example 4: Kinematic Energy Equation:

# Define functions and user inputs
x = np.array([2])
tol = 1e-8
iterations_max = 1000

# v_i = initial velocity of object
v_i = 0
# a = acceleration of object
a = 2
# delta_x = displacement
delta_x = 1600

# Defining function(s) of interest (for Residual) and its derivative(s) (for Jacobian)
def residual(x):
    residual = v_i*x + 1/2*a*x**2 - delta_x
    return residual
                                            
def jacobian(x):
    jacobian = a*x
    return jacobian

# Call Newton's Method solver function from main solver file and print result
result = nms.newtons_method(x, residual, jacobian, tol, iterations_max)
print(result)

----------------------------------------------------------------------------------------------------------------------------
# Import necessary pacakges
import numpy as np
import newtonsmethod_main as nms

# Example 5: Bernoulli's Equation

# Define functions and user inputs
x = np.array([2])
tol = 1e-8
iterations_max = 1000

# Static Pressure at Point 1
p_1 = 1e6
# rho (density of fluid)
rho = 800
# Volume at Point 1
v_1 = 15
# Static Pressure at Point 2
p_2 = 4e6

# Defining function(s) of interest (for Residual) and its derivative(s) (for Jacobian)
def residual(x):
    residual = p_1 + 1/2*rho*(v_1**2) - p_2 - 1/2*rho*(x**2)
    return residual
                                            
def jacobian(x):
    jacobian = rho*x
    return jacobian

# Call Newton's Method solver function from main solver file and print result
result = nms.newtons_method(x, residual, jacobian, tol, iterations_max)
print(result)
