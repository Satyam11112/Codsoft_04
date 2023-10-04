import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 30

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Load images
rock_image = pygame.image.load("Rock.jpeg")
paper_image = pygame.image.load("Paper.jpeg")
scissors_image = pygame.image.load("scissor.jpeg")

# Define the choices
choices = ["Rock", "Paper", "Scissors"]

def draw_choices():
    choice_font = pygame.font.Font(None, 36)
    text = choice_font.render("Choose your move:", True, WHITE)
    screen.blit(text, (300, 50))

    for i, choice in enumerate(choices):
        image = None
        if choice == "Rock":
            image = rock_image
        elif choice == "Paper":
            image = paper_image
        elif choice == "Scissors":
            image = scissors_image
        screen.blit(image, (200 + i * 200, 150))

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player_choice = None
                if 200 <= event.pos[0] <= 360:
                    player_choice = "Rock"
                elif 400 <= event.pos[0] <= 560:
                    player_choice = "Paper"
                elif 600 <= event.pos[0] <= 760:
                    player_choice = "Scissors"

                if player_choice:
                    computer_choice = random.choice(choices)
                    print("Player:", player_choice)
                    print("Computer:", computer_choice)
                    
        screen.fill((0, 0, 0))
        draw_choices()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if"__name__" == "_main_":
    main()