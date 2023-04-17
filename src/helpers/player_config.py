import json


class SpawnPlayer:

    def player_info(self, enemy_type: str):
        f = open('./rules/player.json')
        player = json.load(f)

        size = (player['size']['x'], player['size']['y'])
        color = (player['color']['r'], player['color']
                 ['g'], player['color']['b'])
        velocity = (player['input_velocity'], player['input_velocity'])
        data_player = {}
        data_player['size'] = size
        data_player['color'] = color
        data_player['vel'] = velocity
        f.close()
        return data_player
