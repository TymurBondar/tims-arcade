import pygame
import pygame_menu


def main():

    global selected_game 
    selected_game = "Minesweeper"

    def select_game(_, game):
        global selected_game
        selected_game = game

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
    menu.add.button("Play", menu.disable)
    menu.mainloop(screen)

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    white = (255, 255, 255)
    bg_grey = (37, 37, 37)
    font = pygame.font.SysFont("Arial", 32)
    text = font.render(f"Welcome to {selected_game}", True, white)
    textRect = text.get_rect()
    # Main program loop
    while True:
        # --- Limit to 60 frames per second
        clock.tick(60)
        screen.fill(bg_grey)
        screen.blit(text, textRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


if __name__ == "__main__":
    main()
