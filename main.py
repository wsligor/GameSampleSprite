# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import math
import os
import sys
from settings import Settings
from pygame.sprite import Sprite


class Mob(Sprite):
    def __init__(self, s: Settings, id: int, x: int = 0, y: int = 0):
        super().__init__()
        self.s = s
        self.id = id
        self.color = s.BLACK
        # self.image = pygame.image.load(os.path.join(s.img_folder, 'p3_hurt.png'))
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.color)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = self.rect.w * self.rect.h
        self.speedx = 3
        self.speedy = 5

    def update(self):
        if (self.rect.left - 10) <= 0 or (self.rect.right + 10) >= self.s.WIDTH:
            self.speedx = -self.speedx + random.randint(-1, 1)
        if (self.rect.top - 10) <= 0 or (self.rect.bottom + 10) >= self.s.HEIGHT:
            self.speedy = -self.speedy + random.randint(-1, 1)
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def change_size(self, size, color):
        new_size = self.size + size
        new_size = int(math.sqrt(new_size))
        self.image = pygame.Surface((new_size, new_size))
        self.color = color
        self.image.fill(self.color)
        self.size = new_size ** 2
        pass

    def del_rect(self):
        self.kill()



def MobCollide(all_s, s):
    mob: Mob
    for first in all_s.copy():
        all_s.remove(first)
        # for second in all_s.copy():
        list = pygame.sprite.spritecollide(first, all_s, True)
            # if first.rect.colliderect(second.rect):
                # first.speedx = -first.speedx
                # first.speedy = -first.speedy
                # second.speedx = -second.speedx
                # second.speedy = -second.speedy
                # first_color = first.color
                # second_color = second.color
                # if first_color == s.BLACK and second_color == s.BLACK:
                #     if random.randint(0, 1) == 0:
                #         second.change_size(first.size, s.RED)
                #         first.del_rect()
                #         break
                #     else:
                #         first.change_size(second.size, s.RED)
                #         second.del_rect()
        all_s.add(first)
                        # second.kill()
                # if first.color == s.RED and second.color == s.BLACK:
                #     all_s.remove(second)
                #     first.change_size(100)
                #     first.update()
                #     all_s.add(first)
                #     break
                # if first_color == s.RED and second_color == s.BLACK:
                #     n = random.randint(1, 3)
                #     if n == 3:
                #         first.change_size(100, s.BLUE)
                #         all_s.remove(second)
                #     else:
                #         second.change_size(100, s.RED)
                #     break
                # if first.color == s.RED and second.color == s.RED:
                #     first.update()
                #     second.update()
                #     all_s.add(first)
                #     break


def main():
    # Создаем игру и окно
    if sys.platform in ["win32", "win64"]: os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()
    s = Settings()
    screen: pygame.Surface = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    all_spites = pygame.sprite.Group()
    # id Mobs
    id = 1
    for i in range(5):
        mob = Mob(s, id, random.randint(0 + 100, s.WIDTH - 100), random.randint(0 + 100, s.HEIGHT - 100))
        all_spites.add(mob)
        id += 1

    # Загрузка фона
    # background = pygame.image.load(os.path.join(s.img_folder, 'cie.png')).convert()
    # background_rect = background.get_rect()

    # Цикл игры
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(s.FPS)
        #pygame.time.delay()
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        all_spites.update()
        MobCollide(all_spites, s)
        #all_spites.clear(screen, s.BLACK)

        # Рендеринг
        screen.fill(s.WHITE)
        # screen.blit(background, background_rect)
        all_spites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
