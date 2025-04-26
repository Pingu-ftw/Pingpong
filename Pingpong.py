from pygame import *
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
lightblue = (173,216,230)
window.fill(lightblue)
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, playerImage, playerX, playerY, playerSpeed, sizeX, sizeY):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(playerImage), (sizeX, sizeY))
        self.speed = playerSpeed
        self.rect = self.image.get_rect()
        self.rect.x = playerX
        self.rect.y = playerY

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_height - 80:
            self.rect.x += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
            if keys[K_s] and self.rect.x < win_height - 80:
                self.rect.x += self.speed
FPS = 60
game = True
finish = False
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(lightblue)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)