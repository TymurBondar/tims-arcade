import pygame
import pygame_menu
import subprocess
import sys


def main():

    global selected_game 
    selected_game = "Minesweeper"

    def select_game(_, game):
        global selected_game
        selected_game = game

    def launch_selected_game():
        subprocess.Popen([sys.executable, f"./lib/games/{selected_game.lower()}/{selected_game.lower()}.py"])
        menu.disable()

    # Initialize Pygame
    pygame.init()


    # Set the width and height of the screen (width, height).
    size = (800, 600)
    screen = pygame.display.set_mode(size)

    # Set the title of the window
    pygame.display.set_caption("Tims Arcade")

    # Loop until the user clicks the close button.

    menu = pygame_menu.Menu("Welcome to Tims Arcade", 800, 600, theme=pygame_menu.themes.THEME_DARK)

    menu.add.selector(
            "Game :",
            [("Minesweeper", "Minesweeper"), ("TicTacToe", "TicTacToe"), ("Snake", "Snake")],
            onchange=select_game,
        )
    menu.add.button("Play", launch_selected_game)
    menu.mainloop(screen)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    white = (255, 255, 255)
    bg_grey = (37, 37, 37)

    font = pygame.font.SysFont("Arial", 32)
    from helpers import Button
    back_button_img = pygame.image.load('back_button.png').convert_alpha()
    back_button = Button(150, 150, back_button_img, 0.5)

    # Main program loop
    while True:
        # --- Limit to 60 frames per second
        clock.tick(60)
        screen.fill(bg_grey)
        text = font.render(f"Welcome to {selected_game}", True, white)
        textRect = text.get_rect()
        screen.blit(text, textRect)

        # return to the main menu after you click the back button
        if back_button.draw(screen):
            menu.enable()
            menu.mainloop(screen)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


if __name__ == "__main__":
    main()
