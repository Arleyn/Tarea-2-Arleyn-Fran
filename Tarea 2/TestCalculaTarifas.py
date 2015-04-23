'''
Created on 22/4/2015

@author: Arleyn Goncalves 10-10290
         Francisco Sucre  10-10717
'''

import unittest
import datetime
import CalculaTarifas

class Test(unittest.TestCase):

    def testCalcularPrecios(self):
        pass
    
    def testTarifaNula(self):
        tarifa = CalculaTarifas.Tarifa(0,0);
        tiempo = [datetime.datetime(2015,4,20,0,0,0),
                                    datetime.datetime(2015,4,27,0,0,0)];
        self.assertEqual(0,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba Frontera lo minimo son 15 dias en un dia de semana
    
    def test15MinutosSemana(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,21,16,0,0),
                                    datetime.datetime(2015,4,21,16,15,0)];
        
        self.assertEqual(5,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba Frontera lo minimo son 15 dias en un fin de semana
        
    def test15MinutosFinSemana(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,25,16,0,0),
                                    datetime.datetime(2015,4,25,16,15,0)];
        
        self.assertEqual(10,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba 5 dias exacto de Lunes a Viernes
        
    def test5DiasSemanaExacto(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,20,0,0,0),
                                    datetime.datetime(2015,4,25,0,0,0)];
        
        self.assertEqual(600,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba 2 dias exactos de Sabado a Domingo
        
    def test2DiasFinSemanaExacto(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,25,0,0,0),
                                    datetime.datetime(2015,4,27,0,0,0)];
        
        self.assertEqual(480,CalculaTarifas.calcularPrecio(tarifa,tiempo))
        
    # Prueba de 1 hora y 1 minuto, probar que se cobra 2 horas

    def test1hora1minuto(self):
        
        tarifa = CalculaTarifas.Tarifa(5,10);
        tiempo = [datetime.datetime(2015,4,21,16,0,0),
                                    datetime.datetime(2015,4,21,17,1,0)];
        
        self.assertEqual(10,CalculaTarifas.calcularPrecio(tarifa,tiempo))        
    
if __name__ == "__main__":
#import sys;sys.argv = ['', 'Test.testName']
    unittest.main()


