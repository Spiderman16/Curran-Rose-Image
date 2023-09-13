import pygame
import os

pygame.init()

#setup the window, size etc
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600

#create a TUPLE
window = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))

pygame.display.set_caption("Curran Rose")

IMAGES_DIR = "images"

image_filenames = [filename for filename in os.listdir(IMAGES_DIR) if filename.endswith(".jpg")]

images = []

for filename in image_filenames:
    image_path = os.path.join(IMAGES_DIR, filename)
    image = pygame.image.load(image_path)
    images.append(image)

current_image_index = 0

current_image = images[current_image_index]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # Press left arrow key to go to the previous image
                current_image_index = (current_image_index - 1) % len(images)
            elif event.key == pygame.K_RIGHT:  # Press right arrow key to go to the next image
                current_image_index = (current_image_index + 1) % len(images)

            # Update the currently displayed image
            current_image = images[current_image_index]

    window.fill((0, 0, 0))  # Clear the screen
    window.blit(current_image, (0, 0))  # Display the current image
    pygame.display.flip()  # Update the display

pygame.quit()