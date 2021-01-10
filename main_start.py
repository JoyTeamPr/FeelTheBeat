import pygame
import sqlite3
import time
import os

pygame.init()
size = 360, 640
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Feel the beat')
pygame.display.set_icon(pygame.image.load('data/note.png'))
mouse_pos = (0, 0)


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


class BackGround(pygame.sprite.Sprite):
    image = load_image('load.jpg')
    image = pygame.transform.scale(image, (360, 640))

    def __init__(self):
        super().__init__(all_sprites)
        self.image = BackGround.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        all_sprites.draw(screen)
        all_sprites.update()


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    background = BackGround()
    clock = pygame.time.Clock()
    running = True
    a = 0
    while running:
        a += 1
        pygame.display.flip()
        clock.tick(100)
        if a == 250:
            running = False
    os.startfile('menu.pyw')
    pygame.quit()
