# HackWM test script
# Runs HaclWM in it's own seperate window to avoid conflicts
# by Dylan Hamer

killall Xephyr  # Kill any existing Xephyr windows
export DISPLAY=:0  # Set display to main display
Xephyr -screen $1 -br :1 &  # Start new Xephyr session
export DISPLAY=:1  # Set display to Xephyr window
python HackWM.py   # Run HackWM
