import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface

from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_tag_player import CTagPlayer


def system_screen_player(world: esper.World, screen: pygame.Surface):

    screen_rect = screen.get_rect()

    components = world.get_components(
        CTransform, CVelocity, CSurface, CTagPlayer)
    c_t: CTransform
    c_v: CVelocity
    c_s: CSurface

    for entity, (c_t, c_v, c_s, ct_p) in components:
        player_rect = c_s.surf.get_rect(topleft=c_t.pos)

        if player_rect.left <= 0 or player_rect.right >= screen_rect.width:

            player_rect.clamp_ip(screen_rect)
            c_t.pos.x = player_rect.x

        if player_rect.top <= 0 or player_rect.bottom >= screen_rect.height:

            player_rect.clamp_ip(screen_rect)
            c_t.pos.y = player_rect.y
