from Xlib.display import colormap

namedColours = {"black":"#000000",
               "white":"#ffffff"}

class colour(object):
    def __init__(self, display):
        self.display = display
        self.colormap = self.display.screen().default_colormap
        self.colours = namedColours

    def getColour(self, colour):
        return self.colormap.alloc_named_color(colour).pixel

