

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


class alarm():
    def __init__(self, name, settings):
        self.settings = settings
        self.name = name
        self.state = settings["state"]
        self.type = settings["limit_type"]
        self.limit_high = settings["limits"]["high"]
        self.limit_low = settings["limits"]["low"]
        self.active_config = settings["active_config"]

    def update_state(self, reading):
        if self.state == 0: 
            if self.type == "inside":
                if float(reading) > float(self.limit_high) or float(reading) < float(self.limit_low):
                    self.state = 1
        elif self.state == 1:
            pass
    
    def reset(self):
        self.state = 0

    def alarm_output(self):
        return self.active_config

    def change_limit(self, limit, lim_set):
        """
        lim name: name from javascript including "high_" or "low_" as the prefix
        lim_set: set limit value entered in web interface
        """
        if limit == "low" and lim_set.isnumeric():
            self.limit_low = lim_set
            print("Change alarm great success!")
        if limit == "high" and lim_set.isnumeric():
            self.limit_high = lim_set
