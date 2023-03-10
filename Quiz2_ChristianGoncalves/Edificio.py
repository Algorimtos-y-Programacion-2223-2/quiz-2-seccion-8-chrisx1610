class Edificio:
    def __init__(self,nombre,pisos,calle,ciudad,codigo,apartamentos) -> None:
        self.nombre=nombre
        self.pisos=pisos
        self.calle=calle
        self.ciudad=ciudad
        self.codigo=codigo
        self.apartamentos=apartamentos
    def mostrar_direccion (self):
        print('nombre {self.nombre}\npisos {self.pisos}\ncalle {self.calle}\nciudad {self.ciudad}\ncodigo {self.codigo}\napartamentos{self.partamentos}')

    def __init__(self):
        self.edificio=[]
        self.apartamentos=[]
    def constructor(self):
        nombre=input('Ingrese el nombre->')
        pisos=input('Ingrese la cantidad de pisos->')
        calle=input('Ingrese la calle->')
        ciudad=input('Ingrese la ciudad->')
        codigo=input('Ingrese el codigo postal->')
        apartamentos=input('Ingrese lista de apartamentos->')
        edificio=Edificio(nombre,pisos,calle,ciudad,codigo,apartamentos)
        self.edificio.append(edificio)

    def monstrar_direccion(self):
        print(Edificio.mostrar_direccion())

    def clasificacion_edificio(self,pisos,apartamentos):
        if apartamentos>(pisos*6):
            return 'Bloque de pisos'
        else:
            return 'Edificio Residencial'
        
    def monstrar_apartamentos(self):
        for apartamento in self.apartamentos:
            print(apartamento)
