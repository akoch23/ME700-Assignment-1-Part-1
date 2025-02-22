import numpy as np

def calc_residual(x, residual):
# Function that calculates the Residual vector R for a given input x (which may be a single value or array of values constituting the "guess" value(s) for function convergence.)

# Check if residual is callable or a valid array
    if not callable(residual) and not isinstance(residual, np.ndarray):
        print("ERROR: residual must be either a callable function or an array.")
        return None
        
# Determine the number of residuals to calculate  
    R_rows = np.size(residual)
    
    R = np.zeros(R_rows)

    iterations = 0
    for func in residual:
        R[iterations] = func(x)
        iterations += 1
        
    return R

def calc_jacobian(x, jacobian):
# Function that calculates the Jacobian matrix J for the same input x (which is a matrix containing the partial derivatives of the mathematical function(s)
    
# Check if jacobian is callable or a valid array
    if not callable(jacobian) and not isinstance(jacobian, np.ndarray):
        print("ERROR: jacobian must be either a callable function or an array.")
        return None
        
# Determine the number of rows and columns in the Jacobian matrix
    J_rows = np.size(jacobian, 0)
    J_cols = np.size(jacobian, 1)

# Initialize the Jacobian matrix as zeros
    J = np.zeros((J_rows, J_cols))

# Loop over rows and columns to compute each Jacobian element, evaluating each function at x
    iterations = 0
    for rows in range(J_rows):
        for cols in range(J_cols):  # Added the inner loop for columns
            J[rows, cols] = jacobian[rows][cols](x)
            
    return J


def newtons_method(x, residual, jacobian, tol, iterations_max):
# Check for valid tol and iterations_max
    if not isinstance(iterations_max, int) or iterations_max <= 0:
        print("ERROR: iterations_max must be a positive integer.")
        return None
    if tol <= 0:
        print("ERROR: tol must be a positive number.")
        return None
# Check input type for residual and jacobian
    if np.size(residual) > 1:
        R = calc_residual(x,residual)
        J = calc_jacobian(x, jacobian)
        J_inv = np.linalg.inv(J)
        
    else:
        # In the case of a single residual
        R = residual(x)
        J = jacobian(x)
        try:
            J_inv = np.linalg.inv(J)
        except np.linalg.LinAlgError:
            print("ERROR: Jacobian matrix is singular and cannot be inverted.")
            return None

    # Initialize iteration process
    iter = 1
    while np.linalg.norm(R) > tol and iter <= iterations_max:
        x = x - np.dot(J_inv, R)
        if np.size(residual) > 1:
            R = calc_residual(x, residual)
            J = calc_jacobian(x, jacobian)
            try:
                J_inv = np.linalg.inv(J)
            except np.linalg.LinAlgError:
                print("ERROR: Jacobian matrix is singular and cannot be inverted.")
                return None
        else:
            R = residual(x)
            J = jacobian(x)
            try:
                J_inv = np.linalg.inv(J)
            except np.linalg.LinAlgError:
                print("ERROR: Jacobian matrix is singular and cannot be inverted.")
                return None
            
        iter += 1
        if iter > iterations_max:
            # Check if maximum number of iterations is exceeded
            print("ERROR: Maximum number of iterations exceeded.")

        if np.linalg.norm(R) > tol:
            # If convergence is not reached
            print("ERROR: Newton's method did not converge within the maximum iterations.")
            return None

    # Output the result (solution) after convergence
    result = print("By iteration ", iter, "the solution is: ", x)
    return x




