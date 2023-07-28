from tkinter import *
from classes.MyClass import myClass

# Create Application Instance with Default Settings.
App = myClass()

# Create Default Main Screen Along With Basic Setup.
App.create_default_main_page_and_place()

# Build App Message Page Components.
App.create_message_page_widgets()

# Start App Inner Loop.
config_last_updated = 0000
App.check_for_update_event_loop(App.PATH + "assets/config.json", config_last_updated)

# Outer or Main App Loop.
App.win.mainloop()