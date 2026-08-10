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
   
    #CORLANC_Abril
    def test_comprobar_valor_corlanc_abril(self):
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

    #CORLANC_Enero_Febrero_Marzo
    def test_comprobar_valor_corlanc_enero_febrero_marzo(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 738958
        iva: float = 140402

        #Establecer datos de salida esperada
        valor_total_esperado = 879360
        valor_total = round(valor_total_esperado)
   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)
   
        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(round(valor_calculado),valor_total)

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

    #SUMINISTROS DE COLOMBIA S.A.S (MATERIALES Y PINTURAS SABANETA)
    def test_comprobar_valor_materiales_pinturas_sabaneta_abril(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 411188
        iva: float = 78126
               
        #Establecer datos de salida esperada
        valor_total_esperado = 489314
               
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)
               
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S (MATERIALES Y PINTURAS SABANETA)
    def test_comprobar_valor_materiales_pinturas_sabaneta_enero_febrero_marzo(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 1330123
        iva: float = 252723

        #Establecer datos de salida esperada
        valor_total_esperado = 1582846      
                   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)
                   
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S (MATERIALES Y PINTURAS SABANETA)
    def test_comprobar_valor_moldes_itagui_enero_febrero_marzo(self):
        #Establecer datos de entrada
        n_servicios: int = 3
        precio_unitario: float = 394110
        iva: float = 224643

        #Establecer datos de salida esperada
        valor_total_esperado = 1406973      
                   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)
                   
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S - CALCINACIÓN ENE FEB MAR
    def test_comprobar_valor_calcinacion_enero_febrero_marzo(self):
        #Establecer datos de entrada
        n_servicios: int = 3
        precio_unitario: float = 1576442
        iva: float = 898572

        #Establecer datos de salida esperada
        valor_total_esperado = 5627898      
                   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)
                   
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S - CALCINACIÓN ABR MAY JUN
    def test_comprobar_valor_calcinacion_abril_mayo_junio(self):
        #Establecer datos de entrada
        n_servicios: int = 3
        precio_unitario: float = 145125
        iva: float = 82721

        #Establecer datos de salida esperada
        valor_total_esperado = 518096      
                   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)
                   
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

"""#CASOS DE ERROR

    #SUMINISTROS DE COLOMBIA S.A.S - CALCINACIÓN ABR MAY JUN (ERROR EN # SERVICIOS)
    def test_comprobar_valor_calcinacion_abril_mayo_junio(self):
        #Establecer datos de entrada
        n_servicios: int = 0
        precio_unitario: float = 145125
        iva: float = 82721

        #Establecer datos de salida esperada
        valor_total_esperado = 518096      
                   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)
                   
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #LOCERIA (PRECIO UNITARIO)
    def test_comprobar_valor_loceria(self):

        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 0
        iva: float = 661770

        #Establecer datos de salida esperada
        valor_total_esperado =  4144770

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(valor_calculado,valor_total_esperado)
"""


if __name__ == '__main__':
    unittest.main()
