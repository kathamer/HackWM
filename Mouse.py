from Xlib import X

class mouse:
    def __init__(self):
        self.dragWindow = None

    def configureMouse(self, window):
            window.grab_button(0, X.Mod1Mask, True,
                X.ButtonMotionMask | X.ButtonReleaseMask | X.ButtonPressMask,
                X.GrabModeAsync,
                X.GrabModeAsync,
                X.NONE,
                X.NONE,
                None)

    def handleMouseEvent(self, event):
        if event.detail == 0 and event.type == X.MotionNotify:
            if self.dragWindow is None:
                print("Starting move...")
                self.dragWindow = event.window
                windowGeometry = self.dragWindow.get_geometry()
                self.moveX = windowGeometry.x - event.root_x
                self.moveY = windowGeometry.y - event.root_y
            else:
                print("Moving...")
                self.dragWindow.configure(x=self.moveX + event.root_x, y=self.moveY + event.root_y)

        elif event.type == X.ButtonRelease:
            self.dragWindow = None

	elif event.detail == 2 and event.type == X.ButtonPress:
            event.window.set_input_focus(X.RevertToParent, X.CurrentTime)
            event.window.configure(stack_mode=X.Above)
