class Link:

    def __init__(self):
        self.url = ""
        self.tags = []

    def getJsonString(self):
        jsonString = {'url': self.url, 'tags': self.tags}
        return jsonString

	def __str__(self):
		stringRepresentation = "Url: " + self.url + " | Tags: "
		for tag in self.tags:
			stringRepresentation += str(tag) + " "
		return stringRepresentation

    def addTag(self, tag):
    	self.tags.append(tag)

    def toJson(self):
    	return {"url": self.url, "tags": self.tags}