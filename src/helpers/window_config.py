import json


class WindowConfig:

    def __init__(self) -> None:
        f = open('./rules/window.json')
        data = json.load(f)
        self.tittle_window = data['title']
        self.size_window = (data['size']['w'], data['size']['h'])
        self.color = (data['bg_color']['r'], data['bg_color']
                      ['g'], data['bg_color']['b'])
        self.framerate = data['framerate']
        f.close()
