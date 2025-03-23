
nombres = ["daniel", "claudio", "victor", "pablo", "felipe", "roberto"]
apellidos = ["daroch", "espinoza", "collio", "fuentes", "chamorro", "vasquez"]
trabajadores = {nombre: apellido for (
    nombre, apellido) in zip(nombres, apellidos)}
print(trabajadores)
trabajadores_v2 = {nombre: apellido for
                   nombre, apellido in trabajadores.items() if "a" in nombre}
print(trabajadores_v2)
