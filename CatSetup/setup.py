from setuptools import setup

APP = ['./SussyMeowmeow/mainMac.py']
DATA_FILES = ['./Audio/aughhhhh.mp3', './Audio/augh_shortened.mp3', './Audio/augh_compressed_sped_up.mp3', './Cat GIFs/idle.GIF', './Cat GIFs/jumpLeft.GIF',
              './Cat GIFs/jumpRight.GIF', './Cat GIFs/jumpUp.GIF', './Cat GIFs/rollLeft.GIF', './Cat GIFs/rollRight.GIF', './Cat GIFs/screm.GIF']
OPTIONS = {
        'iconfile': 'icon.icns',
        'argv_emulation': False
}

setup(
    app=APP,
    name='SussyMeowmeow',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)