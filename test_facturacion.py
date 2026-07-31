import unittest
import facturacion_sensores

class TestsFacturacion(unittest.TestCase):
  #GAMMA
  def comprobar_valor_gamma(self): 
  #Establecer datos de entrada
    n_servicios: int = 1
    precio_unitario: float = 1741500
    iva: float = 330885

    #Establecer datos de salida esperada
    valor_total_esperado = 2072385

    #Probar la funcion que resuelve problemas
    valor_calculado = facturacion_sensores.calcular_valor_factura(n_servicios,precio_unitario,iva)

    # Verificar que el dato obtenido sea el esperado
    if valor_calculado == valor_total_esperado:
        print("La factura de GAMMA esta bien")
    else:
        print("Hay un error en la factura")
    
    #CORLANC
    def comprobar_valor_corlanc(self): 
    #Establecer datos de entrada
        n_servicios: int = 2
        precio_unitario: float = 241875
        iva: float = 91913

        #Establecer datos de salida esperada
        valor_total_esperado = 575662.5
        valor_total = round(valor_total_esperado)

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura_corlanc(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        if round(valor_calculado) == valor_total:
            print("La factura de CORLANC esta bien")
        else:
            print("Hay un error en la factura")

    #LOCERIA
    def comprobar_valor_loceria(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 3483000
        iva: float = 661770

        #Establecer datos de salida esperada
        valor_total_esperado = 4144770
        valor_total = round(valor_total_esperado)

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura_corlanc(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        if round(valor_calculado) == valor_total:
            print("La factura de LOCERIA esta bien")
        else:
            print("Hay un error en la factura")

    #ENKA
    def comprobar_valor_enka(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 1680000
        iva: float = 319200

        #Establecer datos de salida esperada
        valor_total_esperado = 1999200
        valor_total = round(valor_total_esperado)

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura_corlanc(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        if round(valor_calculado) == valor_total:
            print("La factura de ENKA esta bien")
        else:
            print("Hay un error en la factura")

    #CRYOGAS GATEWAYS
    def comprobar_valor_cryogas_gateways(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 6820000
        iva: float = 1295800

        #Establecer datos de salida esperada
        valor_total_esperado = 8115800  
        valor_total = round(valor_total_esperado)

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura_corlanc(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        if round(valor_calculado) == valor_total:
            print("La factura de CRYOGAS gateway esta bien")
        else:
            print("Hay un error en la factura")

    #CRYOGAS SENSOR
    def comprobar_valor_cryogas_sensor(self):
        #Establecer datos de entrada
        n_servicios: int = 1
        precio_unitario: float = 1500000
        iva: float = 285000

        #Establecer datos de salida esperada
        valor_total_esperado = 1785000
        valor_total = round(valor_total_esperado)

        #Probar la funcion que resuelve problemas
        valor_calculado = facturacion_sensores.calcular_valor_factura_corlanc(n_servicios,precio_unitario,iva)

        # Verificar que el dato obtenido sea el esperado
        if round(valor_calculado) == valor_total:
            print("La factura de CRYOGAS sensor esta bien")
        else:
            print("Hay un error en la factura")

if __name__ == '__main__':
    unittest.main()