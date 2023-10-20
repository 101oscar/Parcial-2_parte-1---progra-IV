class ProductoControl:
    def __init__(self, ica, nombre, frecuencia_aplicacion, valor):
        if not ica or not nombre or not frecuencia_aplicacion or not valor:
            raise ValueError("Todos los campos son obligatorios.")
        if not ica.isdigit():
            raise ValueError("debe ser un valor numérico")
        if valor < 0:
            raise ValueError("El valor no puede ser negativo.")
        self.ica = ica
        self.nombre = nombre
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.valor = valor
