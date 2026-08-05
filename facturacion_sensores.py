class ServiciosInvalidos(Exception):
  pass
class PrecioInvalido(Exception):
  pass
class IvaInvalido(Exception):
  pass

def calcular_valor_factura(n_servicios:int,precio_unitario:float,iva: float):
  iva = 0.19 * (n_servicios * precio_unitario)
  valor_servicios = (n_servicios * precio_unitario) + iva

  if n_servicios < 0:
    raise ServiciosInvalidos("La cantidad de servicios no pueden ser negativos")
  if precio_unitario <= 0:
    raise PrecioInvalido("El precio unitario no puede ser negativos o 0")
  if iva <= 0:
    raise IvaInvalido("El iva no puede ser negativos o 0")

  return valor_servicios
