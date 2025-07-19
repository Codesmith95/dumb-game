# import the pygame module
import pygame
from pygame.locals import *
# Other imports
import math

def createWindow():
  # Define the background colour
  # using RGB color coding.
  background_colour = (255, 255, 255)

  # Define the dimensions of screen object(width,height)
  screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
  display_info = pygame.display.Info()
  s_width = 1920
  s_height = 1080
  # s_width = display_info.current_w
  # s_height = display_info.current_h

  # Create a background
  map_x = -5000
  map_y = -4000
  map_size = (7659, 7659)
  background_map = pygame.image.load("textures/maps/dawnport-beta-map.png")
  map = pygame.transform.scale(background_map, map_size)

  # Define the properties of the player
  x = s_width / 2
  y = s_height / 2
  width = 25
  height = 25
  vel = 10

  # Set the caption of the screen
  pygame.display.set_caption('The Hero of Dawnport')

  # Fill the background colour to the screen
  screen.fill(background_colour)

  # Update the display
  pygame.display.update()

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
    # Go left
    if keys[pygame.K_LEFT] and map_x < 0:
      map_x += vel
    if keys[pygame.K_RIGHT] and map_x > -(7659 - s_width):
      map_x -= vel
    if keys[pygame.K_UP] and map_y < 0:
      map_y += vel
    if keys[pygame.K_DOWN] and map_y < 7659 - s_height:
      map_y -= vel

    ### DRAW ###
    # Draw the background
    screen.fill(background_colour)

    # Draw the map
    screen.blit(map, (map_x, map_y))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))

    # UPDATE DISPLAY
    pygame.display.update()
