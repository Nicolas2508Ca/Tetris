import pygame
from colors import Colors

class Grid:

    # Inicializa los atributos de la clase
    def __init__(self):

        # Numero de filas y columnas
        self.num_rows = 20
        self.num_cols = 10
        # Tamaño de la celda
        self.cell_size = 30
        # Crea una lista bidimensional representa la cuadrícula. Cada celda con el valor 0.
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        # Asigna colores a las celdas
        self.colors = Colors.get_cell_colors()

    # Imprime la cuadrícula en la consola
    def print_grid(self): 
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end=" ")
            print()

    def is_inside(self, row, column):
        if row >= 0  and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False 
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_down_rows(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_down_rows(row, completed)
        return completed
    
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    # Dibuja la cuadrícula en la pantalla
    def draw (self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +11, row*self.cell_size +11, self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

