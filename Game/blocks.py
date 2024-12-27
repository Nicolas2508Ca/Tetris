from .block import Block
from .position import Position

# Todos los bloques heredan de la clase Block, es decir que hereadn sus métodos y atributos

class LBlock(Block):
    def __init__(self):
        # Se llama al constructor de la clase padre (block) y se le pasa el id del bloque
        super().__init__(id = 1)
        # Se definen las posiciones de las celdas del bloque en cada una de sus rotaciones
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
        }
        # Llama al metodo move de la clase Block para mover el bloque a la posición inicial, cambiando la posicion incial por defecto 0, 0
        self.move(0, 3)

class JBlock(Block):
    def __init__(self):
        # Se llama al constructor de la clase padre (block) y se le pasa el id del bloque
        super().__init__(id = 2)
        # Se definen las posiciones de las celdas del bloque en cada una de sus rotaciones
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        # Llama al metodo move de la clase Block para mover el bloque a la posición inicial, cambiando la posicion incial por defecto 0, 0
        self.move(0, 3)

class IBlock(Block):
    def __init__(self):
        # Se llama al constructor de la clase padre (block) y se le pasa el id del bloque
        super().__init__(id = 3)
        # Se definen las posiciones de las celdas del bloque en cada una de sus rotaciones
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        # Llama al metodo move de la clase Block para mover el bloque a la posición inicial, cambiando la posicion incial por defecto 0, 0
        self.move(-1, 3)

class OBlock(Block):
    def __init__(self):
        # Se llama al constructor de la clase padre (block) y se le pasa el id del bloque
        super().__init__(id = 4)
        # Se definen las posiciones de las celdas del bloque en cada una de sus rotaciones
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        # Llama al metodo move de la clase Block para mover el bloque a la posición inicial, cambiando la posicion incial por defecto 0, 0
        self.move(0, 4)

class SBlock(Block):
    def __init__(self):
        # Se llama al constructor de la clase padre (block) y se le pasa el id del bloque
        super().__init__(id = 5)
        # Se definen las posiciones de las celdas del bloque en cada una de sus rotaciones
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        # Llama al metodo move de la clase Block para mover el bloque a la posición inicial, cambiando la posicion incial por defecto 0, 0
        self.move(0, 3)

class TBlock(Block):
    def __init__(self):
        # Se llama al constructor de la clase padre (block) y se le pasa el id del bloque
        super().__init__(id = 6)
        # Se definen las posiciones de las celdas del bloque en cada una de sus rotaciones
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        # Llama al metodo move de la clase Block para mover el bloque a la posición inicial, cambiando la posicion incial por defecto 0, 0
        self.move(0, 3)

class ZBlock(Block):
    def __init__(self):
        # Se llama al constructor de la clase padre (block) y se le pasa el id del bloque
        super().__init__(id = 7)
        # Se definen las posiciones de las celdas del bloque en cada una de sus rotaciones
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        # Llama al metodo move de la clase Block para mover el bloque a la posición inicial, cambiando la posicion incial por defecto 0, 0
        self.move(0, 3)
