import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED_X = 7
BALL_SPEED_Y = 7
PADDLE_SPEED = 10

# Configuración del juego
game_over = False
score_left = 0
score_right = 0

# Crear la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Clase para crear las paletas
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_y = 0

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Clase para crear la pelota
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2, HEIGHT//2)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1
        if pygame.sprite.collide_rect(self, left_paddle) or pygame.sprite.collide_rect(self, right_paddle):
            self.speed_x *= -1
        if self.rect.left < 0:
            self.rect.center = (WIDTH//2, HEIGHT//2)
            self.speed_x = BALL_SPEED_X
            self.speed_y = BALL_SPEED_Y
            global score_right
            score_right += 1
        if self.rect.right > WIDTH:
            self.rect.center = (WIDTH//2, HEIGHT//2)
            self.speed_x = -BALL_SPEED_X
            self.speed_y = BALL_SPEED_Y
            global score_left
            score_left += 1

# Crear las paletas
left_paddle = Paddle(50, HEIGHT//2)
right_paddle = Paddle(WIDTH - 50, HEIGHT//2)

# Crear la pelota
ball = Ball()

# Grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(left_paddle, right_paddle, ball)

# Bucle principal del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle.speed_y = -PADDLE_SPEED
            if event.key == pygame.K_s:
                left_paddle.speed_y = PADDLE_SPEED
            if event.key == pygame.K_UP:
                right_paddle.speed_y = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                right_paddle.speed_y = PADDLE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_paddle.speed_y = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle.speed_y = 0

    all_sprites.update()

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    pygame.draw.circle(screen, WHITE, (WIDTH//2, HEIGHT//2), 50, 3)

    all_sprites.draw(screen)

    font = pygame.font.SysFont(None, 50)
    text = font.render(str(score_left), True, WHITE)
    screen.blit(text, (WIDTH//4, 50))
    text = font.render(str(score_right), True, WHITE)
    screen.blit(text, (3*WIDTH//4, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
