from app import pygame
from app import Path
from app import os
from app import screen, game_font
from app import M, N
from app import WIDTH, HEIGHT
from app import BLACK, WHITE, PURPLE, RED, GREEN

def image(name_img, x, y):
    path = Path(os.path.abspath(__file__))
    directory = path.parent.parent
    img = pygame.image.load(f'{directory}\img\{name_img}').convert()
    img = pygame.transform.scale(img, (x, y))
    return img

class Stick(pygame.sprite.Sprite):
    def __init__(self, x, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, HEIGHT / 2)

class Button(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

def main():

    all_sprites = pygame.sprite.Group()
    all_buttons = pygame.sprite.Group()

    img = image('hand.png', 100, 64)
    button = Button(img, WIDTH / 2, 550)
    all_buttons.add(button)
    img_2 = image('refresh.png', 40, 40)
    button_2 = Button(img_2, 40, 40)
    all_buttons.add(button_2)

    for i in range(N):
        stick = Stick(50 * (i+1), 32, 256)
        all_sprites.add(stick)

    running = True

    gamer = 0
    text = ["Ход первого игрока:", "Ход второго игрока:", "Победил первый игрок :)", "Победил второй игрок :)"]
    location = (WIDTH / 3, 0)

    while running:

        if gamer:
            color = RED
        else:
            color = GREEN

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
                clr_sprites = [s for s in all_sprites if s.image.get_at((0,0)) == color]
                if len (clr_sprites) < M:
                    for sprite in clicked_sprites:
                        sprite.image.fill(color)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button.rect.collidepoint(pos):
                    clr_sprites = [s for s in all_sprites if s.image.get_at((0, 0)) == color]
                    if len (clr_sprites) > 0:
                        all_sprites.remove(clr_sprites)
                        if len(all_sprites) == 0:
                            gamer += 2
                            location = (WIDTH / 4, HEIGHT / 2.5)
                        else:
                            gamer = (gamer + 1) % 2
                if button_2.rect.collidepoint(pos):
                    main()

        all_sprites.update()
        all_buttons.update()
        screen.fill(PURPLE)
        all_sprites.draw(screen)
        all_buttons.draw(screen)

        text_surface = game_font.render(text[gamer], False, BLACK)
        screen.blit(text_surface, location)

        pygame.display.update()

    print("Exited the game loop. Game will quit...")
    quit()