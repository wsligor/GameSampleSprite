import os
import pygame

class Settings:
    def __init__(self):
        # Задаем цвета
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        #Параметры экрана
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.FPS = 30

        # Каталог ресурсов игры
        self.game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(self.game_folder, 'images')

        # self.background = pygame.image.load(os.path.join(self.img_folder, 'cie.png')).convert()
        # self.background_rect = self.background.get_rect()