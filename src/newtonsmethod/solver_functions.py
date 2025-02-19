


def example_SOE_1(x: float):
    function_1 = x[1]**3 - 4*x[2]**2 + 1
    function_2 = 3*x[1] - 8*x[2]
    return example_SOE_1

'''
def newton_function_2(x: float):
    # Example Parabolic Function
    function_2 = (x)**7 - 1000
    return function_2


def newton_function_2_prime(x: float):
    # Derivative of newton_function_2
    function_2_prime = 7*(x**6)
    return function_2_prime


def newton_function_3(x: float):
    # Example Parabolic Function
    function_3 = x**5 - 5*x + 3
    return function_3

def newton_function_3_prime(x: float):
    # Derivative of newton_function_3
    function_3_prime = 5*(x**4) - 5
    return function_3_prime


def newton_function_4(x: float):
    # Simple Mechanics Problem: A ball is thrown straight up, from 3 meter above the ground with a velocity of approximately 14 m/s. When will it hit the ground? (Test a x_0 value near 10)
    function_4 = -5*(x**2) + 14*x + 3
    return function_4


def newton_function_4_prime(x: float):
    # Derivative of newton_function_4
    function_4_prime = -10*x + 14
    return function_4_prime


# def newton_function_5(x: float):
    # Example Parabolic Function
    # Given a float value, will substitute it for variables in below equation and return value. Used to determine the values of f(a), f(b), and f(c) 
   # function_5 = x**5 - 5*x + 3
   # return function_5


# def newton_function_5_prime(x: float):
    # Derivative of base_function_1
    # Given a float value, will substitute it for variables in below equation and return value. Used to determine the values of f(a), f(b), and f(c) 
   # function_5_prime = 5*(x**4) - 5
   # return function_5_prime
'''

def compute_residual(x):
    residuals = np.array(
    return residuals

def compute_jacobian(x):
    n = len(x)
    jacobian = np.zeros((n,n))

    epsilon = 1e-6
    for i in range(n):
        x_perturbed = x.copy()
        x_perturbed[i] += epsilon
        jacobian[:, i] = (compute_residual(x_perturbed) - compute_residual(x)) / epsilon
    return jacobian

def newton_method(initial_guess, tolerance=1e-6, max_iter=100):
    x = initial_guess
    for iteration in range(max_iter):
        R = compute_residual(x)
        J = compute_residual(x)

        try:
            delta_x = np.lingalg.solve(J, -R)


        x_new = x + delta_x

        if np.linalg.norm(R) < tolerance:
            print(f"Convergence reached after {iteration + 1} iterations.")
            return x_new
        
        x = x_new

    print("Max number of iterations reached.")
    return x

system_of_functions = [example_SOE_1.function_1, example_SOE_1.function_2]
initial_guess = np.array([1.0, 0.5])
solution = newtons_method(initial_guess)
print("Solution: ", solution)
