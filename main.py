# Title: Main Dashboard Script
# Author: Cole Barach
# Date Created: 22.09.28
# Date Updated: 22.10.23
# Function: The main script of the dashboard. Responsible for initializing all systems of the dashboard.

# Includes
import car_data
import gui

# Main Execution
def main():
    gui.Initialize()
    gui.Loop()

# Interrupts
def SetDriveState(state):
    car_data.driveState = state
    gui.Update()

# Script Execution
if __name__ == '__main__':
    main()