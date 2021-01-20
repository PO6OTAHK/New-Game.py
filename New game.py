# импорт всех библиотек. после чего будут доступны реализованные решения из них
import os
import sys
import pygame

# TODO: импорт клавиш

# инициализация
pygame.init()

# устанавливаем характеристики повторения нажатия клавиш
# set_repeat (задержка, интервал)
pygame.key.set_repeat(200, 70)

# ширина экрана
WIDTH = 550
# высота экрана
HEIGHT = 500
# шаг героя
STEP = 10

# создаем экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
damage_group

#TODO загрузка уровня
def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = []
        for line in mapFile:
            level_map.append(line.strip())
        return level_map


#TODO генерация уровня
def generate_level(level_map):
    new_player, x ,y = None, None, None
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == ".":
                Tile ("grass", x, y)
            elif level_map[y][x] == "#":
                Wall("box", x, y)
            elif level_map[y][x] == "@":
                Tile("grass", x, y)
                new_player = Player(x, y)
    
    return new_player, x, y

tile_images = {'grass': pygame.image.load('D:\Projects\.vscode\KEK\data\grass.png')}
wall_images = {'box': pygame.image.load('D:\Projects\.vscode\KEK\data\kox.png')}
player_image = pygame.image.load('D:\Projects\.vscode\KEK\data\Tank1.png')

tile_width = tile_height = wall_width = wall_height = 50
player_width = 50
player_height = 50

# TODO класс tile
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

# TODO класс wall
class Wall(pygame.sprite.Sprite):
    def __init__(self, wall_type, pos_x, pos_y):
        super().__init__(walls_group, all_sprites)
        self.image = wall_images[wall_type]
        self.rect = self.image.get_rect().move(wall_width * pos_x, wall_height * pos_y)
        self.health = 100

# TODO класс player
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(player_width * pos_x, player_height * pos_y)

    def getDamage(self, damage):
        if self.health > 0:
            self.health -= damage
        return self.health



def load_menu():
    # набор пунктов меню, список []
    elements_menu = [   
        #[x, y, название, цвет обычный, цвет при наведении, id]
        [300, 200, 'Play', [255, 0, 0], [0, 255, 0], 0],
        [300, 270, 'Quit', [255, 0, 0], [0, 255, 0], 1]
    ]
    pygame.key.set_repeat(0, 0)
    pygame.mouse.set_visible(True)

    fon = pygame.transform.scale(pygame.image.load("D:\Projects\.vscode\KEK\data\Fon.png, 550, 500"), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    element = -1
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame. QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if element == 0:
                    pygame.key.set_repeat(200, 70)
                    done = True
                elif element == 1:
                    pygame.quit()
                    sys.exit()
            # Получение позиции курсора мыши
            pointer = pygame.mouse.get_pos()
             # Совпали ли координаты курсора и кнопки
            for el in elements_menu:
                if pointer[0] > el[0] and pointer[0] < el[0] + 100 and pointer[1] < el[1] + 10 and pointer[1] > el[1]:
                    element = el[5]

            
            for el in elements_menu:
                if element == el[5]:
                    screen.blit(Starfont.render(el[2], 1, el[4]), [el[0], el[1] - 40])
                else:
                    # изменение цвета
                    screen.blit(Starfont.render(el[2], 1, el[3]), [el[0], el[1] - 40])

            window.blit(score, [0, 0])
            window.blit(screen, [0, 0])
            pygame.display.flip()

class Damage_object(pygame.sprite.Sprite):
    super().__init__(player_group, all_sprites)



player, level_x, level_y = generate_level(load_level("D:\Projects\.vscode\KEK\data\levels\levelex.txt"))
load_menu()
running = True
# цикл игры
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            load_menu()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= STEP
                if pygame.sprite.spritecollide(player, walls_group, False):
                    player.rect.x += STEP
               
            if event.key == pygame.K_RIGHT:
                player.rect.x += STEP
                if pygame.sprite.spritecollide(player, walls_group, False):
                     player.rect.x -= STEP

            if event.key == pygame.K_UP:
                player.rect.y -= STEP
                if pygame.sprite.spritecollide(player, walls_group, False):
                     player.rect.y += STEP

            if event.key == pygame.K_DOWN:
                player.rect.y += STEP
                if pygame.sprite.spritecollide(player, walls_group, False):
                     player.rect.y -= STEP

    screen.fill(pygame.Color(0, 0, 0))
    tiles_group.draw(screen)
    walls_group.draw(screen)
    player_group.draw(screen)


    pygame.display.flip()

pygame.quit()