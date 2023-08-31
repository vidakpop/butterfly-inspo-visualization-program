import pygame
import random
import time

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Butterfly:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.image = pygame.image.load("butterfly.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.angle = 0

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rect = rotated_image.get_rect(center=(self.x, self.y))
        screen.blit(rotated_image, rect)

def draw_text(screen, font, message, butterflies):
    x, y = WIDTH // 2, HEIGHT // 2
    lines = message.split('.')
    line_height = 0
    for line in lines:
        text = font.render(line, True, (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))
        text_rect = text.get_rect(center=(x, y))
        screen.fill(WHITE)
        for butterfly in butterflies:
            #butterfly.update()
            butterfly.draw(screen)
        screen.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(1.3)
        y += line_height
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Butterfly Writing Message")
    clock = pygame.time.Clock()

    font = pygame.font.Font("font.ttf", 52)
    message = "You're overthinking again.\nBreathe. It's okay. \U0001F609 \nYou'll figure it out. \U0001F642 \nAnd even if you don't, that's okay too♥♥. \U0001F60D"


    butterflies = [Butterfly() for _ in range(30)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_text(screen, font, message, butterflies)

        # Update the butterflies for 1 second
        start_time = time.time()
        while time.time() - start_time < 1:
            screen.fill(WHITE)
            for butterfly in butterflies:
                butterfly.draw(screen)
            pygame.display.flip()
            clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
