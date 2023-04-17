import pygame

import esper
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_input_command import CInputCommand, CommandPhase
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.tags.c_tag_bullet import CTagBullet
from src.ecs.systems.s_collision_bullet_enemy import \
    system_collision_bullet_enemy
from src.ecs.systems.s_collision_player_enemy import \
    system_collision_player_enemy
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner
from src.ecs.systems.s_input_player import system_input_player
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.ecs.systems.s_screen_bullet import system_screen_bullet
from src.ecs.systems.s_screen_player import system_screen_player
from src.helpers.prefab_creator import (create_bullet, create_input_player,
                                        create_player_square)
from src.config.event_data_config import EventDataConfig
from src.config.window_config import WindowConfig


class GameEngine:

    def __init__(self) -> None:
        pygame.init
        pygame.display.set_caption(WindowConfig().tittle_window)
        self.screen = pygame.display.set_mode(
            WindowConfig().size_window, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.framerate = WindowConfig().framerate
        self.delta_time = 0
        self.player_cfg = EventDataConfig().player_info()
        self.level_player_config = EventDataConfig().level_player_config()

        self.ecs_world = esper.World()

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        self._player_entity = create_player_square(
            self.ecs_world, self.player_cfg, self.level_player_config)

        self._player_v_c = self.ecs_world.component_for_entity(
            self._player_entity, CVelocity)

        self._player_t_c = self.ecs_world.component_for_entity(
            self._player_entity, CTransform)
        self._player_s_c = self.ecs_world.component_for_entity(
            self._player_entity, CSurface)

        enemy_spawner_entity = self.ecs_world.create_entity()
        self.ecs_world.add_component(enemy_spawner_entity, CEnemySpawner())

        create_input_player(self.ecs_world)

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0
        self.tiempo_transcurrido = (pygame.time.get_ticks() / 1000.0)

    def _process_events(self):
        for event in pygame.event.get():
            system_input_player(self.ecs_world, event, self._do_action)
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_enemy_spawner(self.ecs_world, self.tiempo_transcurrido)
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)
        system_screen_bullet(self.ecs_world, self.screen)
        system_screen_player(self.ecs_world, self.screen)
        system_collision_player_enemy(
            self.ecs_world, self._player_entity, self.level_player_config)
        system_collision_bullet_enemy(self.ecs_world)
        self.ecs_world._clear_dead_entities()

    def _draw(self):
        self.screen.fill(WindowConfig().color)
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()

    def _clean(self):
        self.ecs_world.clear_database()
        pygame.quit()

    def _do_action(self, c_input: CInputCommand):

        if(c_input.name == "PLAYER_LEFT"):
            if(c_input.phase == CommandPhase.START):
                self._player_v_c.vel.x -= self.player_cfg["input_velocity"]
            elif (c_input.phase == CommandPhase.END):
                self._player_v_c.vel.x += self.player_cfg["input_velocity"]

        if(c_input.name == "PLAYER_RIGHT"):
            if(c_input.phase == CommandPhase.START):
                self._player_v_c.vel.x += self.player_cfg["input_velocity"]
            elif (c_input.phase == CommandPhase.END):
                self._player_v_c.vel.x -= self.player_cfg["input_velocity"]

        if(c_input.name == "PLAYER_UP"):
            if(c_input.phase == CommandPhase.START):
                self._player_v_c.vel.y -= self.player_cfg["input_velocity"]
            elif (c_input.phase == CommandPhase.END):
                self._player_v_c.vel.y += self.player_cfg["input_velocity"]

        if(c_input.name == "PLAYER_DOWN"):
            if(c_input.phase == CommandPhase.START):
                self._player_v_c.vel.y += self.player_cfg["input_velocity"]
            elif (c_input.phase == CommandPhase.END):
                self._player_v_c.vel.y -= self.player_cfg["input_velocity"]

        if(c_input.name == "SHOT_BULLET"):
            if(c_input.phase == CommandPhase.START):
                mouse_pos = pygame.mouse.get_pos()
                position_cursor = pygame.Vector2(mouse_pos)
                c_bullet = self.ecs_world.get_components(CTagBullet)

                if(len(c_bullet) < self.level_player_config["max_bullets"]):
                    create_bullet(self.ecs_world, self._player_t_c.pos,
                                  self._player_s_c.surf.get_size(), position_cursor)

            elif (c_input.phase == CommandPhase.END):
                self._player_v_c.vel.y -= self.player_cfg["input_velocity"]
