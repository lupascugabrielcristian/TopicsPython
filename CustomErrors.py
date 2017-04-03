class ArgumentNotFound(Exception):
    def __init__(self, value):
        self.value = "Argument not found: " + value
    def __str__(self):
        return repr(self.value)

class CommandInvalid(Exception):
    def __init__(self, value=""):
        self.value = "Command is invalid. " + str(value)
    def __str__(self):
        return repr(self.value)

class CommandInsuficient(Exception):
    def __init__(self):
        self.value = "Command insufficient"
    def __str__(self):
        return repr(self.value)

class CommandUnknown(Exception):
    def __init__(self):
        self.value = "Command unkown"
    def __str__(self):
        return repr(self.value)

class DataStoreError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)