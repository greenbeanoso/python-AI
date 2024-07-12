import pygame
import random
import time

# 初始化pygame
pygame.init()
# 設定遊戲視窗大小
screen = pygame.display.set_mode((800, 600))
# 設定遊戲標題
pygame.display.set_caption("射擊遊戲")
# 設定遊戲背景顏色
background = pygame.image.load("pages\space (1).png")
# 設定玩家飛船
player = pygame.image.load("pages/fighter_M (1).png")
player_x = 370
player_y = 480
player_x_change = 0
# 設定敵人飛機
enemy = pygame.image.load("pages\enemy1 (1).png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 4
enemy_y_change = 0
# 設定射擊
bullet = pygame.image.load("pages/bullet (1).png")
bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = "ready"


# 定義函數：畫出玩家飛船
def player_ship(x, y):
    screen.blit(player, (x, y))


# 定義函數：畫出敵人飛機
def enemy_ship(x, y):
    screen.blit(enemy, (x, y))


# 定義函數：發射子彈
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))


# 遊戲主迴圈
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5

            if event.key == pygame.K_RIGHT:
                player_x_change = 5

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 4
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -4
        enemy_y += enemy_y_change
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    player_ship(player_x, player_y)
    enemy_ship(enemy_x, enemy_y)
    pygame.display.update()
