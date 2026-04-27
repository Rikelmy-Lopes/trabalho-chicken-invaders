


from entities.Entity import Entity

RED_COLOR = (255, 0, 0)


class Enemy(Entity):

    def __init__(self, x, y, image_path=None):
        super().__init__(x, y, RED_COLOR, (100, 100), image_path)
        self.health = 100