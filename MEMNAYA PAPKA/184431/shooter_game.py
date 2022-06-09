import pygame
pygame.init()
from pygame import *
win_width = 700
from random import *
window = display.set_mode((700,500))
background = transform.scale(image.load('phone1.jpg'),(700,500))
clock = time.Clock()
game = True
display.set_caption('pong')
finish = False
a,b=0,0
back = (200, 255, 255)
dx = 3
dy = 3


class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height)
      self.fill_color = back
      if color:
          self.fill_color = color
  def color(self, new_color):
      self.fill_color = new_color
  def fill(self):
      pygame.draw.rect(mw, self.fill_color, self.rect)
  def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)      
  def colliderect(self, rect):
      return self.rect.colliderect(rect)

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

class Ball(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_u] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys[K_j] and self.rect.y < win_width - 80:
            self.rect.y +=self.speed
        if keys[K_h] and self.rect.x > 5:
            self.rect.x-=self.speed
        if keys[K_k] and self.rect.x < win_width - 80:
            self.rect.x +=self.speed
        if self.rect.bottom > 500:
            self.rect.bottom = 500
        if self.rect.top < 0:
            self.rect.top = 0   

class Picture(Area):
  def __init__(self, filename, x=0, y=0, width=10, height=10):
      Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
      self.image = pygame.image.load(filename)
    
  def draw(self):
      background.blit(self.image, (self.rect.x, self.rect.y))
 
ball = Picture('ball4.png', 300, 200, 1, 1)        


player1 = Player('leg4.png',500,10,win_width-550,200,200)
player2 = Player2('leg3.png', 0,10,win_width-550,200,200)



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
        ball.draw()
    display.update()
    clock.tick(120)