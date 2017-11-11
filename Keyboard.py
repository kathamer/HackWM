"""
HackWM Keyboard Manager
Handles binding of keys and keypress events in HackWM
by Dylan Hamer
"""

from Xlib import X, XK
from Utilities import runProcess

modifier = X.Mod1Mask  # ALT as modifier

class keyboard:
    def __init__(self, display, rootWindow):
        self.display = display
        self.rootWindow = rootWindow
        self.configureKeys()

    """Return all possible keycodes for a certain key"""
    def getKeycodes(self, key):
        codes = set(code for code, index in self.display.keysym_to_keycodes(key)) 
        return codes

    """Bind keys"""
    def configureKeys(self):
       grabbedKeys = [[X.Mod1Mask, XK.XK_T], [X.Mod1Mask, XK.XK_E], [X.NONE, X.Mod1Mask]]
       for keyBinding in grabbedKeys:  # For each key to grab,
            modifier = keyBinding[0]
            key = keyBinding[1]
            codes = self.getKeycodes(key)
            for code in codes:  # For each code
                self.rootWindow.grab_key(code, modifier, 1, X.GrabModeAsync, X.GrabModeAsync)  # Receive events when the key is pressed

    """Handle key presses"""
    def handleKeyEvent(self, event):
        if event.detail in self.getKeycodes(XK.XK_T): runProcess("/usr/bin/lxterminal")

