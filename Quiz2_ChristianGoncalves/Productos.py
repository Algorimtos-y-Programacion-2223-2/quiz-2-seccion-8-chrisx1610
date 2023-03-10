class Productos():
    def __init__(self,id,name,type,stock,price) -> None:
        self.id=id
        self.name=name
        self.type=type
        self.stock=stock
        self.price=price
    def mostrar (self):
        print('id {self.id}\nname {self.name}\ntype {self.type}\nstock {self.stock}\nprice {self.price}')