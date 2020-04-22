# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os
from settings import Settings
from pygame.sprite import Sprite


class Mob(Sprite):
    def __init__(self, s: Settings, id: int, x: int = 0, y: int = 0):
        super().__init__()
        self.s = s
        self.id = id
        self.image = pygame.image.load(os.path.join(s.img_folder, 'p3_hurt.png'))
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 3
        self.speedy = 5

    def update(self):
        if self.rect.left<=0 or self.rect.right >= self.s.WIDTH:
            self.speedx = -self.speedx + random.randint(-1, 1)
        if self.rect.top <= 0 or self.rect.bottom >= self.s.HEIGHT:
            self.speedy = -self.speedy + random.randint(-1, 1)
        self.rect.x += self.speedx
        self.rect.y += self.speedy

def MobCollide


def main():
    # Создаем игру и окно
    pygame.init()
    pygame.mixer.init()
    s = Settings()
    screen: pygame.Surface = pygame.display.set_mode((s.WIDTH, s.HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    all_spites = pygame.sprite.Group()
    # id Mobs
    id = 1
    for i in range(2):
        mob = Mob(s, id, random.randint(0+50, s.WIDTH-50), random.randint(0+50, s.HEIGHT-50))
        all_spites.add(mob)
        id += 1

    # Загрузка фона
    background = pygame.image.load(os.path.join(s.img_folder, 'cie.png')).convert()
    background_rect = background.get_rect()

    # Цикл игры
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(s.FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        all_spites.update()

        # Рендеринг
        screen.fill(s.BLACK)
        screen.blit(background, background_rect)
        all_spites.draw(screen)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
