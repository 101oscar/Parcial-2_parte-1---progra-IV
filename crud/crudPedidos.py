from .crudCliente import verifica_cliente, read_cliente, update_pedido_cliente, delete_pedido_cliente
from model.pedido import Pedido

productos = []
lista_pedidos = []

def agregar_productos(producto):
	productos.append(producto)

def create_pedido(productos):
	nuevo_pedido = Pedido(productos)
	lista_pedidos.append(nuevo_pedido)

def read_pedido(fecha):
	for pedido in lista_pedidos:
		if pedido.fecha == fecha:
			return pedido
	raise Exception("No existe un pedido con la fecha indicada.")

def update_p(fecha, productos):
	try:
		pedido = read_pedido(fecha)
		pedido.productos = productos
		return pedido
	except Exception as e:
		raise e

def delete_p(fecha):
	try:
		pedido = read_pedido(fecha)
		lista_pedidos.remove(pedido)
		return pedido
	except Exception as e:
		raise e

def pedido_cliente(cliente, pedido):
	try:
		verifica_cliente(cliente.cedula)
		cliente.agregar_pedido(pedido)
	except Exception as e:
		raise e	
	
def registro_pedido(cedula, fecha):
	try:
		cliente = read_cliente(cedula)
		pedido = read_pedido(fecha)
		pedido_cliente(cliente, pedido)
	except Exception as e:
		raise e

def update_pedido(cliente, fecha, productos):
	try:	
		update_p(fecha, productos)
		update_pedido_cliente(cliente, fecha, productos)
	except Exception as e:
		raise e

def delete_pedido(cliente, fecha):
	try:
		delete_p(fecha)
		delete_pedido_cliente(cliente, fecha)
	except Exception as e:
		raise e