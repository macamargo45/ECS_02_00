import json


class WindowConfig:

    def __init__(self) -> None:
        # Leer valores desde archivo JSON
        with open('./assets/cfg/window.json', 'r') as f:
            window_config = json.load(f)

        self.tittle_window = window_config['title']
        self.size_window = (window_config['size']['w'], window_config['size']['h'])
        self.color = (window_config['bg_color']['r'], window_config['bg_color']
                      ['g'], window_config['bg_color']['b'])
        self.framerate = window_config['framerate']
        f.close()
