# import the pygame module
import pygame
from pygame.locals import *

# Define the background colour
# using RGB color coding.
background_colour = (255, 255, 255)

# Define the dimensions of screen object(width,height)
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
display_info = pygame.display.Info()
s_width = display_info.current_w
s_height = display_info.current_h

# Define the properties of the player
x = s_width / 2
y = s_height / 2
width = 20
height = 20
vel = 1

# Define the box the player is in
stageSize = s_width / 4
stageX = stageSize + (s_width / 8)
stageY = ((s_height - stageSize) / 2) + ((s_height - stageSize) / 100)

# Clock
clock = pygame.time.Clock()

# Set the caption of the screen
pygame.display.set_caption('JamFight')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display
pygame.display.update()

# Variable to keep our game loop running
running = True

# game loop
while running:
  ### EVENTS ###
  # for loop through the event queue
  for event in pygame.event.get():
    # Check for QUIT event
    if event.type == pygame.QUIT:
      running = False

  ### LOGIC ###
  # Get the keys that are pressed
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and x > (stageX + 5):
    x -= vel
  if keys[pygame.K_RIGHT] and x < ((stageX + stageSize) - width - 5):
    x += vel
  if keys[pygame.K_UP] and y > (stageY + 5):
    y -= vel
  if keys[pygame.K_DOWN] and y < ((stageY + stageSize) - height - 5):
    y += vel

  ### DRAW ###
  # Draw the background
  screen.fill(background_colour)

  # Draw the box
  pygame.draw.rect(screen, (0, 0, 0), (stageX, stageY, stageSize, stageSize), 6)

  # Draw the player
  pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))

  # UPDATE DISPLAY
  pygame.display.update()
