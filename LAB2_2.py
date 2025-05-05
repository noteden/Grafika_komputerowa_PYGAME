import pygame
import math
pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zadanie 2")
clock = pygame.time.Clock()

BG = (255, 255, 255)
TRIANGLE_COLOR = (100, 149, 237)
OUTLINE = (0, 0, 0)

def compute_vertices(center, radius, n):
    cx, cy = center
    return [
        (
            cx + radius * math.cos(2 * math.pi * i / n),
            cy + radius * math.sin(2 * math.pi * i / n)
        )
        for i in range(n)
    ]

CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 200
N_VERTICES = 14

vertices = compute_vertices(CENTER, RADIUS, N_VERTICES)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)

    for i in range(N_VERTICES):
        p1 = CENTER
        p2 = vertices[i]
        p3 = vertices[(i + 1) % N_VERTICES]
        pygame.draw.polygon(screen, TRIANGLE_COLOR, [p1, p2, p3])
        pygame.draw.polygon(screen, OUTLINE, [p1, p2, p3], width=1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
