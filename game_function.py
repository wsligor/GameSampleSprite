
class GameFunction():
    def __init__(self, screean):
        self.screean = screean


    def MobCollide(all_sprite):
        for i in all_sprite.copy():
            all_sprite.remove(i)
            for j in all_sprite:
                if i.rect.colliderect(j.rect):
                    if i.weight > j.weight:
                        i.speedx = -i.speedx
                        i.speedy = -i.speedy
                    else:
                        all_sprite.remove(j)
                i.update()
                j.update()
            all_sprite.add(i)


pass

