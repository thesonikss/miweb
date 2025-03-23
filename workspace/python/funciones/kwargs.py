# keywords arguments es una forma en que podemos empaquetar todos los parametros en solo 1 parametro
def get_product(**datos):
    print(datos["name"])


get_product(id="id",
            name="iPhone",
            nacionalidad="Chile")
