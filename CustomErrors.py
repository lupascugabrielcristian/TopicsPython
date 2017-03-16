class ArgumentNotFound(Exception):
    def __init__(self, value):
        self.value = "Argument not found: " + value
    def __str__(self):
        return repr(self.value)

class DataStoreError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)