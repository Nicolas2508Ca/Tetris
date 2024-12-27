import pygame, sys
from Game.game import Game
from Game.colors import Colors

# Inicializa todos los módulos de Pygame
pygame.init()

# Configura la fuente para los textos del juego
title_font = pygame.font.Font(None, 40)
#Se utiliza el metodo render del objeto title font para crear una superficie con el texto que se le pasa como parametro, tambien se pasa un booleano para antialiasing y el color del texto
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# Define los rectángulos para las áreas de puntuación y la siguiente pieza
# Los parametros son (posicion x, posicion y, ancho, alto)
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Creación de la ventana de juego de 500 píxeles de ancho y 620 píxeles de alto
screen = pygame.display.set_mode((500, 620))

# Título de la ventana
pygame.display.set_caption("Python Tetris")

# Reloj para controlar los fps
clock = pygame.time.Clock()

# Crea una instancia del juego
game = Game()

# Define un evento personalizado para actualizar el juego
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Game loop
while True:
    # Obtiene todos los eventos que se han producido
    for event in pygame.event.get():
        # Si el evento es de tipo QUIT (cerrar ventana), se cierra el juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Manejo de eventos de teclado
        if event.type == pygame.KEYDOWN:
            # Reinicia el juego si está en estado de game over
            if game.game_over == True:
                game.game_over = False
                game.reset()
            # Mueve la pieza a la izquierda si no está en game over
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            # Mueve la pieza a la derecha si no está en game over
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            # Mueve la pieza hacia abajo si no está en game over y actualiza la puntuación
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            # Rota la pieza si no está en game over
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        # Actualiza el juego en intervalos regulares si no está en game over
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
    
    # Crea una superficie con la puntuación actual del juego
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    # color de fondo de la pantalla
    screen.fill(Colors.dark_blue)

    # Dibula los titulos de la puntuacion y la siguiente pieza. Los 2 primeros del segundo parametro son las coordenadas x y y, el tercero y cuarto son el ancho y alto de la superficie
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (365, 180, 50, 50))

    # Dibuja la puntuación actual del juego. Calculando la posicion de la superficie de la puntuacion para que en todo momento este centrado el texto de la puntuacion
    

    # Muestra el mensaje de game over si el juego ha terminado
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
        
    # Dibuja los rectángulos de puntuación y la siguiente pieza. Como parametro se pasa la superficie, el color, el rectangulo, el ancho de la linea y el radio de las esquinas
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    # Dibuja la cuadrícula del juego, las fichas, etc
    game.draw(screen)

    # Actualiza la pantalla y muestra todo lo dibujado
    pygame.display.update()

    # Limita el juego a 60 fps
    clock.tick(60)