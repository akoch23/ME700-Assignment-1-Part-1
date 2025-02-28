# Newton's Method Solver

[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)




### Newton's Method Algorithm

**Newton's Method** is another numerial technique for finding the roots of a continuous function f(x). This method works by taking an initial guess (x_0), and uses the function f(x) and it's derivative f'(x) to iteratively estimate a value near the root until the actual root value is found (with sufficient accuracy witin some tolerance value).




### Conda environment installation and testing

To install this package, first establish a new conda environment:
```bash
conda create --name newtons-method-solver-env python=3.12
```
Afterwards, activate the environment:
```bash
conda activate newtons-method-solver-env
```

You can double check if the installed version of python is indeed version 3.12 in the new conda environment:
```bash
python --version
```

Ensure that pip is using the latest version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```

Create an editable install of the newton's method code (reminder: make sure you're in the right directory for this step, using the cd: [insert folder path] command)
```bash
pip install -e .
```

Test that the code is working with pytest:
```bash
pytest -v --cov=newtonsmethod --cov-report term-missing
```

Code coverage should be 100%


## Solver Description

### Variables

* `x`: initial guess, either a singular value or a pair in 1D array format
* `residual`: 1D array, containing function(s) to be solved
* `jacobian`: Jacobian matrix containing derivatives of functions in "residual"
* `iterations_max`: Maximum allowable iterations for the solver  
* `tol`: Desired tolerance amount for convergence  

### Files

* *src/newtonsmethod/newtonsmethod_main.py*: Contains main functions for iteratively calculating residual and jacobian matrices and implementing them in Newton's Method
* *tests/test_newtonsmethod.py*: Test commands for main file *newtonsmethod_main.py*
* *tutorial/tutorial_newtonsmethod.py*: Tutorial file containing five example problems that can be copied and run
