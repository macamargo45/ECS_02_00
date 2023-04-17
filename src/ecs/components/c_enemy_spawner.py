from src.helpers.spawn_event_data import SpawnEventData


class CEnemySpawner:
    def __init__(self) -> None:
        spawnEventData = SpawnEventData()
        level = spawnEventData.level()
        self.level = level
