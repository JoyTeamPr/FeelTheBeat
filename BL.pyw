import pygame
import random
import time
import os
import sys
import sqlite3

pygame.font.init()
pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Blinding Lights')
pygame.display.set_icon(pygame.image.load('data/note.png'))


def msg(screen, text, color=(55, 55, 55), size=36, pos=(-1, -1)):
    if pos[0] == -1:
        pos = (screen.get_rect().centerx, pos[1])
    if pos[1] == -1:
        pos = (pos[0], screen.get_rect().centery)
    font = pygame.font.Font('data/19846.otf', size)
    text = font.render(text, 1, color)
    textpos = text.get_rect()
    textpos.centerx = pos[0]
    textpos.centery = pos[1]
    screen.blit(text, textpos)


def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_sound(name):
    sound = ''
    if not pygame.mixer or not pygame.mixer.get_init():
        pass
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error:
        print(f'Файл со звуком "{sound}" не найден')
    return sound


class Game:
    def __init__(self):
        super().__init__()
        self.loosing = []

    def play_jbr(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        value = sql.execute("""SELECT volume FROM data""").fetchone()
        db.close()
        song_jbr = load_sound('music/BL.mp3')
        song_jbr.play()
        song_jbr.set_volume(value[0] / 100)

    def lose(self, name):
        pygame.mixer.stop()
        loosing1 = load_sound('music/Проигрыш (1).mp3')
        loosing2 = load_sound('music/Проигрыш (2).mp3')
        loosing3 = load_sound('music/Проигрыш (3).mp3')
        loosing = [loosing1, loosing2, loosing3]
        random.choice(loosing).play()
        con1 = sqlite3.connect("data/base.db")
        cur1 = con1.cursor()
        lives = cur1.execute("""SELECT lives FROM data""").fetchone()
        lives = lives[0]
        cur1.execute(
            f"""UPDATE data SET lives = {lives - 1}""")
        con1.commit()
        con1.close()


class Menu:
    Game.play_jbr('AOBTD')


class Tile:
    x = 0
    y = -700 // 5
    h = 1000 // 4 - 1
    len_ = 700 // 5
    flag = True

    def pos(self, name):
        self.x = name * 1000 // 4

    def update(self, screen):
        if self.flag:
            pygame.draw.rect(screen, (0, 0, 0),
                             [self.x, self.y, self.h, self.len_])
        else:
            pygame.draw.rect(screen, (180, 180, 180),
                             [self.x, self.y, self.h, self.len_])

    def click(self, position):
        if position[0] in range(self.x, self.h + self.x):
            if position[1] in range(self.y, self.len_ + self.y):
                self.flag = False
                return 0
        return 1


if __name__ == '__main__':
    win = False
    all_sprites = pygame.sprite.Group()
    my_cursor_image = load_image('data/arrow.png')
    my_cursor = pygame.sprite.Sprite(all_sprites)
    my_cursor.image = my_cursor_image
    my_cursor.rect = my_cursor.image.get_rect()
    pygame.mouse.set_visible(True)
    clock = pygame.time.Clock()
    map_ = [0, 1, 2, 1, 3, 2, 1, 0, 2, 3, 1, 0, 3, 1, 0, 2, 1, 3, 0, 1, 3, 2,
            1, 0, 2, 3, 0, 2, 3, 1, 2, 0, 1, 3, 0, 1, 2, 0, 3, 2, 1, 2, 0, 3,
            1, 2, 0, 1, 0, 2, 1, 0, 3, 0, 1, 2, 3, 0, 2, 1, 2, 3, 1, 3, 2, 0,
            2, 1, 3, 2, 3, 1, 0, 2, 3, 2, 1, 0, 2, 3, 1, 0, 2, 3, 0, 2, 1, 0,
            2, 1, 3, 2, 1, 0, 3, 0, 1, 2, 0, 3]
    lost = 0
    time_ = 0
    delta = 60
    sb = []
    speed = 6
    score = 0
    flag = True
    flag1 = True
    while lost == 0:
        for i in map_:
            sb.append(Tile())
            sb[-1].pos(i)
            if lost != 0:
                break
            for j in range(700 // (5 * speed)):
                time_ += 1 / delta
                clock.tick(delta)
                screen.fill((255, 115, 0))
                if lost != 0:
                    break
                for k in range(len(sb)):
                    try:
                        sb[k].y += speed
                        sb[k].update(screen)
                        if sb[k].y > 700 - sb[k].len_ and sb[k].flag:
                            lost = 1
                    finally:
                        pass
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or \
                            (event.type == pygame.KEYDOWN and event.key
                             == pygame.K_ESCAPE):
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        lost = sb[score].click(pygame.mouse.get_pos())
                        score += 1
                    elif event.type == pygame.MOUSEMOTION:
                        my_cursor.rect.topleft = event.pos
                        all_sprites.update()
                if score == 250 and flag:
                    flag = False
                    con = sqlite3.connect("data/base.db")
                    cur = con.cursor()
                    b = cur.execute("""SELECT money FROM data""").fetchone()
                    add = 100
                    print(b)
                    a = b[0]
                    a += add
                    print(a)
                    cur.execute(
                        f"""UPDATE data SET money = {a}""")
                    con.commit()
                    con.close()
                if score >= 511 and flag1:
                    win = True
                    msg(screen, "ВЫ ВЫИГРАЛИ", color=(255, 100, 225),
                        size=70, pos=(-1, -1))
                    pygame.mixer.stop()
                    pygame.display.flip()
                    running = False
                    con = sqlite3.connect("data/base.db")
                    cur = con.cursor()
                    money = cur.execute("""SELECT money FROM data""")
                    add = 100
                    money = money[0]
                    money += add
                    cur.execute(
                        f"""UPDATE data SET money = {money}""")
                    con.commit()
                    con.close()
                    time.sleep(2)
                    sys.exit()
                msg(screen, "СЧЁТ " + str(score), color=(0, 90, 255),
                    pos=(-1, 30))
                pygame.display.update()
    pygame.mixer.music.stop()
    msg(screen, f"ВЫ ПРОИГРАЛИ. ВАШ СЧЁТ: {score}", color=(10, 100, 225),
        size=70, pos=(-1, -1))
    Game.lose('', '')
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()
