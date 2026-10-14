import pygame
import random

# تشغيل Pygame
pygame.init()

# إعدادات النافذة
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("لعبة تجميع العملات")

# الألوان
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
BLUE = (50, 120, 255)
YELLOW = (255, 220, 50)
RED = (230, 60, 60)

# اللاعب
player = pygame.Rect(100, 100, 40, 40)
player_speed = 5

# العملة
coin = pygame.Rect(
    random.randint(20, WIDTH - 40),
    random.randint(20, HEIGHT - 40),
    20,
    20
)

score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    # الأحداث
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # التحكم باللاعب
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += player_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= player_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += player_speed

    # منع اللاعب من الخروج من الشاشة
    player.clamp_ip(screen.get_rect())

    # جمع العملة
    if player.colliderect(coin):
        score += 1
        coin.x = random.randint(20, WIDTH - 40)
        coin.y = random.randint(20, HEIGHT - 40)

    # رسم الشاشة
    screen.fill(BLACK)

    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.ellipse(screen, YELLOW, coin)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
