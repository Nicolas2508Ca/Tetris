from .colors import Colors
import pygame
from .position import Position

class  Block:
    def __init__ (self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30

        # Define la posicion inicial del bloque
        self.row_offset = 0
        self.column_offset = 0

        # Define el estado de rotacion del bloque ( por defecto todos los bloques empiezan en la rotacion 0)
        self.rotation_state = 0

        self.colors = Colors.get_cell_colors()

    # Metodo para mover el bloque en el tablero
    def move(self, rows, columns):
        # Se actualiza la posicion del bloque en el tablero, sumando las filas y columnas que se pasan como parametros con la posicion de origen.
        # El operado += es equivalente a self.row_offset = self.row_offset + rows
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        # Obtiene las posiciones de las celdas del bloque en la rotacion actual
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        # Se recorre la lista de posiciones de las celdas y se crea una nueva lista con las posiciones actualizadas
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    # Metodo para rotar el bloque
    def rotate(self):
        # Incremneta el valor del estado de rotacion en 1
        self.rotation_state += 1
        # Si el esatdo de rotacion llega a 4 (longitud de la lista de rotaciones) se reinicia a 0 para volver a la rotacion inicial
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # Metodo para deshacer la rotacion, cuando el bloque no cabe en la cuadricula
    def undo_rotation(self):
        # Decrementa el valor del estado de rotacion en 1
        self.rotation_state -= 1
        # Si al restar 1 al estado de rotacion llega a 0, se reinicia a la ultima rotacion
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) -1

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column*self.cell_size, offset_y + tile.row*self.cell_size , self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)