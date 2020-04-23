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
        #self.image = pygame.image.load(os.path.join(s.img_folder, 'p3_hurt.png'))
        self.image = pygame.Surface((10, 10))
        self.image.fill(self.color)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = self.rect.w * self.rect.h
        self.speedx = 1
        self.speedy = 1
        self.last_update = pygame.time.get_ticks()

    def update(self):
        if self.rect.left<=0 or self.rect.right >= self.s.WIDTH:
            self.speedx = -self.speedx + random.randint(-1, 1)*0
        if self.rect.top <= 0 or self.rect.bottom >= self.s.HEIGHT:
            self.speedy = -self.speedy + random.randint(-1, 1)*0
        self.rect.move_ip(self.speedx, self.speedy)

    def change_size(self, size):
        new_size = self.size + size
        new_size = int(math.sqrt(new_size))
        self.color = self.s.RED
        self.image = pygame.Surface((new_size, new_size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.size = new_size**2
        pass

def MobCollide(all_s, s):
    mob: Mob
    for i in all_s:
        first: Mob = i
        all_s.remove(first)
        for j in all_s:
            second: Mob = j
            if first.rect.colliderect(second.rect):
                first.speedx = -first.speedx
                first.speedy = -first.speedy
                second.speedx = -second.speedx
                second.speedy = -second.speedy
                pass
                # if first.color == s.RED and second.color == s.BLACK:
                #     all_s.remove(second)
                #     first.change_size(100)
                #     first.update()
                #     all_s.add(first)
                #     break
                # if first.color == s.BLACK and second.color == s.RED:
                #     second.change_size(100)
                #     second.update()
                #     break
                # if first.color == s.RED and second.color == s.RED:
                #     first.speedx = -first.speedx
                #     first.speedy = -first.speedy
                #     second.speedx = -second.speedx
                #     second.speedy = -second.speedy
                #     first.update()
                #     second.update()
                #     all_s.add(first)
                #     break
                # if first.color == s.BLACK and second.color == s.BLACK:
                #     if random.randint(0, 1) == 0:
                #         second.change_size(100)
                #         second.update()
                #     else:
                #         first.change_size(100)
                #         first.update()
                #         all_s.add(first)
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
    for i in range(50):
        mob = Mob(s, id, random.randint(0+50, s.WIDTH-50), random.randint(0+50, s.HEIGHT-50))
        all_spites.add(mob)
        id += 1

    # Загрузка фона
    # background = pygame.image.load(os.path.join(s.img_folder, 'cie.png')).convert()
    # background_rect = background.get_rect()
    last_update = 0
    # Цикл игры
    running = True
    while running:
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        all_spites.update()
        MobCollide(all_spites, s)

        # Рендеринг
        screen.fill(s.WHITE)
        #screen.blit(background, background_rect)
        all_spites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()
        # Держим цикл на правильной скорости
        clock.tick(s.FPS)
        pygame.time.delay(100)
    pygame.quit()


if __name__ == '__main__':
    main()
