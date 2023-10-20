class Antibiotico:
    tipos_animales_validos = ["Bovino", "Caprino", "Porcino"]

    def __init__(self, nombre, dosis, tipo_animal, valor):
        if not nombre or not dosis or not tipo_animal or not valor:
            raise ValueError("El nombre no puede estar vacío")
        if dosis<400 or dosis>600:
            raise ValueError("La dosis debe estar entre 400 y 600.")
        if tipo_animal not in self.tipos_animales_validos:
            raise ValueError("El tipo de animal no es válido.")
        if valor < 0:
            raise ValueError("El valor no puede ser negativo.")
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.valor = valor
