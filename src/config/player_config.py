import json


class PlayerConfig:

    def player_config(self):
        # Leer valores de pantalla desde archivo JSON
        with open('./assets/cfg/player.json', 'r') as f:
            player_config = json.load(f)

        size = (player_config['size']['x'], player_config['size']['y'])
        color = (player_config['color']['r'], player_config['color']
                 ['g'], player_config['color']['b'])
        velocity = (player_config['input_velocity'],
                    player_config['input_velocity'])
        data_player = {}
        data_player['size'] = size
        data_player['color'] = color
        data_player['vel'] = velocity
        f.close()
        return data_player
