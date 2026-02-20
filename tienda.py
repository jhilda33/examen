class producto:
    #constructor
    def _init_(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    #metodo
    def mostrar_info(self):
        print(f'nombre: {self.nombre}')
        print(f'precio: {self.precio}')
        print(f'cantidad: {self.cantidad}')
        print(f'valor total: ${self.valor_total}')

    #metodo
    def valor_total(self):
        return self.precio * self.cantidad

#crear lista
productos = []

#agregar productos
def agregar_producto():
    nombre = input("ingrese nombre del producto: ")
    precio = float(input("ingrese precio: "))
    cantidad = int(input("ingrese cantidad: "))


    nuevo_producto = Producto(nombre, precio, cantidad)
    productos.append(nuevo_producto)

    print("producto agregado correctamente.\n")
#mostrar producto
def mostrar_productos():
    if len(productos) == 0:
        print("no hay productos resgistrados: \n")
    else:
        print("\n lista de productos: ")
        for producto in productos:
            producto. mostrar_info()

#menu
while True:
    print ("menu")
    print ("1.agregar producto")
    print ("2.mostrar productos")
    print ("salir")

    opcion = input("seleccione una opcion")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        print("saliendo del programa: ")
        break
    else:
        print("opcion invalida")

