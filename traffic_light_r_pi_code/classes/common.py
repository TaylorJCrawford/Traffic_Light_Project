import os

class CommonFunctions:

    def __init__(self):
        pass

    def get_path(self):
        """ Returns Path for assets """

        self.PATH = '/home/pi/traffic-light-code/' # Setting Initial Path

        try:
            # If works running on linux env.
            os.uname()
        except:
            # Else running on local dev machine. i.e. windows
            self.PATH = ''
        finally:
            return self.PATH

    def readConfig():
        pass

    def updateConfig():
        pass