import json
import random


class SpawnEventData:

    def level(self):
        f = open('./rules/level_01.json')
        data = json.load(f)
        result = []

        for i in data['enemy_spawn_events']:
            i['used'] = False
            result.append(i)
        f.close()
        return result

    def level_player(self):
        f = open('./rules/level_01.json')
        data = json.load(f)
        f.close()
        return data['player_spawn']

    def enemy_by_type(self, enemy_type: str):
        f = open('./rules/enemies.json')
        enemies = json.load(f)
        enemy = enemies[enemy_type]
        size = (enemy['size']['x'], enemy['size']['y'])
        color = (enemy['color']['r'], enemy['color']['g'], enemy['color']['b'])
        velocity = random.randint(enemy['velocity_min'], enemy['velocity_max'])
        data_enemy = {}
        data_enemy['size'] = size
        data_enemy['color'] = color
        data_enemy['vel'] = velocity
        f.close()
        return data_enemy

    def player_info(self):
        f = open('./rules/player.json')
        player = json.load(f)

        size = (player['size']['x'], player['size']['y'])
        color = (player['color']['r'], player['color']
                 ['g'], player['color']['b'])
        data_player = {}
        data_player['size'] = size
        data_player['color'] = color
        data_player['input_velocity'] = player['input_velocity']
        f.close()
        return data_player

    @staticmethod
    def bullet_info():
        f = open('./rules/bullet.json')
        bullet = json.load(f)

        size = (bullet['size']['x'], bullet['size']['y'])
        color = (bullet['color']['r'], bullet['color']
                 ['g'], bullet['color']['b'])
        data_bullet = {}
        data_bullet['size'] = size
        data_bullet['color'] = color
        data_bullet['velocity'] = bullet['velocity']
        f.close()
        return data_bullet


event_data = SpawnEventData()
game = event_data.level()
