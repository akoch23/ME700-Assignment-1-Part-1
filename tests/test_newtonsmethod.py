import numpy as np
import src.newtonMethod as newt
import pytest
 

def test_calc_resid():

    def fnR0(x,y,z=0):
        fnR0 = x**2 - 1 + y
        return fnR0

    def fnR1(x,y,z=0):
        fnR1 = y**3 -1
        return fnR1

    fnR = [fnR0,fnR1]

    known = np.array([[6], [26]])
    found = newt.calc_resid(np.array([[2],[3],[0]]),fnR)
    assert (known==found).all()
    
def test_calc_jacob():

    def fnJ00(x,y,z=0):
        fnJ00 = 2*x
        return fnJ00

    def fnJ10(x,y,z=0):
        fnJ10 = 1
        return fnJ10

    def fnJ01(x,y,z=0):
        fnJ01 = 0
        return fnJ01

    def fnJ11(x,y,z=0):
        fnJ11 = 3*y**2
        return fnJ11

    # combine into matrix rows
    fnJ = [[fnJ00, fnJ01],[fnJ10, fnJ11]]
    #fnJ1 = [fnJ10, fnJ11]
    #fnJ2 = 
    
    known = np.array([[4, 0],[1,27]])
    found = newt.calc_jacob(np.array([[2],[3]]),fnJ)
    assert (known==found).all()

def test_maxIterReached():
    with pytest.raises(SystemExit):
        newt.maxIterReached(10,10,7)
    known = 7
    found = newt.maxIterReached(9,10,7)
    assert known == found

def test_nIterMaxCheck():
    with pytest.raises(SystemExit):
        newt.nIterMaxCheck(-1)
    
    known = "PASS: nIterMax is positive whole number"
    found = newt.nIterMaxCheck(10)
    assert known == found

def test_newtonMethodFunc():
    
    x = np.array([2])
    
    def fnR(x):
        fnR = x**3-2+x
        return fnR

    def fnJ(x):
        fnJ = 3*x**2+1
        return fnJ
    
    result = newt.newtonMethodFunc(x,fnR,fnJ)
    found = result["solution"]
    known = 1

    assert np.allclose(known,found,rtol=1e-4,atol=1e-5)

def test_newtonMethodFunc_2D():
    
    x = np.array([[2], [4]])    # initial guess
    tol = 1e-9                  # tolerance
    maxIter = 1000              # max number of iterations

    # function of interest (fnR) and its derivative (fnJ)
    def fnR0(x,y,z=0):
        fnR0 = x**3 + y - 2
        return fnR0

    def fnR1(x,y,z=0):
        fnR1 = -x + y**3 + 3
        return fnR1

    fnR = [fnR0, fnR1]

    def fnJ00(x,y,z=0):
        fnJ00 = 3*x**2 
        return fnJ00

    def fnJ10(x,y,z=0):
        fnJ10 = 1
        return fnJ10

    def fnJ01(x,y,z=0):
        fnJ01 = -1
        return fnJ01

    def fnJ11(x,y,z=0):
        fnJ11 = 3*y**2
        return fnJ11

    fnJ = [[fnJ00, fnJ01], [fnJ10, fnJ11]]

    
    result = newt.newtonMethodFunc(x,fnR,fnJ)
    found = result["solution"]
    known = np.array([[1.46639344],[-1.1532005]])

    assert np.allclose(known,found,rtol=1e-4,atol=1e-5)
