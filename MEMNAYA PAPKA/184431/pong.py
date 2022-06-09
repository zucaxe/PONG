from pygame import *
win_width = 700
from random import randint
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
window = display.set_mode((700,500))
background = transform.scale(image.load('phone1.jpg'),(700,500))
clock = time.Clock()
game = True
display.set_caption('pong')
finish = False
a,b=0,0


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_speed,player_y,a,b):
        super().__init__()
        
        self.image = transform.scale(image.load(player_image),(a,b))
        self.speed = player_speed
        self.rect =self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y +=self.speed
        if self.rect.bottom > 500:
            self.rect.bottom = 500
        if self.rect.top < 0:
            self.rect.top = 0


class Player2(GameSprite):
    def update(self):
        
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y +=self.speed
        if self.rect.bottom > 500:
            self.rect.bottom = 500
        if self.rect.top < 0:
            self.rect.top = 0


player1 = Player('leg.png',600,10,win_width-550,100,200)
player2 = Player2('leg2.png', 10,10,win_width-550,100,200)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True: 
        window.blit(background,(0,0))
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()
    display.update()
    clock.tick(120)S    