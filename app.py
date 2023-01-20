import gui
import can
import database

class App():
    def __init__(self):
        print("APP - Initializing...")
        # Instance Database
        self.database = database.Setup()

        # Instance CAN
        self.can = can.Setup(self.database)
        self.can.Begin()

        # Instance GUI
        self.gui = gui.Setup(self.database)
        self.gui.Begin()

    def Kill(self):
        self.can.Kill()
        print("APP - Terminated.")

print(__name__)

if(__name__ == "__main__"):
    global app
    app = App()
    app.Kill()