

class alarm():

    def __init__(self, name, settings):
        self.settings = settings
        self.name = name
        self.state = settings['state']
        self.type = settings['limit_type']
        self.limit_high = settings['limits']['high']
        self.limit_low = settings['limits']['low']
        self.active_config = settings['active_config']

    def update_state(self, reading):
        if self.state == 0: #alarm currently not active
            if self.type == "inside":
                if reading > self.limit_high or reading < self.limit_low:
                    self.state = 1
        else: # use reset to clear alarm on event for latching functionality
            pass

    def reset_alarm(self):
        self.state = 0