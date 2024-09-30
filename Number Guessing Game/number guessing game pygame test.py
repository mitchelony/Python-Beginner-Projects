import pygame
import random

# Initialize Pygame
pygame.init()

# Set up window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Number Guessing Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font for text
font = pygame.font.Font(None, 36)

# Game variables
secret_number = random.randint(1, 10)
attempts = 0
difficulty = None
game_over = False
message = "Choose a difficulty"

# Button class to create interactive buttons
class Button:
    def __init__(self, text, x, y, w, h, color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, WHITE)
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                                   self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Difficulty buttons
easy_button = Button("Easy (10 Attempts)", 200, 50, 200, 50, BLUE)
medium_button = Button("Medium (5 Attempts)", 200, 120, 200, 50, GREEN)
hard_button = Button("Hard (3 Attempts)", 200, 190, 200, 50, RED)

# Input for guess
input_box = pygame.Rect(200, 300, 140, 50)
active = False
input_text = ''

def reset_game():
    global secret_number, attempts, difficulty, game_over, message, input_text
    secret_number = random.randint(1, 10)
    attempts = 0
    difficulty = None
    game_over = False
    message = "Choose a difficulty"
    input_text = ''

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easy_button.is_clicked(event.pos):
                difficulty = 10
                attempts = 10
                message = "Guess a number between 1 and 10!"
            elif medium_button.is_clicked(event.pos):
                difficulty = 5
                attempts = 5
                message = "Guess a number between 1 and 10!"
            elif hard_button.is_clicked(event.pos):
                difficulty = 3
                attempts = 3
                message = "Guess a number between 1 and 10!"
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    if input_text.isdigit():
                        guess = int(input_text)
                        if guess == secret_number:
                            message = f"Congratulations! The number was {secret_number}."
                            game_over = True
                        else:
                            attempts -= 1
                            if guess > secret_number:
                                message = "Too high! Try again."
                            else:
                                message = "Too low! Try again."

                            if attempts == 0:
                                message = f"Game Over! The number was {secret_number}."
                                game_over = True
                        input_text = ''
                    else:
                        message = "Please enter a valid number."
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Draw buttons and input box
    if difficulty is None:
        easy_button.draw(screen)
        medium_button.draw(screen)
        hard_button.draw(screen)
    else:
        # Input box
        pygame.draw.rect(screen, BLUE if active else BLACK, input_box, 2)
        text_surface = font.render(input_text, True, BLACK)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 10))

    # Display message
    message_surface = font.render(message, True, BLACK)
    screen.blit(message_surface, (50, 250))

    # Reset game if over
    if game_over and attempts == 0:
        pygame.time.delay(2000)
        reset_game()

    # Update the display
    pygame.display.flip()

pygame.quit()