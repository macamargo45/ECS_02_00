import esper
import pygame

from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.helpers.prefab_creator import create_enemy_square
from src.config.event_data_config import EventDataConfig


def system_enemy_spawner(world: esper.World, tiempo_transcurrido: float):

    components = world.get_components(CEnemySpawner)

    c_e_s: CEnemySpawner
    for entity, (c_e_s) in components:
        my_enemy = next((enemy for enemy in c_e_s[0].level if enemy['time']
                        < tiempo_transcurrido and enemy['used'] == False), None)

        if not my_enemy is None:
            my_enemy['used'] = True
            eventDataConfig = EventDataConfig()
            enemy_data = eventDataConfig.enemies_config(my_enemy['enemy_type'])
            pos = pygame.Vector2(
                my_enemy['position']['x'], my_enemy['position']['y'])
            create_enemy_square(world, pos, enemy_data)
