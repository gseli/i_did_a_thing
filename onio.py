import pygame
from pygame.rect import RectType

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill("black")
pygame.display.set_caption('iseeyou.exe')

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Set the original positions of the eyes
    eye1_x, eye1_y = 320, 300
    eye2_x, eye2_y = 430, 300

    # Move the eyes towards the mouse position slightly
    eye1_dx = (mouse_x - eye1_x) * 0.1  # 0.1 for smooth movement
    eye1_dy = (mouse_y - eye1_y) * 0.1
    eye2_dx = (mouse_x - eye2_x) * 0.1
    eye2_dy = (mouse_y - eye2_y) * 0.1

    # Update the eye positions
    eye1_x += eye1_dx
    eye1_y += eye1_dy
    eye2_x += eye2_dx
    eye2_y += eye2_dy

    # Fill the screen with black
    screen.fill("black")

    # Draw the face and features
    pygame.draw.ellipse(screen, "white", (200, 200, 400, 333), 0)  # head
    pygame.draw.ellipse(screen, "white", (275, 50, 100, 333), 0)   # left ear
    pygame.draw.ellipse(screen, "white", (425, 50, 100, 333), 0)   # right ear
    pygame.draw.ellipse(screen, "pink", (RectType(450,69,50,150)),0)
    pygame.draw.ellipse(screen, "pink", (RectType(300,69,50,150)),0)
    pygame.draw.lines(screen, "black", False, [(350, 400), (375, 425), (400, 400), (425, 425), (450, 400)], 3)  # mouth
    pygame.draw.line(screen, "black", (310, 250), (375, 300), 4)  # left eyebrow
    pygame.draw.line(screen, "black", (400, 300), (465, 250), 4)  # right eyebrow

    # Draw the eyes, using the updated positions
    pygame.draw.ellipse(screen, "navy blue", (eye1_x, eye1_y, 30, 50), 0)  # left eye
    pygame.draw.ellipse(screen, "navy blue", (eye2_x, eye2_y, 30, 50), 0)  # right eye

    # Update the display
    pygame.display.flip()
