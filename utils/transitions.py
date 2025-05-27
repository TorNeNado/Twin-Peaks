import pygame

def fade_transition(screen, from_surface=None, to_surface=None, duration=800):
    clock = pygame.time.Clock()
    overlay = pygame.Surface(screen.get_size())
    overlay.fill((0, 0, 0))
    alpha = 0
    step = 255 / (duration / 16)

    while alpha < 255:
        if from_surface:
            screen.blit(from_surface, (0, 0))
        overlay.set_alpha(int(alpha))
        screen.blit(overlay, (0, 0))
        pygame.display.flip()
        alpha += step
        clock.tick(60)

    if to_surface:
        screen.blit(to_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(150)
