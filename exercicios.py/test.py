

#comandos para instalar o pytest:
#pip install pytest
#python -m pytest .\test.py

import pytest
from src.operacoes import soma
def test_soma_deve_somar_dois_numeros():
    #Arrange (organiza)
    a,b = 2,3
    #Act (Agir)
    resultado = soma(a,b)
    assert resultado == 5
#Forma mais profissional ao inves de escrever vaios testes
@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (2,3,5), #Soma positivos
     (0,0,0), #Soma zeros
     (1,5,2.5,4.0), #Soma floats
    ],
)
def test_soma_varios_casos(a,b, esperado):
    assert soma(a,b) == esperado