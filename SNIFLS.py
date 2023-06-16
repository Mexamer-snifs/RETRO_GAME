from pygame import *
# import time as time1

clock = time.Clock()
FPS = 15

width = 700
height = 500
#создай окно игры
okno = display.set_mode((700, 500))
display.set_caption('PUPSEN')
background = transform.scale(image.load('NIGGERS.png'), (700,500))
game = True








class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed, player_x ,player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (20,20))
        self.speed = speed
        self.speedy = 10
        self.rect  = self. image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        okno.blit(self.image,(self.rect.x, self.rect.y))
    def update(self):
        if self.rect.x < 0:
            pass
        if self.rect.x > 700:
            pass
        if self.rect.y<0:
            self.speedy *= -1
        if self.rect.y > 480:
            self.speedy *= -1
        self.rect.y += self.speedy
        self.rect.x += self.speed
        

# class Ball(GameSprite):
    
    
#     def draw(self, shift_x, shift_y):
#         okno.blit(self.image,(self.rect.x +shift_x, self.rect.y + shift_y))
      
            




class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x,wall_y, wall_width, wall_height ):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self. height = wall_height
        self. image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 1 and ball.rect.x <345:
            self.rect.y -=10
        if keys_pressed[K_s] and self.rect.y <  450 and ball.rect.x <345 :
            self.rect.y +=10
    def reset(self):
        okno.blit(self.image,(self.rect.x, self.rect.y))
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 1 and ball.rect.x >345:
            self.rect.y -=15
        if keys_pressed[K_DOWN] and self.rect.y <  450 and ball.rect.x >345 :
            self.rect.y +=15
    def draw(self, shift_x, shift_y):
        self.fill()
        window.blit(self.image,(self.rect.x +shift_x, self.rect.y + shift_y))

WALL1  = Wall(255,255,255, 0, 300, 10, 70)
WALL2 = Wall(255,255,255, 690,300, 10, 70)
WALL3 = Wall(255,255,255, 345, 0 , 5, 700)

font.init()

font = font.Font(None, 70)

win  = font.render('RIGHT PLAYER WIN!', True,(255, 215, 0))

lose  = font.render('LEFT PLAYER WIN!', True,(255, 0, 0))

finish = False


ball= GameSprite('SHAR.png', 10, 300, 300)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        okno.blit(background,(0,0))
        
        WALL1.reset()
        WALL1.update()

        WALL2.reset()
        WALL2.update2()
        WALL3.reset()
        WALL3.update
        ball.update()
        ball.reset()  
        clock.tick(FPS)
        if sprite.collide_rect(ball, WALL1) or sprite.collide_rect(ball, WALL2): 
            ball.speed *= -1
        if ball.rect.x < 0:
            finish = True
            okno.blit(win,(100,300))
        if ball.rect.x >690:
            finish = True
            okno.blit(lose,(100,300))
    display.update()






