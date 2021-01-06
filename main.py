import pygame
import random
import os
import sys

pygame.font.init()
pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Feel the beat')
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


def load_sound(name):
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
        song_jbr = load_sound('music/JBR.mp3')
        song_jbr.play()
        song_jbr.set_volume(0.3)

    def lose(self, name):
        pygame.mixer.stop()
        loosing1 = load_sound('music/Проигрыш (1).mp3')
        loosing2 = load_sound('music/Проигрыш (2).mp3')
        loosing3 = load_sound('music/Проигрыш (3).mp3')
        loosing = [loosing1, loosing2, loosing3]
        random.choice(loosing).play()


class Menu:
    Game.play_jbr('JBR')

