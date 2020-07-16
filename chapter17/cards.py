import pygame
import random


class Card:
    def __init__(self, image, target_pos, num):
        self.image = image
        self.pos = target_pos
        self.num = max(0, min(51, int(num)))

    def draw(self, target_surface):
        patch_rect = ((self.num % 13) * 639 // 13, (self.num // 13) * 64, 639 // 13, 64)
        target_surface.blit(self.image, self.pos, patch_rect)


def draw_random_hand():
    deck = pygame.image.load("Deck_Of_Cards.png")
    surface = pygame.display.set_mode((500, 500))
    list = random.sample(range(0, 52), 5)
    cards = []
    for i in list:
        cards.append(Card(deck, (80 * list.index(i) + 30, 222), i))
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        surface.fill((0, 0, 0))
        for card in cards:
            card.draw(surface)
        pygame.display.flip()
    pygame.quit()


draw_random_hand()