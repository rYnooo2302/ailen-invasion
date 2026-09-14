import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Tài hình con tàu lên và nhận nó
        self.image = pygame.image.load('image/ship1.bmp')
        self.rect = self.image.get_rect()

        # bắt đầu tạo ra một con tàu ở chính giữa màn hình
        self.rect.midbottom = self.screen_rect.midbottom

        # tàu di chuyển sang ngang trên màn hình với trục X
        self.x = float(self.rect.x)

        # tàu di theo hương dọc màn hình với trục y
        self.y = float(self.rect.y)

        #cờ di chuyển trục X
        self.moving_right = False
        self.moving_left = False

        # cờ di chuyển trục Y
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Cập nhật vị trí trục x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Cập nhật vị trí trục y
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed


        # Update rect object from self.x,y.
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)