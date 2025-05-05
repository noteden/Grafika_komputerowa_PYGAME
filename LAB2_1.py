import pygame
import math

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zadanie 1")
clock = pygame.time.Clock()

BG_COLOR = (255, 255, 0)
POLY_COLOR = (0, 128, 255)
TEXT_COLOR = (0, 0, 0)

RADIUS = 150
n_vertices = 14
unit_points = [
    (math.cos(2 * math.pi * i / n_vertices), math.sin(2 * math.pi * i / n_vertices))
    for i in range(n_vertices)
]

directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}

transforms = {
    pygame.K_1: {'sx': 0.3, 'sy': 0.3, 'angle':   0, 'shear': 0.0, 'pos': (WIDTH//2, HEIGHT//2)},
    pygame.K_2: {'sx': 1.2, 'sy': 1.2, 'angle':  30, 'shear': 0.0, 'pos': (WIDTH//2, HEIGHT//2)},
    pygame.K_3: {'sx': 0.5,'sy': 1.2, 'angle':   0, 'shear': 0.0, 'pos': (WIDTH//2, HEIGHT//2), 'rev_y': True},
    pygame.K_4: {'sx': 0.7, 'sy': 0.7, 'angle':   0, 'shear': 0.5, 'pos': (WIDTH//2, HEIGHT//2)},
    pygame.K_5: {'sx': 1.2, 'sy': 0.5, 'angle':   0, 'shear': 0.0, 'pos': (WIDTH//2, int(RADIUS * 0.5 + 20))},
    pygame.K_6: {'sx': 0.6, 'sy': 0.6, 'angle':  90, 'shear': 0.5, 'pos': (WIDTH//2, HEIGHT//2)},
    pygame.K_7: {'sx': 0.5, 'sy': 1.2, 'angle': 180, 'shear': 0.0, 'pos': (WIDTH//2, HEIGHT//2)},
    pygame.K_8: { 'sx': 1.2, 'sy': 0.5, 'angle': 30, 'shear': 0.0, 'pos': (int(RADIUS * 1.25 + 10), HEIGHT - int(RADIUS * 0.8 + 10)) },
    pygame.K_9: {'sx': 0.8, 'sy': 0.8, 'angle': 180, 'shear': 0.5, 'pos': (WIDTH - int(RADIUS * 0.8 + 20), HEIGHT//2)}
}

current = transforms[pygame.K_1].copy()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key in transforms:
            current = transforms[event.key].copy()

    screen.fill(BG_COLOR)

    sx = current['sx']
    sy = current['sy']
    angle_rad = math.radians(current['angle'])
    shear = current['shear']
    cx, cy = current['pos']
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    rev_y = current.get('rev_y', False)

    pts = []
    for ux, uy in unit_points:
        x0 = ux * RADIUS * sx
        y0 = uy * RADIUS * sy
        x1 = x0 + shear * y0
        y1 = y0
        xr = x1 * cos_a - y1 * sin_a
        yr = x1 * sin_a + y1 * cos_a
        pts.append((cx + xr, cy + yr))

    pygame.draw.polygon(screen, POLY_COLOR, pts)

    margin = 20
    font = pygame.font.SysFont(None, 32)
    for lbl, (dx, dy) in directions.items():
        draw_lbl = lbl
        if rev_y and lbl in ('N', 'S'):
            draw_lbl = 'S' if lbl == 'N' else 'N'
        dx0, dy0 = dx, dy
        dxr = dx0 * cos_a - dy0 * sin_a
        dyr = dx0 * sin_a + dy0 * cos_a
        dist = (RADIUS * (sy if lbl in ('N', 'S') else sx)) + margin
        tx = cx + dxr * dist
        ty = cy + dyr * dist
        surf = font.render(draw_lbl, True, TEXT_COLOR)
        rect = surf.get_rect(center=(tx, ty))
        screen.blit(surf, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
