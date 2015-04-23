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
    
if __name__ == "__main__":
#import sys;sys.argv = ['', 'Test.testName']
    unittest.main()


