import pygame as pg
import random
pg.init()

# ---------------- SETTINGS ----------------
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_FORCE = -10
COLUMN_SPEED_START = 5
COLUMN_GAP = 200
COLUMN_WIDTH = 70
COLUMN_DISTANCE = 300

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
font = pg.font.Font(None, 40)
bg = pg.image.load("C:\\Users\\moham\\OneDrive\\Desktop\\9b008f67224ff330cfec2ff3f9208f77.jpg").convert()
bg = pg.transform.scale(bg, (WIDTH, HEIGHT))

column_img = pg.image.load("C:\\Users\\moham\\abderezak\\PYTHON\\Column-No-Background.png").convert_alpha()
column_img = pg.transform.scale(column_img, (COLUMN_WIDTH, 400))
column_img_flipped = pg.transform.flip(column_img, False, True)
# --------------- PARTICLE ----------------

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(3, 6)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(1, 3)
        self.life = 20

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.life -= 1

    def draw(self):
        pg.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), self.size)

# --------------- PLAYER ----------------

class Player:
    def __init__(self):
        self.x = WIDTH // 3
        self.y = HEIGHT // 2
        self.radius = 20
        self.velocity = 0
        self.angle = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

        # Rotation effect
        self.angle = -self.velocity * 3
        self.angle = max(-45, min(90, self.angle))

        # Floor & ceiling
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.velocity = 0

        if self.y < self.radius:
            self.y = self.radius
            self.velocity = 0

    def jump(self):
        self.velocity = JUMP_FORCE

    def draw(self):
        # Rotated circle approximation
        pg.draw.circle(screen, (255, 255, 255),
                       (int(self.x), int(self.y)), self.radius)

    def get_rect(self):
        return pg.Rect(self.x - self.radius,
                       self.y - self.radius,
                       self.radius * 2,
                       self.radius * 2)

# --------------- COLUMN ----------------

class Column:
    def __init__(self, x):
        self.x = x
        self.reset()
        self.passed = False

    def reset(self):
        self.height = random.randint(150, 400)
        self.passed = False

    def update(self, speed):
        self.x -= speed
        if self.x < -COLUMN_WIDTH:
            self.x += COLUMN_DISTANCE * len(columns)
            self.reset()

    def draw(self):
        # Top column
        screen.blit(column_img_flipped, (self.x, self.height - 400))
        # Bottom column
        screen.blit(column_img, (self.x, self.height + COLUMN_GAP))
    def collide(self, player_rect):
        top = pg.Rect(self.x, 0, COLUMN_WIDTH, self.height)
        bottom = pg.Rect(self.x,
                         self.height + COLUMN_GAP,
                         COLUMN_WIDTH,
                         HEIGHT)
        return player_rect.colliderect(top) or player_rect.colliderect(bottom)

# --------------- GAME ----------------

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        global columns
        self.player = Player()
        self.score = 0
        self.high_score = getattr(self, "high_score", 0)
        self.state = "menu"
        self.speed = COLUMN_SPEED_START
        self.particles = []

        columns = []
        for i in range(3):
            columns.append(Column(WIDTH + i * COLUMN_DISTANCE))

    def update(self):
        if self.state != "playing":
            return

        self.player.update()

        for column in columns:
            column.update(self.speed)

            if column.collide(self.player.get_rect()):
                self.state = "game_over"
                self.high_score = max(self.high_score, self.score)

            if not column.passed and column.x < self.player.x:
                column.passed = True
                self.score += 1

                # Increase difficulty
                if self.score % 5 == 0:
                    self.speed += 1

        # Update particles
        for particle in self.particles[:]:
            particle.update()
            if particle.life <= 0:
                self.particles.remove(particle)

    def draw(self):
        screen.blit(bg, (0, 0))

        for column in columns:
            column.draw()

        self.player.draw()

        for particle in self.particles:
            particle.draw()

        score_text = font.render(f"Score: {self.score}", True, (255,255,255))
        screen.blit(score_text, (20, 20))

        high_text = font.render(f"High: {self.high_score}", True, (255,255,0))
        screen.blit(high_text, (20, 60))

        if self.state == "menu":
            text = font.render("Press SPACE to Start", True, (255,255,255))
            screen.blit(text, (WIDTH//2 - 150, HEIGHT//2))

        if self.state == "game_over":
            text = font.render("Game Over! Press SPACE", True, (255,0,0))
            screen.blit(text, (WIDTH//2 - 180, HEIGHT//2))

    def jump(self):
        if self.state == "menu":
            self.state = "playing"

        elif self.state == "playing":
            self.player.jump()
            for _ in range(5):
                self.particles.append(
                    Particle(self.player.x, self.player.y)
                )

        elif self.state == "game_over":
            self.reset()



game = Game()
running = True

while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                game.jump()

    game.update()
    game.draw()

    pg.display.flip()

pg.quit()
