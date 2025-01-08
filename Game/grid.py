import pygame
from .colors import Colors

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

    # Comprueba si la fila y columna están dentro de la cuadrícula
    def is_inside(self, row, column):
        # Si la fila y columna están dentro de la cuadrícula, devuelve True. En caso contrario, devuelve False.
        if row >= 0  and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False 
    
    # Comprueba si la fila y columna están vacías
    def is_empty(self, row, column):
        # Si la celda está vacía, devuelve True. En caso contrario, devuelve False.
        if self.grid[row][column] == 0:
            return True
        return False
    
    # Comprueba si la fila están ocupadas
    def is_row_full(self, row):
        # Si la fila está llena, devuelve True. En caso contrario, devuelve False.
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    # Cambia el valor de la celda en la fila y columna especificadas de nuevo a 0 (celda vacía)
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0
    
    # Mueve las columnas hacia abajo cuando una columna de mas abajo es completada
    def move_down_rows(self, row, num_rows):
        for column in range(self.num_cols):
            # Ya que el orden de las filas es de arriba a abajo, a la fila que se quiere mover se le suma el numero de filas completas (elimindas) y en la nueva fila se copia el valor de la fila anterior
            self.grid[row + num_rows][column] = self.grid[row][column]
            # Vacia la fila original, ya que debe dar la sensacion de que las filas caen
            self.grid[row][column] = 0

    # Encargada de juntar las otras funciones para limpiar las filas completas
    def clear_full_rows(self):
        completed = 0
        # Recorre las filas de abajo hacia arriba (de la 19 (ultima fila) a la 0 (primera fila)) decrementando en 1
        for row in range(self.num_rows-1, 0, -1):
            # Si la fila esta completa, la limpia y aumenta el contador de filas completas
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            # Una vez no hay mas filas completas que eliminar, se mueven hacia abajo las filas que se encontraban sobre las filas completas
            elif completed > 0:
                self.move_down_rows(row, completed)
        return completed
    
    # Reinicia la cuadrícula (todas las celdas con el valor 0)
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    # Dibuja la cuadrícula en la pantalla
    def draw (self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                # Guarda el valor de la celda en una variable
                cell_value = self.grid[row][column]
                # Crea un rectángulo para cada celda y lo dibuja en la pantalla. Las coordenadas x e y se calculan multiplicando la fila y la columna por el tamaño de la celda. El ancho y el alto de la celda son el tamaño de la celda menos 1 para que haya un espacio entre las celdas.
                cell_rect = pygame.Rect(column*self.cell_size +11, row*self.cell_size +11, self.cell_size -1, self.cell_size -1)
                # Dibuja el rectángulo en la pantalla con el color correspondiente al valor de la celda. Los parametros son la superficie, el color y el rectangulo.
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

