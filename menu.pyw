import pygame
import os
import sqlite3
import sys
import sqlite3


pygame.font.init()
pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Feel the beat')
pygame.display.set_icon(pygame.image.load('data/note.png'))
mouse_pos = (0, 0)


def load_sound(name):
    if not pygame.mixer or not pygame.mixer.get_init():
        pass
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error:
        print(f'Файл со звуком "{sound}" не найден')
    return sound


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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


def motion():
    flag = False
    if mouse_pos[0] in range(30, 215):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (29, 135, 186, 101), 3)
            else:
                flag = False
                all_sprites.draw(screen)
        else:
            flag = False
            all_sprites.draw(screen)

    elif mouse_pos[0] in range(266, 447):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (265, 137, 184, 101), 3)
            else:
                flag = False
                all_sprites.draw(screen)
        else:
            flag = False
            all_sprites.draw(screen)

    elif mouse_pos[0] in range(502, 686):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (501, 136, 186, 101), 3)
            else:
                flag = False
                all_sprites.draw(screen)
        else:
            flag = False
            all_sprites.draw(screen)

    elif mouse_pos[0] in range(756, 939):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (755, 136, 186, 101), 3)
            else:
                flag = False
                all_sprites.draw(screen)
        else:
            flag = False
            all_sprites.draw(screen)

    elif mouse_pos[0] in range(32, 213):
        if mouse_pos[1] in range(370, 272):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (31, 274, 213, 370), 3)
            else:
                flag = False
                all_sprites.draw(screen)
        else:
            flag = False
            all_sprites.draw(screen)
    else:
        flag = False
        all_sprites.draw(screen)


class BackGround(pygame.sprite.Sprite):
    image = load_image('menu.png')

    def __init__(self):
        super().__init__(all_sprites)
        self.image = BackGround.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        all_sprites.draw(screen)
        all_sprites.update()


class JBR:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(30, 215):
            if mouse_pos[1] in range(140, 240):
                os.startfile('JBR.pyw')


class AOBTD:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(266, 447):
            if mouse_pos[1] in range(140, 240):
                os.startfile('AOBTD.pyw')


class DM:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(502, 683):
            if mouse_pos[1] in range(140, 240):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Dance Monkey'""").fetchone()
                if clock[0] == 1:
                    os.startfile('DM.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class BG:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(757, 938):
            if mouse_pos[1] in range(140, 240):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Bad Guy'""").fetchone()
                if clock[0] == 1:
                    os.startfile('BG.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class MSKWYDITD:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(30, 215):
            if mouse_pos[1] in range(274, 370):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'My Songs Know What 
                    You Did In The Dark'""").fetchone()
                if clock[0] == 1:
                    os.startfile('LEU.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class SNA:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(266, 447):
            if mouse_pos[1] in range(274, 370):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Seven Nation Army'""").fetchone()
                if clock[0] == 1:
                    os.startfile('SNA.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class SO:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(502, 683):
            if mouse_pos[1] in range(274, 370):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Stressed Out'""").fetchone()
                if clock[0] == 1:
                    os.startfile('SO.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class OTR:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(757, 938):
            if mouse_pos[1] in range(274, 370):
                os.startfile('OTR.pyw')


class T:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(30, 215):
            if mouse_pos[1] in range(409, 510):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Thunder'""").fetchone()
                if clock[0] == 1:
                    os.startfile('T.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class BL:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(266, 447):
            if mouse_pos[1] in range(409, 510):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Blinding Lights'""").fetchone()
                if clock[0] == 1:
                    os.startfile('BL.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class RA:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(502, 683):
            if mouse_pos[1] in range(409, 510):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Runaway Baby'""").fetchone()
                if clock[0] == 1:
                    os.startfile('RA.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class A:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(757, 938):
            if mouse_pos[1] in range(409, 510):
                os.startfile('A.pyw')


class Shop:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(273, 385):
            if mouse_pos[1] in range(610, 700):
                os.startfile('shop.pyw')


class Settings:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(542, 680):
            if mouse_pos[1] in range(610, 700):
                os.startfile('settings.pyw')


class Exit:
    def __init__(self):
        super().__init__()

    def click(self):
        if mouse_pos[0] in range(905, 1000):
            if mouse_pos[1] in range(610, 700):
                pygame.quit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    BackGround()
    my_cursor_image = load_image('arrow.png')
    my_cursor = pygame.sprite.Sprite(all_sprites)
    my_cursor_image = pygame.transform.scale(my_cursor_image, (60, 85))
    my_cursor.image = my_cursor_image
    my_cursor.rect = my_cursor.image.get_rect()

    pygame.mouse.set_visible(False)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                my_cursor.rect.topleft = event.pos
                print(mouse_pos)
            if pygame.mouse.get_focused():
                all_sprites.draw(screen)
            all_sprites.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                JBR.click('')
                AOBTD.click('')
                DM.click('')
                BG.click('')
                MSKWYDITD.click('')
                SNA.click('')
                SO.click('')
                OTR.click('')
                T.click('')
                BL.click('')
                RA.click('')
                A.click('')
                Shop.click('')
                Settings.click('')
                Exit.click('')
        motion()
        pygame.display.flip()
        clock.tick(100)
    sys.excepthook = except_hook
    pygame.quit()
