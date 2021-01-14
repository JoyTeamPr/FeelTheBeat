import pygame
import os
import sqlite3
import sys

pygame.font.init()
pygame.init()
win_size = 1000, 700
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption('Feel the beat')
pygame.display.set_icon(pygame.image.load('data/note.png'))
mouse_pos = (0, 0)
mouse_position = (0, 0)
counter, text = 10, '10'.rjust(3)
all_sprites = pygame.sprite.Group()


def load_sound(name):
    sound = ''
    if not pygame.mixer or not pygame.mixer.get_init():
        pass
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error:
        print(f'Файл со звуком "{sound}" не найден')
    return sound


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_color_key(color_key)
    else:
        image = image.convert_alpha()
    return image


def msg(screen_, text_, color=(55, 55, 55), size=30, pos=(-1, -1)):
    font = pygame.font.Font('data/19846.otf', size)
    text_ = font.render(text_, 1, color)
    textpos = text_.get_rect()
    textpos.centerx = pos[0]
    textpos.centery = pos[1]
    screen_.blit(text_, textpos)


def money():
    db = sqlite3.connect('data/base.db')
    sql = db.cursor()
    money_ = sql.execute(
        """SELECT money FROM data""").fetchone()
    lives = sql.execute(
        """SELECT lives FROM data""").fetchone()
    a = money_[0]
    b_ = lives[0]
    msg(screen, str(a), color=(255, 0, 13),
        pos=(905, 47))
    msg(screen, str(b_), color=(255, 255, 0),
        pos=(684, 46))


def motion2():
    flag = False
    if flag:
        pass
    if mouse_pos[0] in range(31, 214):
        if mouse_pos[1] in range(410, 507):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (28, 409, 189, 101), 3)
            else:
                flag = False
        else:
            flag = False

    elif mouse_pos[0] in range(265, 449):
        if mouse_pos[1] in range(410, 509):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (265, 408, 184, 103), 3)
            else:
                flag = False
        else:
            flag = False

    elif mouse_pos[0] in range(497, 682):
        if mouse_pos[1] in range(413, 512):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (498, 411, 184, 102), 3)
            else:
                flag = False
        else:
            flag = False

    elif mouse_pos[0] in range(757, 940):
        if mouse_pos[1] in range(414, 513):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (756, 413, 184, 102), 3)
            else:
                flag = False
        else:
            flag = False
    else:
        flag = False

    if flag:
        pass


def motion1():
    motion2()
    flag = False
    if mouse_pos[0] in range(32, 212):
        if mouse_pos[1] in range(274, 368):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (31, 273, 181, 100), 3)
            else:
                flag = False
        else:
            flag = False

    elif mouse_pos[0] in range(267, 446):
        if mouse_pos[1] in range(272, 372):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (265, 271, 184, 103), 3)
            else:
                flag = False
        else:
            flag = False

    elif mouse_pos[0] in range(504, 682):
        if mouse_pos[1] in range(274, 370):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (503, 272, 181, 101), 3)
            else:
                flag = False
        else:
            flag = False

    elif mouse_pos[0] in range(757, 937):
        if mouse_pos[1] in range(276, 372):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (757, 275, 183, 100), 3)
            else:
                flag = False
        else:
            flag = False

    if flag:
        pass


def motion():
    motion1()
    flag = False
    if flag:
        pass
    if mouse_pos[0] in range(30, 215):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (29, 135, 186, 101), 3)
            else:
                flag = False
        else:
            flag = False

    elif mouse_pos[0] in range(266, 447):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (265, 137, 184, 101), 3)
            else:
                flag = False
        else:
            flag = False

    elif mouse_pos[0] in range(502, 686):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (501, 136, 186, 101), 3)
            else:
                flag = False
        else:
            flag = False

    elif mouse_pos[0] in range(756, 939):
        if mouse_pos[1] in range(140, 240):
            flag = True
            if flag:
                pygame.draw.rect(screen, (255, 255, 255),
                                 (755, 136, 186, 101), 3)
            else:
                flag = False
        else:
            flag = False
    else:
        flag = False

    if flag:
        pass


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

    @staticmethod
    def click():
        if mouse_pos[0] in range(30, 215):
            if mouse_pos[1] in range(140, 240):
                con1 = sqlite3.connect("data/base.db")
                cur1 = con1.cursor()
                lives = cur1.execute(
                    """SELECT lives FROM data""").fetchone()
                lives = lives[0]
                con1.close()
                if lives > 0:
                    os.startfile('JBR.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class AOBTD:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(266, 447):
            if mouse_pos[1] in range(140, 240):
                con1 = sqlite3.connect("data/base.db")
                cur1 = con1.cursor()
                lives = cur1.execute(
                    """SELECT lives FROM data""").fetchone()
                lives = lives[0]
                con1.close()
                if lives > 0:
                    os.startfile('AOBTD.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class DM:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(502, 683):
            if mouse_pos[1] in range(140, 240):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock1 = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Dance Monkey'""").fetchone()
                if clock1[0] == 1:
                    con1 = sqlite3.connect("data/base.db")
                    cur1 = con1.cursor()
                    lives = cur1.execute(
                        """SELECT lives FROM data""").fetchone()
                    lives = lives[0]
                    con1.close()
                    if lives > 0:
                        os.startfile('DM.pyw')
                    else:
                        a = load_sound('data/песня_закрыта.mp3')
                        a.play()
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class BG:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(757, 938):
            if mouse_pos[1] in range(140, 240):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock2 = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Bad Guy'""").fetchone()
                if clock2[0] == 1:
                    con1 = sqlite3.connect("data/base.db")
                    cur1 = con1.cursor()
                    lives = cur1.execute(
                        """SELECT lives FROM data""").fetchone()
                    lives = lives[0]
                    con1.close()
                    if lives > 0:
                        os.startfile('BG.pyw')
                    else:
                        a = load_sound('data/песня_закрыта.mp3')
                        a.play()
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class MSKWYDITD:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(30, 215):
            if mouse_pos[1] in range(274, 370):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock3 = sql.execute(
                    """SELECT open FROM songs WHERE name =
                     'My Songs Know What You Did In The Dark'""").fetchone()
                if clock3[0] == 1:
                    con1 = sqlite3.connect("data/base.db")
                    cur1 = con1.cursor()
                    lives = cur1.execute(
                        """SELECT lives FROM data""").fetchone()
                    lives = lives[0]
                    con1.close()
                    if lives > 0:
                        os.startfile('LEU.pyw')
                    else:
                        a = load_sound('data/песня_закрыта.mp3')
                        a.play()
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class SNA:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(266, 447):
            if mouse_pos[1] in range(274, 370):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock4 = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Seven Nation Army'""").fetchone()
                if clock4[0] == 1:
                    con1 = sqlite3.connect("data/base.db")
                    cur1 = con1.cursor()
                    lives = cur1.execute(
                        """SELECT lives FROM data""").fetchone()
                    lives = lives[0]
                    con1.close()
                    if lives > 0:
                        os.startfile('SNA.pyw')
                    else:
                        a = load_sound('data/песня_закрыта.mp3')
                        a.play()
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class SO:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(502, 683):
            if mouse_pos[1] in range(274, 370):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock5 = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Stressed Out'""").fetchone()
                if clock5[0] == 1:
                    con1 = sqlite3.connect("data/base.db")
                    cur1 = con1.cursor()
                    lives = cur1.execute(
                        """SELECT lives FROM data""").fetchone()
                    lives = lives[0]
                    con1.close()
                    if lives > 0:
                        os.startfile('SO.pyw')
                    else:
                        a = load_sound('data/песня_закрыта.mp3')
                        a.play()
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class OTR:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(757, 938):
            if mouse_pos[1] in range(274, 370):
                con1 = sqlite3.connect("data/base.db")
                cur1 = con1.cursor()
                lives = cur1.execute(
                    """SELECT lives FROM data""").fetchone()
                lives = lives[0]
                con1.close()
                if lives > 0:
                    os.startfile('OTR.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class T:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(30, 215):
            if mouse_pos[1] in range(409, 510):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock6 = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Thunder'""").fetchone()
                if clock6[0] == 1:
                    con1 = sqlite3.connect("data/base.db")
                    cur1 = con1.cursor()
                    lives = cur1.execute(
                        """SELECT lives FROM data""").fetchone()
                    lives = lives[0]
                    con1.close()
                    if lives > 0:
                        os.startfile('T.pyw')
                    else:
                        a = load_sound('data/песня_закрыта.mp3')
                        a.play()
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class BL:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(266, 447):
            if mouse_pos[1] in range(409, 510):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock7 = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Blinding Lights'""").fetchone()
                if clock7[0] == 1:
                    con1 = sqlite3.connect("data/base.db")
                    cur1 = con1.cursor()
                    lives = cur1.execute(
                        """SELECT lives FROM data""").fetchone()
                    lives = lives[0]
                    con1.close()
                    if lives > 0:
                        os.startfile('BL.pyw')
                    else:
                        a = load_sound('data/песня_закрыта.mp3')
                        a.play()
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class RA:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(502, 683):
            if mouse_pos[1] in range(409, 510):
                db = sqlite3.connect('data/base.db')
                sql = db.cursor()
                clock8 = sql.execute(
                    """SELECT open FROM songs WHERE 
                    name = 'Runaway Baby'""").fetchone()
                if clock8[0] == 1:
                    con1 = sqlite3.connect("data/base.db")
                    cur1 = con1.cursor()
                    lives = cur1.execute(
                        """SELECT lives FROM data""").fetchone()
                    lives = lives[0]
                    con1.close()
                    if lives > 0:
                        os.startfile('RA.pyw')
                    else:
                        a = load_sound('data/песня_закрыта.mp3')
                        a.play()
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class A:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(757, 938):
            if mouse_pos[1] in range(409, 510):
                con1 = sqlite3.connect("data/base.db")
                cur1 = con1.cursor()
                lives = cur1.execute("""SELECT lives FROM data""").fetchone()
                lives = lives[0]
                con1.close()
                if lives > 0:
                    os.startfile('A.pyw')
                else:
                    a = load_sound('data/песня_закрыта.mp3')
                    a.play()


class Shop:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(273, 385):
            if mouse_pos[1] in range(610, 700):
                os.startfile('shop.pyw')


class Settings:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(542, 680):
            if mouse_pos[1] in range(610, 700):
                os.startfile('settings.pyw')


class Exit:
    def __init__(self):
        super().__init__()

    @staticmethod
    def click():
        if mouse_pos[0] in range(905, 1000):
            if mouse_pos[1] in range(610, 700):
                sys.exit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()

    BackGround()
    my_cursor_image = load_image('arrow.png')
    my_cursor = pygame.sprite.Sprite(all_sprites)
    my_cursor_image = pygame.transform.scale(my_cursor_image, (60, 85))
    my_cursor.image = my_cursor_image
    my_cursor.rect = my_cursor.image.get_rect()

    pygame.mouse.set_visible(False)
    running = True
    time = 38000
    flag_live = False
    while running:
        all_sprites.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0),
                         (649, 74, 72, 10), 0)
        time -= 1
        if time >= 37000:
            pygame.draw.rect(screen, (255, 255, 255),
                             (650, 75, 70, 8), 0)
        if 30000 < time < 37000:
            pygame.draw.rect(screen, (255, 255, 255),
                             (650, 75, 60, 8), 0)
        if 25000 < time < 30000:
            pygame.draw.rect(screen, (255, 255, 255),
                             (650, 75, 50, 8), 0)
        if 20000 < time < 25000:
            pygame.draw.rect(screen, (255, 255, 255),
                             (650, 75, 40, 8), 0)
        if 15000 < time < 20000:
            pygame.draw.rect(screen, (255, 255, 255),
                             (650, 75, 30, 8), 0)
        if 10000 < time < 15000:
            pygame.draw.rect(screen, (255, 255, 255),
                             (650, 75, 20, 8), 0)
        if 5000 < time < 10000:
            pygame.draw.rect(screen, (255, 255, 255),
                             (650, 75, 10, 8), 0)
        if time < 5000:
            pygame.draw.rect(screen, (255, 255, 255),
                             (650, 75, 0, 8), 0)
        if time <= 0 and not flag_live:
            time = 38000
            flag_live = True
            con = sqlite3.connect("data/base.db")
            cur = con.cursor()
            b = cur.execute("""SELECT lives FROM data""").fetchone()
            b = b[0]
            if b != 5:
                flag_live = False
                cur.execute(
                    f"""UPDATE data SET lives = {b + 1}""")
                con.commit()
            con.close()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                mouse_position = pygame.mouse.get_pos()
                my_cursor.rect.topleft = event.pos
            all_sprites.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                JBR.click()
                AOBTD.click()
                DM.click()
                BG.click()
                MSKWYDITD.click()
                SNA.click()
                SO.click()
                OTR.click()
                T.click()
                BL.click()
                RA.click()
                A.click()
                Shop.click()
                Settings.click()
                Exit.click()
        motion()
        money()
        pygame.display.flip()
        clock.tick(100)
    sys.excepthook = except_hook
    pygame.quit()
