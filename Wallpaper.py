"""
Wallpaper
Currently just calls Feh to provide a wallpaper but will soon be a standalone wallpaper manager
by Dylan Hamer
"""

from Utilities import runProcess

def setWallpaper():
    runProcess(["feh", "--bg-scale", "DefaultWallpaper.jpeg"])

