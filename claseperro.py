print("Clases version 2 el constructor")
class Perro:
    # funciom constructor
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad
    # las funciones creadas por el usuario 
    def muerde(self):
        print("nmms mi pataaaaaaa!!!")
    def Chatperro(self, mensaje):
        print(f"Chat perro: {mensaje}")
    def Chatperra(self, mensajepe):
        print(f"Chat perra: {mensajepe}")
    def datos(self):
        print(f"Color: {self.color} Edad: {self.edad}")
#crea el objeto 
chihuas=Perro("cafe", 3) 
# llamar a la funcion 
chihuas.datos()
chihuas.muerde()
chihuas.Chatperro("Hola Robertota")
chihuas.Chatperra("Hola mi Men hermoso")
chihuas.Chatperro("quieres tener setzo?")
chihuas.Chatperra("gogogo.......")