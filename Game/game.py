from .grid import Grid
from .blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        # Se crea una lista con las instancias de la clase de cada bloque
        self.block = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        # Se retorna un bloque aleatorio de la lista
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")
    
        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)

    # Se encarga de actualizar la puntuacion del jugador, recibe como parametros las lineas completadas y los puntos por mover la pieza hacia abajo que siempre es 1
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points
        
    
    def get_random_block(self):
        # Si la lista de bloques esta vacia se vuelve a llenar
        if len(self.block) == 0:
            self.block = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        # random.choice elige un bloque aleatorio de la lista
        block = random.choice(self.block)
        # Se elimina el bloque de la lista para que no se repita
        self.block.remove(block)
        return block
    
    def move_left(self):
        # self.current_block guarda la instancia del bloque, que es una herencia de la clase Block, por lo que se puede utilizar el metodo move. Como parametros se pasan las filas y columnas que se quieren mover
        self.current_block.move(0, -1)
        # Se comprueba si el bloque esta dentro de la cuadricula o si alguna de las celda de la figura ya esta ocupada
        if self.block_inside() == False or self.block_fits() == False:
            # Si no se cumple la condicion (cualquiera de las funciones devuelven false) se deshace el movimiento. Ya que esta funcion es para mover la pieza a la izquierda, de colisionar con algo al hacer el movimiento lo contrario es mover la pieza a la derecha, para simular que no se movio
            self.current_block.move(0, 1)
    
    def move_right(self):
        # self.current_block guarda la instancia del bloque, que es una herencia de la clase Block, por lo que se puede utilizar el metodo move. Como parametros se pasan las filas y columnas que se quieren mover
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            # Si no se cumple la condicion (cualquiera de las funciones devuelven false) se deshace el movimiento. Ya que esta funcion es para mover la pieza a la derecha, de colisionar con algo al hacer el movimiento lo contrario es mover la pieza a la izquierda, para simular que no se movio
            self.current_block.move(0, -1) 
    
    def move_down(self):
        # self.current_block guarda la instancia del bloque, que es una herencia de la clase Block, por lo que se puede utilizar el metodo move. Como parametros se pasan las filas y columnas que se quieren mover
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            # Si no se cumple la condicion (cualquiera de las funciones devuelven false) se deshace el movimiento. Ya que esta funcion es para mover la pieza hacia abajo, de colisionar con algo al hacer el movimiento lo contrario es mover la pieza hacia arriba, para simular que no se movio
            self.current_block.move(-1, 0)
            self.lock_block()
    
    # Se encarga de bloquear el bloque en la cuadricula
    def lock_block(self):
        # Se obtienen las posiciones de las celdas del bloque
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            # Guarda la posicion en la que se enceuntra el bloque en la cuadricula, asigando en esa celdas el id del bloque
            self.grid.grid[position.row][position.column] = self.current_block.id
        # Una vez el bloque esta bloqueado, se cambia el bloque actual por el siguiente
        self.current_block = self.next_block
        # Y el bloque siguiente obtine una nueva figura aleatoria
        self.next_block = self.get_random_block()
        # Se utiliza la funcion clear_full_rows que lleva el conteo de las filas completadas
        rows_cleared = self.grid.clear_full_rows()
        # Si se completaron filas, se actualiza la puntuacion
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        # Se comprueba si el bloque siguiente cabe en la cuadricula, si no se cumple la condicion se termina el juego
        if self.block_fits() == False:
            self.game_over = True

    # Se encarga de reiniciar el juego
    def reset(self):
        # la funcion grid.reset se encarga de poner todas las celdas en 0 (vacio)
        self.grid.reset()
        # Se vuelve a llenar la lista de bloques
        self.block = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        # Se obtiene de manera aleatoria un bloque para el bloque actual y el siguiente
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        # Se inicializa el la puntuacion en 0
        self.score = 0

    def block_fits(self):
        # Se obtienen las posiciones de las celdas del bloque
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            # Se comprueba si la fila y columna de la celda esta vacia
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
    
    def rotate(self):
        # Se obtiene el id de rotacion del bloque
        self.current_block.rotate()
        # Se comprueba si el bloque al rotar esta dentro de la cuadricula o si alguna de las celdas de la figura ya esta ocupada
        if self.block_inside() == False or self.block_fits() == False:
            # Si no se cumple la condicion (cualquiera de las funciones devuelven false) se deshace la rotacion
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def block_inside(self):
        # Se obtienen las posiciones de las celdas del bloque
        tiles = self.current_block.get_cell_positions()
        # Se recorre la lista de posiciones de las celdas
        for tile in tiles:
            # Se comprueba si la fila y columna de la celda estan dentro de la cuadricula
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)