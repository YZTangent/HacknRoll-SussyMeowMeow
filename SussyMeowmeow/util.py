from pathlib import Path

from PIL import Image, ImageSequence

def load_gif_frames(path: Path, dimensions: tuple[int, int] = (120, 120)) -> Image:
    frames: list[Image] = []
    with Image.open(path) as img:
        for frame in ImageSequence.Iterator(img):
            resz: Image = frame.resize(dimensions)
            frames.append(resz)
            #bitmap = wx.Bitmap(*dimensions, 32)
            #bitmap.SetData(resz.convert("RGB").tobytes())
            #bitmap.SetAlphaData(resz.convert("RGBA").tobytes()[3::4])

    return frames
