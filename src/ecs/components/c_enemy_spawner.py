from src.config.event_data_config import EventDataConfig


class CEnemySpawner:
    def __init__(self) -> None:
        eventDataConfig = EventDataConfig()
        level = eventDataConfig.level_config()
        self.level = level
