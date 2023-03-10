from Productos import Productos

class App():
    def __init__(self):
        self.products_viejo = [{'id': 1, 'name': "Nevera", type: 'Hogar', "stock": 753, "price": 800 },
{ "id": 2, "name": "Cama", type: "Hogar", "stock": 327, "price": 600 },
{ "id": 3, "name": "Suéter", type: "Ropa", "stock": 260, "price": 25 },
{ "id": 4, "name": "Zapatos", type: "Ropa", "stock": 593, "price": 5 },
{ "id": 5, "name": "Laptop Gamer", type: "Gaming", "stock": 11, "price": 2500 },
{ "id": 6, "name": "Nintendo Switch OLED", type: "Gaming", "stock": 25, "price": 400 },]
        self.products={ "name": [], type: [] }
    def cargar(self):
        for type, lista in self.products_viejo.items():
            for producto in lista:
                if type == "Hogar":
                    b=Productos(producto["id"], producto["nombre"], producto["stock"], producto["price"])
                elif type == 'Ropa':
                    b=Productos(producto["id"], producto["nombre"], producto["stock"], producto["price"])
                else:
                    b=Productos(producto["id"], producto["nombre"], producto["stock"], producto["price"])

                self.products["Hogar" if isinstance(b, Productos) else "Ropa"].append(b)

    def ver_inventario(self):
        print("INVENTARIO ----")
        for type, producto in self.products():
            print(f"\n{type.upper()} >>>\n")
            for producto in Productos:
                producto.mostrar()            
                
              


       


    




























