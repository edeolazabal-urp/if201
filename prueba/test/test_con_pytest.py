'''
Modulo de Prueba Unitaria con PyTest
Fecha 09-09-2024
'''
import pytest
from prueba.programa import suma, es_mayor

def test_suma_negativo():
    assert suma(-1,-5) == -6

def test_suma_positiva():
    assert suma(6,3) == 9

def test_suma_dentro_de_un_rango():
    resultado = suma(4,2)
    valores = [1,2,3,5,6]
    assert resultado in valores

def test_verifica_si_es_mayor():
       assert es_mayor(10,5)

def test_verifica_que_no_es_mayor():
       assert not es_mayor(2,8)
