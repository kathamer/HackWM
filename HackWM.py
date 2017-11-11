"""
HackWM
A hackable, modular window manager
by Dylan Hamer
"""

# Xlib imports - Interface with the X window system
from Xlib import X, XK
from Xlib.display import Display

# HackWM imports - Core functions of HackWM
from Keyboard import keyboard
from Mouse import mouse
from Mapping import mapping
from Wallpaper import setWallpaper

class wm:
    def __init__(self):
        self.display = Display()  # Initialise display
        self.rootWindow = self.display.screen().root  # Initialise root window

        self.rootWindow.change_attributes(event_mask = X.SubstructureRedirectMask)

        self.keyboardHandler = keyboard(self.display, self.rootWindow)
        self.mouseHandler = mouse()
        self.mappingHandler = mapping(self.display, self.rootWindow)

        setWallpaper()

    def handleEvents(self):
        if True: #self.display.pending_events() > 0:  # If there is an event in the queue
            event = self.display.next_event()  # Grab it
            print("Got an event! ({})".format(str(event.type)))
            if event.type == X.KeyPress: self.keyboardHandler.handleKeyEvent(event)
            elif event.type == X.MapRequest: self.mappingHandler.handleMapEvent(event)
            elif event.type == X.ButtonPress: self.mouseHandler.handleMouseEvent(event)
            elif event.type == X.ButtonRelease: self.mouseHandler.handleMouseEvent(event)
            elif event.type == X.MotionNotify: self.mouseHandler.handleMouseEvent(event) 

    def loop(self):
        while True:
            self.handleEvents()
            self.mappingHandler.drawBorders()
            self.mappingHandler.updateFocus()

windowManager = wm()
windowManager.loop()
