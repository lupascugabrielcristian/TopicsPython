class Link:

    def __init__(self):
        self.url = ""
        self.comment = ""

    def getJsonString(self):
        jsonString = {'url': self.url, 'comment': self.comment}
        return jsonString