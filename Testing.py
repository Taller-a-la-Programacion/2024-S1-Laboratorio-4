import Laboratorio4;
import pytest;
    
def test_conservarPrimos_1():
    assert Laboratorio4.conservarPrimos( [5, 78, 12, 0, 11, 12, 12]  ) == [5, 11]
    
def test_conservarPrimos_2():
    assert Laboratorio4.conservarPrimos( [12, 1, 12] ) == [ 5.2]
######################################################################    
def test_sumaImparesPares_1():
    assert Laboratorio4.sumaImparesPares([0,2], [4, 8, 6, 0]) == [10, 10]
    
def test_sumaImparesPares_2():
    assert Laboratorio4.sumaImparesPares([10, 0], [100, 2]) == [110, 2]
######################################################################        
def test_sumaImparesPares_3():
    assert isinstance(Laboratorio4.sumaImparesPares([1,2], "dos"), str) == isinstance("Error: segundo argumento debe ser entero", str)
    
def test_convertirBase_1():
    assert Laboratorio4.convertirBase([0,0,1,0] , 2, 10) == 2

def test_convertirBase_2():
    assert Laboratorio4.convertirBase([2] , 10, 2) == 10

def test_convertirBase_3():
    assert Laboratorio4.convertirBase(["F","F","F"] , 16, 10) == 4095
    
def test_convertirBase_4():
    assert Laboratorio4.convertirBase([4,0,9,5] , 10, 16) == "FFF"
