# ZRE-Dashboard-2023
Demo of code developed for Zips Racing Electric

# Directory
## App.py
The main file for the application, execute this file to instance the app. This file is responsible for instancing and initializing the CAN and GUI modules.

## GUI.py
The GUI module contains everything for managing the TKinter GUI.
### Main
#### Constructor
This object, when instanced, will setup an empty TKinter window. An interface for a database, views, subwindows, and interrupts will be established.

*Due to the structure of TK, this class can only be instanced once per application.*
#### Append View
Call this method to insert a View Object into the list of GUI views. The first object appended will act as the default view, being opened when **CloseViews()** is called. The Views in this list can be accessed using **OpenView()**
#### Open View
After views have been properly initialized and appended, this method may be called to **Open()** a specific view by ID or by reference. This function will **Close()** the currently opened view, then **Open()** the desired view.
#### Close Views
After views have been properly initialized and appended, this method may be called to **Close()** the currently opened view. The view that is in position 0 of the views list will be opened.

#### Append Window
Call this method to insert a Window Object into the list of GUI subwindows.
#### Toggle Window
After windows have been properly initialized and appended, this method may be called to **Toggle()** a specific window by ID or by reference. If the specified window is currently open, it will be closed, and vice-versa.

#### Append Keybind
Call this method to insert a Keybind to the Keyboard interrupt. The **key** parameter will accept a string, being the **keysym** identity of the desired key. The command parameter accepts a lambda function that will be executed on the key interrupt.

#### Update
This method, when called, will call the **Update()** function of the currently opened view, if any.

#### Loop
This method, when called, will begin the update loop of the GUI. The function will call the **Update()** function of the GUI, then schedule itself to be called again based on the GUI framerate.

*This funtion is called by the **Begin()** function of the GUI. This function is for internal use only.*

#### Kill
Call this method to destroy the GUI and its children. The main TKinter window and its subwindows will be closed, key interrupts will no longer respond, and the update loop will be halted.

*If the GUI has already been destoryed, this function will do nothing.*

### View
This object represents a root frame for the TKinter main window. In usage with the **Main** class, this object provides a stable framework for a GUI with multiple views and a main menu. Objects inheriting from this class will inherit the behavior for opening and closing, initialization, and updating. These methods may be overrided appropriately.

### Window
This object represents a TopLevel object for the TKinter main window. In usage with the **Main** class, this object provides a stable framework for a GUI with Subwindows. Objects inheriting from this class will inherit the behavior opening, closing, toggling, and updating. These methods may be overrided appropriately.
