import pygame
import random

# Initialize Pygame
pygame.init()

# Set up window
screen = pygame.display.set_mode((720, 480), vsync=1)
pygame.display.set_caption("Number Guessing Game By Mitchel Onyebuchi")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#BLUES
BLUE = (52, 152, 219)  # A nice blue color
LIGHT_BLUE = (174, 214, 241)  # Lighter blue for hover effect
DARK_BLUE = (41, 128, 185)  # Darker blue for click effect
#GREENS
GREEN = (50, 205, 50)
LIGHT_GREEN = (144, 238, 144)
DARK_GREEN = (0, 128, 0)
#REDS
RED = (255, 0, 0)
LIGHT_RED = (255, 99, 71)
DARK_RED = (139, 0, 0)

GREY = (200, 200, 200)
LIGHT_GREY = (230, 230, 230)

# Font for text
font = pygame.font.Font(None, 48)

# Game variables
secret_number = random.randint(1, 10)
attempts = 0
difficulty = None
game_over = False
message = "Choose a difficulty"

# Button class to create interactive buttons
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, click_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.click_color = click_color
        self.current_color = color
        self.font = pygame.font.SysFont("Arial", 24)
    
    def draw(self, screen, mouse_pos, clicked):
        # Check for hover
        if self.rect.collidepoint(mouse_pos):
            if clicked:
                self.current_color = self.click_color
            else:
                self.current_color = self.hover_color
        else:
            self.current_color = self.color
        
        # Draw the button
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=10)
        
        # Draw the text
        text_surf = self.font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
def draw_input_box(screen, input_box, input_text, active):
    # Input box appearance (shadow + border)
    pygame.draw.rect(screen, GREY, input_box.inflate(10, 10))  # Shadow effect
    pygame.draw.rect(screen, BLUE if active else BLACK, input_box, 2, border_radius=10)
    
    # Text in the input box
    font = pygame.font.SysFont("Arial", 24)
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (input_box.x + 10, input_box.y + 8))

def draw_background(screen):
    background_color = (WHITE)  # A light grey color
    screen.fill(background_color)

    # Optional: Add a gradient effect or images for a more premium feel

running = True
active = False
input_text = ""
secret_number = random.randint(1, 10)
difficulty = None
attempts = 0
message = "Select a difficulty!"

easy_button = Button(110, 150, 150, 50, "Easy", GREEN, LIGHT_GREEN, DARK_GREEN)
medium_button = Button(280, 150, 150, 50, "Medium", BLUE, LIGHT_BLUE, DARK_BLUE)
hard_button = Button(450, 150, 150, 50, "Hard", RED, LIGHT_RED, DARK_RED)
input_box = pygame.Rect(260, 250, 200, 50)

while running:
    screen.fill(WHITE)  # Clear screen
    draw_background(screen)  # Apply new background

    mouse_pos = pygame.mouse.get_pos()
    clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
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
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:
                if input_text.isdigit():
                    guess = int(input_text)
                    if guess == secret_number:
                        message = f"Congratulations! The number was {secret_number}."
                    else:
                        attempts -= 1
                        message = "Too high!" if guess > secret_number else "Too low!"
                        if attempts == 0:
                            message = f"Game Over! The number was {secret_number}."
                input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    if difficulty is None:
        easy_button.draw(screen, mouse_pos, clicked)
        medium_button.draw(screen, mouse_pos, clicked)
        hard_button.draw(screen, mouse_pos, clicked)
    else:
        draw_input_box(screen, input_box, input_text, active)

    font = pygame.font.SysFont("Arial", 24)
    message_surf = font.render(message, True, BLACK)
    screen.blit(message_surf, (260, 320))

    pygame.display.update()

pygame.quit()