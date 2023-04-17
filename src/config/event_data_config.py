import json
import random


class EventDataConfig:

    def level_config(self):
        # Leer valores desde archivo JSON
        with open('./assets/cfg/level_01.json', 'r') as f:
            level_config = json.load(f)

        result = []
        for i in level_config['enemy_spawn_events']:
            i['used'] = False
            result.append(i)
        f.close()
        return result

    def level_player_config(self):
        # Leer valores desde archivo JSON
        with open('./assets/cfg/level_01.json', 'r') as f:
            level_player_config = json.load(f)
        f.close()
        return level_player_config['player_spawn']

    def enemies_config(self, enemy_type: str):
        # Leer valores desde archivo JSON
        with open('./assets/cfg/enemies.json', 'r') as f:
            enemies_config = json.load(f)

        enemy = enemies_config[enemy_type]
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
        # Leer valores desde archivo JSON
        with open('./assets/cfg/player.json', 'r') as f:
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
        # Leer valores desde archivo JSON
        with open('./assets/cfg/bullet.json', 'r') as f:
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


event_data = EventDataConfig()
game = event_data.level_config()
