import unittest
import facturacion_sensores

class TestsFacturacion(unittest.TestCase):
    #GAMMA
    def test_comprobar_valor_gamma(self): 
    #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 1741500
        iva: float = 330885

        #Establecer datos de salida esperada
        valor_total_esperado = 2072385

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)
    
    #CORLANC
    def test_comprobar_valor_corlanc(self): 
    #Establecer datos de entrada
        n_servicios: int = 2
        precio_unitario: float = 241875
        iva: float = 91913

        #Establecer datos de salida esperada
        valor_total_esperado = 575662.5
        valor_total = round(valor_total_esperado)

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(valor_calculado,valor_total,0)

    #LOCERIA
    def test_comprobar_valor_loceria(self):

        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 3483000
        iva: float = 661770

        #Establecer datos de salida esperada
        valor_total_esperado =  4144770

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(valor_calculado,valor_total_esperado)

    #ENKA
    def test_comprobar_valor_enka(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 1680000
        iva: float = 319200

        #Establecer datos de salida esperada
        valor_total_esperado = 1999200

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)

    #CRYOGAS GATEWAYS
    def test_comprobar_valor_cryogas_gateways(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 6820000
        iva: float = 1295800

        #Establecer datos de salida esperada
        valor_total_esperado = 8115800

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)

    #CRYOGAS SENSOR
    def test_comprobar_valor_cryogas_sensor(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 1500000
        iva: float = 285000

        #Establecer datos de salida esperada
        valor_total_esperado = 1785000

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)

if __name__ == '__main__':
    unittest.main()
