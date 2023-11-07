import pygame
import pygame_menu


def main():

    global selected_game 
    selected_game = "Minesweeper"

    def select_game(_, game):
        global selected_game
        selected_game = game

    def launch_selected_game():
        print(selected_game)
        menu.disable()
        return

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
            "game :",
            [("Minesweeper", "Minesweeper"), ("TicTacToe", "TicTacToe"), ("Snake", "Snake")],
            onchange=select_game,
        )
    menu.add.button("Play", launch_selected_game)
    menu.mainloop(screen)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Main program loop
    while True:
        # --- Limit to 60 frames per second
        clock.tick(60)
        screen.fill((37, 37, 37))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


if __name__ == "__main__":
    main()
