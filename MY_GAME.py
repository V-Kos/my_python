# Всякие импорты
import pygame
import random
from os import path
# указываю путь файлов
img_dir=path.join(path.dirname(__file__), 'IMGG')

# указываю все глобальные переменные

WIDTH = 720
HEIGHT = 600
FPS = 60

fon_list=["FON.PNG","FON2.PNG","FON3.PNG","FON4.PNG"]
pow_list=["pow1.PNG","pow2.PNG"]

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

color_list=[WHITE,BLACK,RED,GREEN,BLUE,YELLOW]

timeee=0
health=3
kunays=10

messeg_list=["Это моя первая игра","Не судите строго","Ну или судите","я сам еще не определился","(Извиняюсь перед всеми эпилептиками за это)"]

# все вспомогательные функции
def start_menu():
    screen.blit(start_img, start_rect)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False



def end_menu():
    screen.blit(end_img,end_rect)
    draw_text(screen, "Your score:"+str(timeee),random.choice(color_list), 100,100,20)
    draw_text(screen, "Для новой партии нажмите любую кнопку",BLACK, 30,375,580)
    pygame.display.flip()
    pygame.time.wait(3000)
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


def show_health():
    global health
    show=0
    x=20
    while show!=health:
        screen.blit(health_mini_img,(x,20))
        x+=40
        show+=1

def show_kunay():
    global kunays
    show=0
    x=100
    while show!=kunays:
        screen.blit(kunay_mini_img,(20,x))
        x+=10
        show+=1

def check_health():
    global health
    global running
    global kunays
    global end_game
    health-=1
    kunays+=2
    death_explosion = Explosion(player.rect.center, 'lg')
    all_sprites.add(death_explosion)
    player.rect.centerx = WIDTH / random.choice([0.2,0.5,0.8,2,3,4,5,6])
    player.rect.bottom = HEIGHT - 10

    if health==0:
        pygame.time.wait(1500)
        end_game=True



font_name = pygame.font.match_font('gothic')
def draw_text(surf, text,color, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True,color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("123")
clock = pygame.time.Clock()
# Создаем все классы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0



    def update(self):
        self.speedx = 0
        self.speedy=0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -4
        if keystate[pygame.K_RIGHT]:
            self.speedx = 4
        if keystate[pygame.K_UP]:
            self.speedy = -4
        if keystate[pygame.K_DOWN]:
            self.speedy = 4
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT  
        if self.rect.left < 0:
            self.rect.left = 0
    def strike(self):
        shell = Shell(self.rect.centerx, self.rect.top)
        all_sprites.add(shell)
        shells.add(shell)

class Mob1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Shuriken_img, (50, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 12)
        self.speedx = random.randrange(-6, 6)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Shell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(FireBall_img, (60, 60))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -20

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['heal', 'ammo'])
        if self.type=='heal':
            self.image = powerup_images_mini1
        else:
            self.image=powerup_images_mini2
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedx = int(random.choice([3,-2,-1,1,2,3]))
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # убить, если он сдвинется с нижней части экрана
        if self.rect.top > HEIGHT:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
# Загружаем все изображения 
background = pygame.image.load(path.join(img_dir,random.choice(fon_list))).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "ninja1.PNG")).convert()
player_dead_img=pygame.image.load(path.join(img_dir, "dead_ninja.PNG")).convert()
Shuriken_img = pygame.image.load(path.join(img_dir, "fireball.PNG")).convert()
FireBall_img=pygame.image.load(path.join(img_dir, "kunay_img.PNG")).convert()
health_img = pygame.image.load(path.join(img_dir, "ninja_mini.PNG")).convert()
health_mini_img = pygame.transform.scale(health_img, (50, 50))
health_mini_img.set_colorkey(BLACK)
minus_health_img=pygame.image.load(path.join(img_dir, "ninja_dead.PNG")).convert()
minus_health_mini_img = pygame.transform.scale(minus_health_img, (40, 40))
powerup_images=pygame.image.load(path.join(img_dir, random.choice(pow_list))).convert()
kunay_img=pygame.image.load(path.join(img_dir, "kunay.PNG")).convert()
kunay_mini_img=pygame.transform.scale(kunay_img, (70, 35))
kunay_mini_img.set_colorkey(BLACK)
powerup_images = {}
powerup_images['heal'] = pygame.image.load(path.join(img_dir, random.choice(pow_list))).convert()
powerup_images_mini1=pygame.transform.scale(powerup_images['heal'], (50, 40))
powerup_images_mini1.set_colorkey(WHITE)
powerup_images['ammo'] = pygame.image.load(path.join(img_dir, "pow_kunays.PNG")).convert()
powerup_images_mini2=pygame.transform.scale(powerup_images['ammo'], (50, 40))
powerup_images_mini2.set_colorkey(WHITE)
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
start_img1= pygame.image.load(path.join(img_dir, "start.PNG")).convert()
start_img=pygame.transform.scale(start_img1, (WIDTH, HEIGHT))
start_rect = start_img.get_rect()
end_img1 = pygame.image.load(path.join(img_dir,"end.jpg")).convert()
end_img=pygame.transform.scale(end_img1, (WIDTH, HEIGHT))
end_rect = end_img.get_rect()
for i in range(4):
    filename = 'fire{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)

# Собираем все спрайты
all_sprites = pygame.sprite.Group()
shells = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
powerups = pygame.sprite.Group()

all_sprites.add(player)
for i in range(12):
    m1 = Mob1()
    all_sprites.add(m1)
    mobs.add(m1)


# Цикл игры
start_game = True
end_game = False
running = True
while running:
    if start_game:
        start_menu()
        start_game = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        shells = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(12):
            m1 = Mob1()
            all_sprites.add(m1)
            mobs.add(m1)
        timeee = 0

    if end_game :
        end_menu()
        
        end_game = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        shells = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(12):
            m1 = Mob1()
            all_sprites.add(m1)
            mobs.add(m1)
        timeee = 0
        health=3
        kunays=10

    timeee+=1
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if kunays>0:
                    player.strike()
                    kunays-=1
                


    # Обновление
    all_sprites.update()
    # Условия столкновений
    hits = pygame.sprite.groupcollide(mobs, shells, True, True)
    for hit in hits:
        m = Mob1()
        all_sprites.add(m)
        mobs.add(m)
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        if random.random()>0.75:
            pow=Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        check_health()
        pygame.time.wait(150)


    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'heal':
            if health<3:
                health+=1
        if hit.type == 'ammo':
            kunays=10
    



    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen,"Score:"+str(timeee),random.choice(color_list), 50,600,20)
    show_health()
    show_kunay()
    mes_y=20
    for i in messeg_list:
        mes_y+=20
        draw_text(screen,i,random.choice(color_list),25,350,mes_y)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()


pygame.quit()