class Informacion:
    def mi_lista(self):
        lista_nomperro=["David", "melgar", "angelito"]
        for x in lista_nomperro:
            print(x)

    def mi_tupla(self):
        tupla_color=("Cafe", "Negro", "Negro y Blanco")
        for x in tupla_color:
            print(x)

    def mi_conjunto(self):
        conjunto_edadperro={3,8,5}
        for x in conjunto_edadperro:
            print(x)

    def mi_diccionario(self):
        diccionario_emoji = {"David": "esteril","melgar": "8","angelito": "6"
}
        for x, k in diccionario_emoji.items():
            print(x,":",k)
# creando el objeto 
datos=Informacion()
print("listado de nombres de los perros de mi chan")
datos.mi_lista()
print("listado de colores de los perros de mi chan")
datos.mi_tupla()
print("listado de edades de los perros de mi chan")
datos.mi_conjunto()
print("listado de las crias de los perros de mi chan")
datos.mi_diccionario()

