import sys
import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 600
fps = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pretty Derby Project")

clock = pygame.time.Clock()

# Format font
font = pygame.font.SysFont("Arial", 22)
big_font = pygame.font.SysFont("Arial", 30, bold=True)

# Parameter Fisika
mass = 60.0           # Massa (kg)
force = 120.0         # Gaya dorong (N)

x = 0.0               # Posisi (m)
velocity = 0.0        # Kecepatan (m/s)
acceleration = 0.0    # Percepatan (m/s^2)

initial_x = 0.0

# meter to pixel
SCALE = 10

# VISUAL
GROUND_Y = 430
OBJECT_RADIUS = 25

# Posisi awal objek ke layar
START_SCREEN_X = 100

running = True
paused = False

# Fungsi Reset
def reset_simulation():

    global x, velocity, acceleration

    x = initial_x
    velocity = 0.0
    acceleration = 0.0

# IN GAME
while running:

    # Delta time (detik)
    dt = clock.tick(fps) / 1000.0

    # Player
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Pause / Resume
            if event.key == pygame.K_SPACE:
                paused = not paused

            # Reset
            if event.key == pygame.K_r:
                reset_simulation()

            # Menambah gaya
            if event.key == pygame.K_UP:
                force += 10

            # Mengurangi gaya
            if event.key == pygame.K_DOWN:
                force = max(0, force - 10)

    # PERHITUNGAN FISIKA
        if not paused:

        # Hukum II Newton
            acceleration = force / mass

        # Update kecepatan
            velocity += acceleration * dt

        # Update posisi
            x += velocity * dt

    # KONVERSI POSISI KE PIXEL
    screen_x = START_SCREEN_X + int(x * SCALE)

    # RENDERING
    screen.fill((235, 240, 245))

    # Judul
    title = big_font.render(
        "PROJECT PRETTY DERBY",
        True,
        (25, 40, 60)
    )

    screen.blit(title, (30, 25))

    # Tanah
    pygame.draw.rect(
        screen,
        (100, 170, 100),
        (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y)
    )

    # Garis lintasan
    pygame.draw.line(
        screen,
        (50, 90, 50),
        (0, GROUND_Y),
        (WIDTH, GROUND_Y),
        4
    )

    # Objek bergerak
    pygame.draw.circle(
        screen,
        (40, 110, 220),
        (screen_x, GROUND_Y - OBJECT_RADIUS),
        OBJECT_RADIUS
    )
    
    # PANEL INFO
    info_box = pygame.Rect(30, 100, 350, 230)

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        info_box,
        border_radius=12
    )

    pygame.draw.rect(
        screen,
        (50, 70, 90),
        info_box,
        2,
        border_radius=12
    )

    info = [
        f"Massa        : {mass:.2f} kg",
        f"Gaya         : {force:.2f} N",
        f"Percepatan   : {acceleration:.2f} m/s^2",
        f"Kecepatan    : {velocity:.2f} m/s",
        f"Posisi       : {x:.2f} m"
    ]

    for i, text in enumerate(info):

        rendered = font.render(
            text,
            True,
            (30, 40, 50)
        )

        screen.blit(rendered, (50, 120 + i * 38))

    # Tombol Kontrol

    controls = [
        "SPACE : Pause / Resume",
        "R     : Reset",
        "UP    : Tambah gaya",
        "DOWN  : Kurangi gaya",
        "Mouse : Bergerak"
    ]

    for i, text in enumerate(controls):

        rendered = font.render(
            text,
            True,
            (30, 40, 50)
        )

        screen.blit(rendered, (650, 120 + i * 35))

    # Status simulasi
    status = "PAUSED" if paused else "RUNNING"

    status_text = font.render(
        f"STATUS: {status}",
        True,
        (200, 50, 50) if paused else (20, 120, 50)
    )

    screen.blit(status_text, (650, 300))

    # Update layar
    pygame.display.flip()

# KELUAR PROGRAM


pygame.quit()
sys.exit()




