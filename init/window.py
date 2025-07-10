# import the pygame module
import pygame
from pygame.locals import *

# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)

# Define the properties of the player
x = 200
y = 200
width = 20
height = 20
vel = 10

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((900, 600))

# Clock
clock = pygame.time.Clock()

# Set the caption of the screen
pygame.display.set_caption('Avoid the projectiles')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display
pygame.display.update()

# Variable to keep our game loop running
running = True

# game loop
while running:
  ###EVENTS
  # for loop through the event queue
  for event in pygame.event.get():
    # Check for QUIT event
    if event.type == pygame.QUIT:
      running = False

  ###Logic
  # Get the keys that are pressed
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and x>0:
    x -= 10
  if keys[pygame.K_RIGHT] and x<900-width:
    x += vel
  if keys[pygame.K_UP] and y>0:
    y -= vel
  if keys[pygame.K_DOWN] and y<600-height:
    y += vel

  ###DRAW
  # Draw the rectangle
  pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))

  # UPDATE DISPLAY
  pygame.display.update()
