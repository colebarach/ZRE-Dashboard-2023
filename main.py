# Title: Main Dashboard Script
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: The main script of the dashboard. Responsible for initializing all systems of the dashboard.

import threading
from threading import Thread

# Includes
import gui
import can

# Main Execution
def Main():
    gui.Initialize()
    Thread(target=can.Begin).start()
    gui.Loop()

def Close():
    gui.Close()
    can.Close()

# Script Execution
if __name__ == '__main__': Main()