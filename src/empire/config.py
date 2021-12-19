import dataclasses


@dataclasses.dataclass
class GameConfig:
    title: str
    window_width: int
    window_height: int
    fps: int
