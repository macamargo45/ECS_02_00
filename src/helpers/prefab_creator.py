import math

import pygame

import esper

from src.ecs.components.c_input_command import CInputCommand
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_tag_bullet import CTagBullet
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_player import CTagPlayer
from src.helpers.spawn_event_data import SpawnEventData


def crear_cuadrado(ecs_world: esper.World, size: pygame.Vector2, pos: pygame.Vector2, vel: pygame.Vector2, col: pygame.Color) -> int:
    cuadrado_entity = ecs_world.create_entity()
    ecs_world.add_component(cuadrado_entity, CSurface(size, col))
    ecs_world.add_component(cuadrado_entity, CTransform(pos))
    ecs_world.add_component(cuadrado_entity, CVelocity(vel))
    return cuadrado_entity


def create_enemy_square(world: esper.World, pos: pygame.Vector2, enemy_info: dict):
    size = pygame.Vector2(enemy_info["size"])
    color = pygame.Color(enemy_info["color"])
    velocity = pygame.Vector2(enemy_info['vel'], enemy_info['vel'])
    enemy_entity = crear_cuadrado(world, size, pos, velocity, color)
    world.add_component(enemy_entity, CTagEnemy())


def create_player_square(world: esper.World, player_info: dict, player_lvl_info: dict) -> int:
    size = pygame.Vector2(player_info["size"])
    color = pygame.Color(player_info["color"])
    pos = pygame.Vector2(player_lvl_info['position']['x'] - (
        size.x / 2), player_lvl_info['position']['y'] - (size.y / 2))
    velocity = pygame.Vector2(0, 0)
    player_entity = crear_cuadrado(world, size, pos, velocity, color)
    world.add_component(player_entity, CTagPlayer())
    return player_entity


def create_input_player(word: esper.World):
    input_left = word.create_entity()
    input_right = word.create_entity()
    input_up = word.create_entity()
    input_down = word.create_entity()
    click_left_mouse = word.create_entity()

    word.add_component(input_left, CInputCommand("PLAYER_LEFT", pygame.K_LEFT))
    word.add_component(input_right, CInputCommand(
        "PLAYER_RIGHT", pygame.K_RIGHT))
    word.add_component(input_up, CInputCommand("PLAYER_UP", pygame.K_UP))
    word.add_component(input_down, CInputCommand("PLAYER_DOWN", pygame.K_DOWN))
    word.add_component(click_left_mouse, CInputCommand(
        "SHOT_BULLET", pygame.BUTTON_LEFT))


def create_bullet(world: esper.World, position_player: pygame.Vector2, size_player: pygame.Vector2, position_cursor: pygame.Vector2) -> int:
    bullet_info = SpawnEventData.bullet_info()

    velocity_bullet_ini = position_cursor - position_player
    magnitude = math.sqrt(velocity_bullet_ini.x**2 + velocity_bullet_ini.y**2)
    vel_x_nom = (velocity_bullet_ini.x / magnitude) * bullet_info['velocity']
    vel_y_nom = (velocity_bullet_ini.y / magnitude) * bullet_info['velocity']

    velocity_bullet = pygame.Vector2(vel_x_nom, vel_y_nom)
    pos = pygame.Vector2(
        position_player.x + size_player[0] / 2, position_player.y + size_player[1] / 2)

    bullet_entity = crear_cuadrado(world,
                                   pygame.Vector2(bullet_info['size']),
                                   pos,
                                   velocity_bullet,
                                   pygame.Color(bullet_info['color']))

    world.add_component(bullet_entity, CTagBullet())
    return bullet_entity
