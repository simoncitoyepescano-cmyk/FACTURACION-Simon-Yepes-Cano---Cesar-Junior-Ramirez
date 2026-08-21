class ServiciosInvalidos(Exception):
  pass
class PrecioInvalido(Exception):
  pass

def calcular_valor_factura(numero_servicios:int,precio_unitario:float)->float:
  """Devuelve un float que contiene el valor de servicios que debera pagar cada Cliente
  según su "numero de servicios" y el "precio unitario" de cada sensor multiplicandolo por
  un valor fijo del iva que seria el 19%.
  "numero_servicios": Es un entero que contiene el número de servicios que estan siendo
  utilizados actualmente por la empresa.
  "precio_unitario": Es un flotante que contiene el precio unitario de cada sensor
  que podria variar según el cliente."""

  iva = 0.19 * (numero_servicios * precio_unitario)
  valor_servicios = (numero_servicios * precio_unitario) + iva

  if numero_servicios <= 0:
    raise ServiciosInvalidos("La cantidad de servicios debe ser mayor que 0")
  if precio_unitario <= 0:
    raise PrecioInvalido("El precio unitario no puede ser negativos o 0")

  return valor_servicios
