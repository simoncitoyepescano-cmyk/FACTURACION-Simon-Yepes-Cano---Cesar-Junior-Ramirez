def calcular_valor_factura(n_servicios:int,precio_unitario:float,iva: float):
  iva = 0.19 * (n_servicios * precio_unitario)
  valor_servicios = (n_servicios * precio_unitario) + iva
  return valor_servicios
