import pygame


class Snake(pygame.sprite.Sprite):
    # TODO: Make Snake a chain of Blocks
    def __init__(self, color, width, height, x, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        # self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, color, (x, y, width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def setX(self, x):
        self.x += x
        return self
    
    """
    Method the will change the direction of the Snake towards the left
    """
    
    def moveLeft(self):
        # self.x -= self.width
        # all_sprite_list.add(Snake(WHITE, self.width, self.height, self.x, self.y))
        # return Snake(WHITE, self.width, self.height, self.x, self.y)
        return (-10, 0)
    
    """
    Method that will change the direction of the Snake toward the right
    """
    
    def moveRight(self):
        # self.x += self.width
        # all_sprite_list.add(Snake(WHITE, self.width, self.height, self.x, self.y))
        return (10, 0)
        # return self.rect.move_ip(30,30)
        # return Snake(WHITE, self.width, self.height, self.x, self.y)
    
    """
    Method that will change the direction of the Snake to go upward
    """
    
    def moveUp(self):
        # self.y -= self.width
        # all_sprite_list.add(Snake(WHITE, self.width, self.height, self.x, self.y))
        # return Snake(WHITE, self.width, self.height, self.x, self.y)
        return (0, -10)
    
    """
    Method that will change the direction of the Snake to go downward
    """
    
    def moveDown(self):
        # self.y += self.width
        # all_sprite_list.add(Snake(WHITE, self.width, self.height, self.x, self.y))
        # return Snake(WHITE, self.width, self.height, self.x, self.y)
        return (0, 10)