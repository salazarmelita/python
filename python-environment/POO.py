
#? Clase para representar una Persona
class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Crear objetos de la clase Persona
persona1 = Persona("Juan", 30, "Ingeniero")
persona2 = Persona("María", 25, "Doctora")

print(persona1.saludar())
print(persona2.saludar())


#? Clase para representar una Cuenta Bancaria
class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

# Crear objetos de la clase CuentaBancaria
cuenta1 = CuentaBancaria(1000)
cuenta2 = CuentaBancaria(500)

cuenta1.depositar(200)
cuenta2.retirar(100)

print(f"Saldo de cuenta1: ${cuenta1.saldo}")
print(f"Saldo de cuenta2: ${cuenta2.saldo}")


#? Clase para representar Figuras Geométricas
class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def area(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

# Crear objetos de diferentes figuras
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

print(f"Área del círculo: {circulo.area()}")
print(f"Área del rectángulo: {rectangulo.area()}")

#* Ejemplo de encapsulación
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("No es posible retirar esa cantidad.")

    def obtener_saldo(self):
        return self.__saldo

# Crear un objeto de la clase CuentaBancaria
cuenta = CuentaBancaria(1000)

# Intentar acceder al atributo privado (esto no es recomendable)
# print(cuenta.__saldo)  # Esto generaría un error

# Utilizar los métodos públicos para interactuar con la cuenta
cuenta.depositar(500)
cuenta.retirar(200)
print(f"Saldo actual: {cuenta.obtener_saldo()}")

#* Ejemplo Polimorfismo
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Woof!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

animales = [Perro(), Gato()]
for animal in animales:
    print(animal.hablar())

#* Ejemplo de Herencia
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"Este es un {self.marca} {self.modelo}."

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def describir(self):
        return f"Este es un {self.marca} {self.modelo} con {self.puertas} puertas."

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def describir(self):
        return f"Esta es una motocicleta {self.marca} {self.modelo} con una cilindrada de {self.cilindrada} cc."

# Crear objetos de diferentes tipos de vehículos
auto = Automovil("Toyota", "Camry", 4)
moto = Motocicleta("Honda", "CBR600RR", 600)

# Utilizar métodos de las clases
print(auto.describir())
print(moto.describir())