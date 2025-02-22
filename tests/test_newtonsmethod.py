import numpy as np
import newtonsmethod_main as nms
import pytest
 

def test_calc_residual():
    # Define sample residual functions
    def residual_1(x):
        return x[0] ** 2 + x[1] ** 2 - 1

    def residual_2(x):
        return x[0] - x[1] ** 2

    residual = [residual_1, residual_2]

    x = np.array([1.0, 0.5])

    known = np.array([0.0, 0.25])  # Residual for x = [1.0, 0.5]
    found = nms.calc_residual(x, residual)


def test_calc_jacobian():
    # Define sample Jacobian functions
    def jacobian_1(x):
        return 2 * x[0]

    def jacobian_2(x):
        return 2 * x[1]

    def jacobian_3(x):
        return 1

    def jacobian_4(x):
        return -2 * x[1]

    jacobian = [[jacobian_1, jacobian_2], 
                [jacobian_3, jacobian_4]
               ]

    x = np.array([1.0, 0.5])

    known = np.array([[2.0, 1.0], [1.0, -1.0]])  # Jacobian for x = [1.0, 0.5]
    found = nms.calc_jacobian(x, jacobian)


def test_newtons_method():
    # Define residual and Jacobian functions
    def residual_1(x):
        return x[0] ** 2 + x[1] ** 2 - 1

    def residual_2(x):
        return x[0] - x[1] ** 2

    residual = [residual_1, residual_2]

    def jacobian1_1(x):
        return 2 * x[0]

    def jacobian1_2(x):
        return 2 * x[1]

    def jacobian_3(x):
        return 1

    def jacobian_4(x):
        return -2 * x[1]

    jacobian = [[jacobian_1, jacobian_2], 
                [jacobian_3, jacobian_4]
               ]

    # Set initial guess
    x0 = np.array([1.0, 0.5])
    tol = 1e-6
    iter_max = 100

    result = nms.newtons_method(x0, residual, jacobian, tol, iter_max)

    # Check the result
    known_result = np.array([1.0, 0.0])  # Expected solution for this system of equations
    assert np.allclose(known_result, result, atol=1e-6), f"Expected {known_result}, but got {result}"


def test_newtons_method_convergence():
    # Test for convergence behavior of Newton's Method
    
    def residual_s1(x):
        return x[0] ** 3 - x[1]

    def residual_s2(x):
        return x[0] - x[1] ** 2

    residual = [residual_s1, residual_s2]

    def jacobian_s1(x):
        return 3 * x[0] ** 2

    def jacobian_s2(x):
        return -1

    def jacobian_s3(x):
        return 1

    def jacobian_s4(x):
        return -2 * x[1]

    jacobian = [[jacobian_s1, jacobian_s2], 
                [jacobian_s3, jacobian_s4]
               ]

    # Set initial guess
    x0 = np.array([2.0, 1.0])
    tol = 1e-6
    iter_max = 100

    result = nms.newtons_method(x0, residual, jacobian, tol, iter_max)

    known_result = np.array([1.0, 1.0])  # Expected solution for this system of equations
    assert np.allclose(known_result, result, atol=1e-6), f"Expected {known_result}, but got {result}"


def test_newtons_method_fail():
    # Test scenario where solver output doesn't converge within maximum allowable iterations

    def residual_f1(x):
        return x[0] ** 3 - x[1]

    def residual_f2(x):
        return x[0] - x[1] ** 2

    residual = [residual_f1, residual_f2]

    def jacobian_f1(x):
        return 3 * x[0] ** 2

    def jacobian_f2(x):
        return -1

    def jacobian_f3(x):
        return 1

    def jacobian_f4(x):
        return -2 * x[1]

    jacobian = [[jacobian_f1, jacobian_f2], 
                [jacobian_f3, jacobian_f4]
               ]

    # Set initial guess that is unlikely to converge
    x0 = np.array([1e6, 1e6])
    tol = 1e-6
    iter_max = 10  # Set small number of iterations to trigger failure

    result = nms.newtons_method(x0, residual, jacobian, tol, iter_max)

    # Failure is expected, check if result is None (i.e., convergence not reached)
    assert result is None, "Expected failure (None result), but got a solution"
