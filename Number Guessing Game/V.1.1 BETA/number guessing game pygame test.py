import pygame
import random

# Initialize Pygame
pygame.init()

# -------------------------- SETUP WINDOW AND CONSTANTS --------------------------
# Set up the display window
screen = pygame.display.set_mode((720, 480), vsync=1)
pygame.display.set_caption("Number Guessing Game By Mitchel Onyebuchi")

# Define color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Blues
BLUE = (52, 152, 219)
LIGHT_BLUE = (174, 214, 241)
DARK_BLUE = (41, 128, 185)
# Greens
GREEN = (50, 205, 50)
LIGHT_GREEN = (144, 238, 144)
DARK_GREEN = (0, 128, 0)
# Reds
RED = (255, 0, 0)
LIGHT_RED = (255, 99, 71)
DARK_RED = (139, 0, 0)
# Greys
GREY = (200, 200, 200)
LIGHT_GREY = (230, 230, 230)

# Font for text (ensure you have the correct path for the font file)
font_path = "Fonts/Bungee-Regular.ttf"
font = pygame.font.Font(font_path, 36)

# -------------------------- GAME VARIABLES --------------------------
# Set up game logic variables
secret_number = random.randint(1, 10)  # Random secret number
attempts = 0  # Counter for number of attempts
difficulty = None  # Difficulty level
game_over = False  # Game state
# message = "Choose a difficulty"

# -------------------------- BUTTON CLASS --------------------------
# Create a class for interactive buttons
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, click_color):
        self.rect = pygame.Rect(x, y, width, height)  # Define button rectangle
        self.text = text  # Button text
        self.color = color  # Normal color
        self.hover_color = hover_color  # Hover color
        self.click_color = click_color  # Click color
        self.current_color = color  # Current color (depends on interaction)
        self.font = pygame.font.Font(font_path, 24)  # Font for the button text
    
    # Draw the button on the screen
    def draw(self, screen, mouse_pos, clicked):
        # Check if mouse is hovering or clicking
        if self.rect.collidepoint(mouse_pos):
            if clicked:
                self.current_color = self.click_color
            else:
                self.current_color = self.hover_color
        else:
            self.current_color = self.color
        
        # Draw the button rectangle
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=10)
        
        # Draw the button text
        text_surf = self.font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    # Check if the button is clicked
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

# -------------------------- HELPER FUNCTIONS --------------------------

# Draw input box for player guesses
def draw_input_box(screen, input_box, input_text, active):
    # Draw shadow and border for the input box
    pygame.draw.rect(screen, WHITE, input_box, border_radius=10)
    pygame.draw.rect(screen, BLUE if active else BLACK, input_box, 2, border_radius=10)
    
    # Display text inside the input box
    font = pygame.font.Font(font_path, 36)
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_box.x + 10, input_box.y + 8))

# Draw the background image for the game
def draw_background(screen):
    background_image = pygame.image.load("/Users/MAC/Documents/GitHub/Python-Beginner-Projects/IMAGES/IMAGE2.png")
    screen.blit(background_image, (0, 0))  # Place the background at (0, 0)

# Draw messages like instructions and game status on the screen
def draw_message(screen, message):
    font = pygame.font.Font(font_path, 24)
    text_surface = font.render(message, True, WHITE)
    screen_width, screen_height = screen.get_size()  # Get screen size
    text_width, text_height = text_surface.get_size()  # Get text size
    
    # Center the text on the screen
    position = ((screen_width - text_width) // 2, 260)
    screen.blit(text_surface, position)

# Draw the number of attempts remaining on the screen
def draw_attempts(screen, attempts):
    font = pygame.font.Font(font_path, 18)
    text_surface = font.render(f"Attempts: {attempts}", True, WHITE)
    screen.blit(text_surface, (580, 20))  # Display attempts at the top right corner

# -------------------------- MAIN GAME LOGIC --------------------------
# Initialize variables for game loop
running = True
active = False
input_text = ""
secret_number = random.randint(1, 10)  # Generate a new random number for every game
difficulty = None
attempts = 0
message = "Select a difficulty!"  # Default message before game starts

# -------------------------- BUTTONS SETUP --------------------------
# Create difficulty buttons (easy, medium, hard)
easy_button = Button(110, 355, 150, 50, "Easy", GREEN, LIGHT_GREEN, DARK_GREEN)
medium_button = Button(280, 355, 150, 50, "Medium", BLUE, LIGHT_BLUE, DARK_BLUE)
hard_button = Button(450, 355, 150, 50, "Hard", RED, LIGHT_RED, DARK_RED)
input_box = pygame.Rect(260, 355, 200, 50)  # Input box for player's guesses

# -------------------------- GAME LOOP --------------------------
while running:
    screen.fill(WHITE)  # Clear the screen with white
    draw_background(screen)  # Draw background image

    # Get mouse position and check for clicks
    mouse_pos = pygame.mouse.get_pos()
    clicked = False

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close game if 'QUIT' event
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
            # Handle difficulty selection buttons
            if difficulty is None:
                if easy_button.is_clicked(mouse_pos):
                    difficulty = 10
                    attempts = 10
                    message = "Guess a number between 1 and 10!"
                elif medium_button.is_clicked(mouse_pos):
                    difficulty = 5
                    attempts = 5
                    message = "Guess a number between 1 and 10!"
                elif hard_button.is_clicked(mouse_pos):
                    difficulty = 3
                    attempts = 3
                    message = "Guess a number between 1 and 10!"
            # Activate input box for entering guesses
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
        # Handle key inputs when the input box is active
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:
                # Check if entered guess is correct
                if input_text.isdigit():
                    guess = int(input_text)
                    if guess == secret_number:
                        message = f"Congratulations! The number was {secret_number}."
                    else:
                        attempts -= 1
                        message = "Too high!" if guess > secret_number else "Too low!"
                        if attempts == 0:
                            message = f"Game Over! The number was {secret_number}."
                input_text = ''  # Clear input text after guess
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]  # Handle backspace to delete text
            else:
                input_text += event.unicode  # Append new character to input text

    # -------------------------- GAME INTERFACE RENDERING --------------------------
    # Draw buttons when difficulty hasn't been selected
    if difficulty is None:
        easy_button.draw(screen, mouse_pos, clicked)
        medium_button.draw(screen, mouse_pos, clicked)
        hard_button.draw(screen, mouse_pos, clicked)
    else:
        draw_input_box(screen, input_box, input_text, active)  # Draw input box for guesses
    
    draw_message(screen, message)  # Show game message
    draw_attempts(screen, attempts)  # Show remaining attempts

    pygame.display.update()  # Refresh display with new elements

# Quit Pygame once the loop ends
pygame.quit()
