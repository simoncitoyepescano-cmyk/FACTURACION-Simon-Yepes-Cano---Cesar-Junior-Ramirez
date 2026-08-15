import unittest
import src.model.facturacion_sensores as facturacion_sensores

class TestsFacturacion(unittest.TestCase):
    #GAMMA
    def test_comprobar_valor_gamma(self):
    #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 1741500

        #Establecer datos de salida esperada
        valor_total_esperado = 2072385
   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)
   
    #CORLANC_Abril
    def test_comprobar_valor_corlanc_abril(self):
    #Establecer datos de entrada
        n_servicios: int = 2
        precio_unitario: float = 241875

        #Establecer datos de salida esperada
        valor_total_esperado = 575662.5
        valor_total = round(valor_total_esperado)

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(valor_calculado,valor_total,0)

    #CORLANC_Enero_Febrero_Marzo
    def test_comprobar_valor_corlanc_enero_febrero_marzo(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 738958

        #Establecer datos de salida esperada
        valor_total_esperado = 879360
        valor_total = round(valor_total_esperado)
   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)
   
        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(round(valor_calculado),valor_total)

    #LOCERIA
    def test_comprobar_valor_loceria(self):

        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 3483000

        #Establecer datos de salida esperada
        valor_total_esperado =  4144770

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(valor_calculado,valor_total_esperado)

    #ENKA
    def test_comprobar_valor_enka(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 1680000

        #Establecer datos de salida esperada
        valor_total_esperado = 1999200

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)

    #CRYOGAS GATEWAYS
    def test_comprobar_valor_cryogas_gateways(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 6820000

        #Establecer datos de salida esperada
        valor_total_esperado = 8115800

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)

    #CRYOGAS SENSOR
    def test_comprobar_valor_cryogas_sensor(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 1500000

        #Establecer datos de salida esperada
        valor_total_esperado = 1785000

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado,valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S (MATERIALES Y PINTURAS SABANETA)
    def test_comprobar_valor_materiales_pinturas_sabaneta_abril(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 411188
               
        #Establecer datos de salida esperada
        valor_total_esperado = 489314
               
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)
               
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S (MATERIALES Y PINTURAS SABANETA)
    def test_comprobar_valor_materiales_pinturas_sabaneta_enero_febrero_marzo(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 1330123

        #Establecer datos de salida esperada
        valor_total_esperado = 1582846      
                   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)
                   
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S (MATERIALES Y PINTURAS SABANETA)
    def test_comprobar_valor_moldes_itagui_enero_febrero_marzo(self):
        #Establecer datos de entrada
        n_servicios: int = 3
        precio_unitario: float = 394110

        #Establecer datos de salida esperada
        valor_total_esperado = 1406973      
                   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)
                   
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S - CALCINACIÓN ENE FEB MAR
    def test_comprobar_valor_calcinacion_enero_febrero_marzo(self):
        #Establecer datos de entrada
        n_servicios: int = 3
        precio_unitario: float = 1576442

        #Establecer datos de salida esperada
        valor_total_esperado = 5627898      
                   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)
                   
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)

    #SUMINISTROS DE COLOMBIA S.A.S - CALCINACIÓN ABR MAY JUN
    def test_comprobar_valor_calcinacion_abril_mayo_junio(self):
        #Establecer datos de entrada
        n_servicios: int = 3
        precio_unitario: float = 145125

        #Establecer datos de salida esperada
        valor_total_esperado = 518096      
                   
        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario)
                   
        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(round(valor_calculado),valor_total_esperado)


    # CASOS DE ERROR

    # ERROR 1 - CANTIDAD DE SERVICIOS IGUAL A CERO
    def test_error_cantidad_servicios_cero(self):

        # Establecer datos de entrada
        n_servicios: int = 0
        precio_unitario: float = 241875

        # Verificar que el programa detecte el dato invalido
        with self.assertRaises(facturacion_sensores.ServiciosInvalidos):
            facturacion_sensores.calcular_valor_factura(n_servicios, precio_unitario)


    # ERROR 2 - PRECIO UNITARIO IGUAL A CERO
    def test_error_precio_unitario_cero(self):

        # Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 0

        # Verificar que el programa detecte el dato invalido
        with self.assertRaises(facturacion_sensores.PrecioInvalido):
            facturacion_sensores.calcular_valor_factura(n_servicios, precio_unitario)


    # ERROR 3 - CANTIDAD DE SERVICIOS NEGATIVA
    def test_error_cantidad_servicios_negativa(self):

        # Establecer datos de entrada
        n_servicios: int = -1
        precio_unitario: float = 241875

        # Verificar que el programa detecte el dato invalido
        with self.assertRaises(facturacion_sensores.ServiciosInvalidos):
            facturacion_sensores.calcular_valor_factura(n_servicios, precio_unitario)


    # ERROR 4 - PRECIO UNITARIO NEGATIVO
    def test_error_precio_unitario_negativo(self):

        # Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = -241875

        # Verificar que el programa detecte el dato invalido
        with self.assertRaises(facturacion_sensores.PrecioInvalido):
            facturacion_sensores.calcular_valor_factura(n_servicios, precio_unitario)


    # CASOS DE PRUEBA EXTRAORDINARIOS

    # EXTRAORDINARIO 1 - GRAN CANTIDAD DE SERVICIOS
    def test_extraordinario_gran_cantidad_servicios(self):

        # Establecer datos de entrada
        n_servicios: int = 100
        precio_unitario: float = 1000

        # Establecer datos de salida esperada
        valor_total_esperado = 119000

        # Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(
            n_servicios, precio_unitario
        )

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado, valor_total_esperado)


    # EXTRAORDINARIO 2 - VALOR UNITARIO CON DECIMALES
    def test_extraordinario_valor_unitario_decimal(self):

        # Establecer datos de entrada
        n_servicios: int = 2
        precio_unitario: float = 1250.50

        # Establecer datos de salida esperada
        valor_total_esperado = 2976.19

        # Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(
            n_servicios, precio_unitario
        )

        # Verificar que el dato obtenido sea el esperado
        self.assertAlmostEqual(valor_calculado, valor_total_esperado, 2)


    # EXTRAORDINARIO 3 - VALOR UNITARIO MUY ALTO
    def test_extraordinario_valor_unitario_alto(self):

        # Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 10000000

        # Establecer datos de salida esperada
        valor_total_esperado = 11900000

        # Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura(
            n_servicios, precio_unitario
        )

        # Verificar que el dato obtenido sea el esperado
        self.assertEqual(valor_calculado, valor_total_esperado)


if __name__ == '__main__':
    unittest.main()

