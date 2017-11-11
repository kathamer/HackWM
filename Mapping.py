from Xlib import X

from Mouse import mouse
from Colour import colour

class mapping:
    def __init__(self, display, rootWindow):
        self.display = display
        self.mouseHandler = mouse()
        self.windowList = []

    def handleMapEvent(self, event):
        event.window.map()  # Map window
        event.window.set_input_focus(X.RevertToParent, X.CurrentTime)  # Focus window
        event.window.configure(stack_mode = X.Above)  # Raise window to top
        self.windowList.append(event.window)  # Add window to list of open windows
        self.mouseHandler.configureMouse(event.window)  # Configure mouse events

    def handleUnmapEvent(self, event):
        event.window.unmap()
        self.windowList.remove(event.window)

    def drawBorders(self):
        colourHandler = colour(self.display)

        for window in self.windowList:
            window.configure(border_width = 2)
            if self.display.get_input_focus().focus == window:
                borderColour = colourHandler.colours["white"]
            else:
                borderColour = colourHandler.colours["black"]
            borderColour = colourHandler.getColour(borderColour)
            window.change_attributes(None, border_pixel=borderColour)

    def updateFocus(self):
        self.focusedWindow = self.display.get_input_focus()
