from dataclasses import dataclass, field

# ? Clase normal
class PointWithoutDataclass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"PointWithoutDataclass(x={self.x}, y={self.y})"
    
    def __eq__(self, other):
        if isinstance(other, PointWithoutDataclass):
            return self.x == other.x and self.y == other.y
        return False

# Crear instancias de la clase PointWithoutDataclass
p1 = PointWithoutDataclass(1, 2)
p2 = PointWithoutDataclass(3, 4)

print(p1)  # Salida: PointWithoutDataclass(x=1, y=2)
print(p2)  # Salida: PointWithoutDataclass(x=3, y=4)
print(p1 == p2)  # Salida: False



# ? Ejemplo 01
#*  La versión con dataclasses es mucho más concisa y no requiere escribir métodos como __init__, __repr__ y __eq__, ya que estos son generados automáticamente.
@dataclass
class PointWithDataclass:
    x: int
    y: int

# Crear instancias de la clase PointWithDataclass
p1 = PointWithDataclass(1, 2)
p2 = PointWithDataclass(3, 4)

print(p1)  # Salida: PointWithDataclass(x=1, y=2)
print(p2)  # Salida: PointWithDataclass(x=3, y=4)
print(p1 == p2)  # Salida: False



# ? Ejemplo 02
@dataclass
class Book:
    title: str
    author: str
    year: int = field(default=2020)

# Crear instancias de la clase Book
book1 = Book("Python Programming", "Alice Smith")
book2 = Book("Data Science Basics", "Bob Johnson", 2022)

# Salida: Book(title='Python Programming', author='Alice Smith', year=2020)
print(book1)
# Salida: Book(title='Data Science Basics', author='Bob Johnson', year=2022)
print(book2)


# ? Ejemplo 03
@dataclass(order=True)
class Student:
    name: str
    age: int
    grade: str

# Crear instancias de la clase Student
student1 = Student("Alice", 18, "A")
student2 = Student("Bob", 17, "B")

print(student1 < student2)  # Salida: False (orden alfabético por nombre)
