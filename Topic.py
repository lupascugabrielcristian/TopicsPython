import random
import json
import Link
import constants
import CustomErrors

class TopicsManger:
    topics = []
    sourceFileName = ""

    def __init_(self):
        self.topics = []

    def fromFile(self, jsonFileName):
        self.sourceFileName = jsonFileName
        self.topics = []
        try:
            with open(jsonFileName) as json_file:
                data = json.load(json_file)
                self.fromJson(data)
        except ValueError:
            raise CustomErrors.DataStoreError("Json file is not readable")

    def fromJson(self, jsonData):
        self.topics = []
        for topicJson in jsonData:
            newTopic = self.parseTopicJson(topicJson)
            self.topics.append(newTopic)
        return self.topics


    def toJson(self):
        jsonString = []
        for topic in self.topics:
            topicJson = {'id': topic.id, 'title': topic.title, 'comment': topic.comment, 'links': topic.links}
            jsonString.append(topicJson)
        return jsonString


    def parseLinks(self, linksJson):
        links = []
        for link in linksJson:
            links.append(link)
        return links

    def parseTopicJson(self, topicJson):
        newTopic = Topic()
        try:
            title = topicJson['title']
            newTopic.title = title
        except KeyError:
            newTopic.title = "Unknown title"
        try:
            id = topicJson['id']
            newTopic.id = id
        except KeyError:
            newTopic.id = "Unknown id"
        try:
            comment = topicJson['comment']
            newTopic.comment = comment
        except KeyError:
            newTopic.comment = "Ukn comment"
        try:
            linksJson = topicJson['links']
            links = map(lambda link: link, linksJson)
            newTopic.links = links
        except KeyError:
            newTopic.links = []
        return newTopic
        
    def getSourceFileName(self):
        return self.sourceFileName

    def get(self, index):
        if index < 0 or index > len(self.topics) - 1:
            raise AssertionError("Invalid index required from topics manager")
        return self.topics[index]

    def remove(self, index):
        if index < 0 or index > len(self.topics):
            raise AssertionError("Index is not in range: " + str(index))
        print "Index: " + str(index)
        del self.topics[index - 1]
        return len(self.topics)

    def add(self, topic):
        self.topics.append(topic)

    def haveItems(self):
        return len(self.topics) > 0

    def __str__(self):
        strs = ""
        for index in range (len(self.topics)):
            strs += str(index + 1) + ". "
            strs += self.topics[index].title
            strs += "\t" + self.topics[index].comment
            strs += "\t" + str(len(self.topics[index].links)) + " links\n"
        return strs

    def __len__(self):
        return len(self.topics)

class Topic:
    title = ""
    id = ""
    links = []
    comment = ""

    def __init__(self):
        self.title = "Default title"
        self.id = self.getId()
        self.links = []
        self.comment = "Default comment"

    def getJsonString(self):
        jsonString = {'title': self.title, 'id': self.id}
        return jsonString

    def getId(self):
        idNumber = random.randint(0,100000)
        return str(idNumber)

    def __str__(self):
        desc =  "\nTitle: " + constants.UNDERLINE + self.title + constants.RESET + "\ncomment: " + self.comment + "\n" 
        if self.links != None and len(self.links) > 0:
            desc += "Links: \n"
            for index in range(0 , len(self.links)):
                desc += "\t" + constants.BOLD  + str(index + 1) + ". " + constants.RESET + self.links[index] + ", \n"
        desc += "\n"
        return desc
    
    # def __repr__(self):
    #     return "Title: " + self.title + "\nLink: " + self.link[0] + "\ncomment: " + self.comment
        