
import numpy as np

def calc_residual(x, residual):
# Function that calculates the Residual vector R for a given input x (which may be a single value or array of values constituting the "guess" value(s) for function convergence.)

# Determine the number of residuals to calculate  
    if isinstance(residual, list):
        R_rows = len(residual)  # Number of residual functions
    elif callable(residual):
        R_rows = 1  # Only one residual function

    R = np.zeros(R_rows)
    for i, func in enumerate(residual):
        R[i] = func(x)  # Compute residual for each function

    return R
        
def calc_jacobian(x, jacobian):
# Function that calculates the Jacobian matrix J for the same input x (which is a matrix containing the partial derivatives of the mathematical function(s)
    
    if isinstance(jacobian, list) and isinstance(jacobian[0], list):
        J_rows = len(jacobian)  # Number of rows in Jacobian matrix
        J_cols = len(jacobian[0])  # Number of columns in Jacobian matrix
    elif callable(jacobian):
        J_rows = J_cols = 1  # Single Jacobian function (in case of 1D problem)
        
    J = np.zeros((J_rows, J_cols))
    for i in range(J_rows):
        for j in range(J_cols):
            J[i, j] = jacobian[i][j](x)  # Compute each Jacobian element

    return J


def newtons_method(x, residual, jacobian, tol, iter_max):
# Check for valid iteration and tolerance values
    if not isinstance(iter_max, int) or iter_max <= 0:
        print("ERROR: iterations_max must be a positive integer.")
        return None
    if tol <= 0:
        print("ERROR: tol must be a positive number.")
        return None
# Check input type for residual and jacobian

    R = calc_residual(x,residual)
    J = calc_jacobian(x, jacobian)
    
    print("Initial residual:", R)
    print("Initial Jacobian:", J)
    
    try:
        J_inv = np.linalg.inv(J)
    except np.linalg.LinAlgError:
        print("ERROR: Jacobian matrix is singular and cannot be inverted.")
        return None

    # Initialize iteration process
    iter = 1
    while np.linalg.norm(R) > tol and iter <= iter_max:
        print("Initial residual norm:", np.linalg.norm(R))
        x_new = x - np.dot(J_inv, R)
        R = calc_residual(x_new, residual)
        J = calc_jacobian(x_new, jacobian)
        
        print(f"Iteration {iter}:")
        print("Residual:", R)
        print("Jacobian:", J)
        
        
        try:
            J_inv = np.linalg.inv(J)
        except np.linalg.LinAlgError:
            print("ERROR: Jacobian matrix is singular and cannot be inverted.")
            return None
 
            
        iter += 1
        if iter > iter_max:
            # Check if maximum number of iterations is exceeded
            print("ERROR: Maximum number of iterations exceeded.")

        if np.linalg.norm(R) <= tol:
            # If convergence is not reached
            print("ERROR: Newton's method did not converge within the maximum iterations.")
            return None

    # Output the result (solution) after convergence
    result = print("By iteration ", iter, "the solution is: ", x_new)
    return x_new
