import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface

from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_tag_bullet import CTagBullet


def system_screen_bullet(world: esper.World, screen: pygame.Surface):

    screen_rect = screen.get_rect()

    components = world.get_components(
        CTransform, CVelocity, CSurface, CTagBullet)
    c_t: CTransform
    c_v: CVelocity
    c_s: CSurface

    for entity_bullet, (c_t, c_v, c_s, ct_e) in components:
        bullet_rect = c_s.surf.get_rect(topleft=c_t.pos)
        if bullet_rect.left <= 0 or bullet_rect.right >= (screen_rect.width):
            world.delete_entity(entity_bullet)

        if bullet_rect.top <= 0 or bullet_rect.bottom >= (screen_rect.height):
            world.delete_entity(entity_bullet)
