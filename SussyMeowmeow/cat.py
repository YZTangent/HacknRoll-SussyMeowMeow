from enum import Enum
from math import floor
from pathlib import Path
from typing import Callable, TypeVar

from PIL import Image, ImageTk
from playsound import playsound

from .util import load_gif_frames

play_sound = lambda sound_path: playsound(sound_path)

root_dir = Path(__file__).parent.parent
gif_dir = root_dir / "Cat GIFs"
audio_dir = root_dir / "SussyMeowmeow" / "Audio"

class CatType(Enum):
    Idle = "idle"
    JumpUp = "jumpUp"
    JumpRight = "jumpRight"
    JumpLeft = "jumpLeft"
    RollRight = "rollRight"
    RollLeft = "rollLeft"
    Screm = "screm"

T = TypeVar('T')

class Cat:
    cat_type: CatType
    frames: list[Image]
    cached_frames: list[T]
    frame_converter: Callable[Image, T]

    def __init__(
        self,
        cat_type: CatType,
        frame_converter: Callable[Image, T] = lambda frame: ImageTk.PhotoImage(frame)
    ):
        self.cat_type = cat_type

        path = gif_dir / f"{self.cat_type.value}.GIF"
        self.frames = load_gif_frames(path)
        self.frame_converter = frame_converter
        self.cached_frames = [None] * len(self.frames)

    def __repr__(self) -> str:
        return f"Cat(cat_type={self.cat_type})"

    def get_frame_count(self):
        return len(self.frames)

    def get_frame(self, num: int) -> Image:
        if self.cached_frames[num] is None:
            self.cached_frames[num] = self.frame_converter(self.frames[num])

        return self.cached_frames[num]

    def get_pos_delta(self, num: int) -> tuple[int, int]:
        if self.cat_type == CatType.JumpUp:
            y = floor(20 * (num - 3)) if num != 0 else 0
            return (0, y)
        elif self.cat_type == CatType.JumpRight:
            y = floor(3 * (num - len(self.frames) / 2))
            return (12, y)
        elif self.cat_type == CatType.JumpLeft:
            y = floor(3 * (num - len(self.frames) / 2))
            return (-12, y)
        elif self.cat_type == CatType.RollRight:
            return (10, 0)
        elif self.cat_type == CatType.RollLeft:
            return (-10, 0)
        else:
            return (0, 0)

    def play_audio(self, num: int):
        if num == 0 and self.cat_type == CatType.Screm:
            play_sound(audio_dir / "augh_compressed_sped_up.wav")
