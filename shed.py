

class shed():

    def __init__(self, name, settings):
        self.name = name
        self.settings = settings
        self.state = "off"
        self.configs = settings['states_available']

    def change_state(self, mode):
        # exit current mode
        # enter new mode
        pass