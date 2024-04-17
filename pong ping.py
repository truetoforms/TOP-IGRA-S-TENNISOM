from pygame import *

window = display.set_mode((700,500))
background=transform.scale(image.load("fon.jpg"),(700,500))
game = True
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, player_speed,razmer_x,razmer_y):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(razmer_x,razmer_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_presed = key.get_pressed()
        if keys_presed[K_s] and self.rect.y<420:
            self.rect.y+=self.speed
        if keys_presed[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
    def update2(self):
        keys_presed = key.get_pressed()
        if keys_presed[K_DOWN] and self.rect.y<420:
            self.rect.y+=self.speed
        if keys_presed[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
finish = False
speed_x = 3
speed_y = 3
roketka1 = Player('roketka.jpg',0,50,10,65,80)
roketka2 = Player('roketka.jpg',640,50,10,65,80)
tennisni = Player('tennisni.png',350,250,10,65,80)
score1 = 0
score2 = 0

font.init()
font2 = font.SysFont('Arial',36)
font3 = font.SysFont('Arial',60)
while game:
    if finish!=True:
        window.blit(background,(0, 0))
        roketka1.update()
        roketka1.reset()
        roketka2.update2()
        roketka2.reset()
        tennisni.reset()
        text_score=font2.render("Счёт 1:" + str(score1), 1, (0, 0, 0))
        text_score2=font2.render("Счёт 2:" + str(score2), 1, (0, 0, 0))
        win=font3.render("1 ИГРОК ВЫЙГРАЛ", 1, (0, 0, 0))
        win2=font3.render("2 ИГРОК ВЫЙГРАЛ", 1, (0, 0, 0))
        window.blit(text_score,(10,20))
        window.blit(text_score2,(520,20))
        tennisni.rect.x += speed_x
        tennisni.rect.y += speed_y
        if tennisni.rect.x<=0:
            score1+=1
            tennisni = Player('tennisni.png',350,250,10,65,80)
            time.wait(1000)
        if tennisni.rect.x>=700:
            score2+=1
            tennisni = Player('tennisni.png',350,250,10,65,80)
            time.wait(1000)
        if score1 >=10:
            window.blit(win,(100,250))
            finish = True
        if score2 >=10:
            window.blit(win2,(100,250))
            finish = True
        if tennisni.rect.y >500-50 or tennisni.rect.y<0:
            speed_y*=-1
        if sprite.collide_rect(roketka1,tennisni) or sprite.collide_rect(roketka2,tennisni):
            speed_x *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)