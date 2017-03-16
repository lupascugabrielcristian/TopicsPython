import constants
import Topic
import json
import CustomErrors
import os.path

class Command:
	index = -1
	name = ""
	options = []
	arguments = []

	def __init__(self, commandString):
		self.parseCommandString(commandString)
		if self.haveArgument(constants.PRINT_COMMAND):
			print "Command parsed " + constants.GREEN + "OK" + constants.RESET
			print self


	def parseCommandString(self, commandString):
		if len(commandString.split(' ')) > 1:
			self.name = commandString.split(' ')[0]
		else:
			self.name = commandString
			return
		
		try:
			self.index = int(commandString.split(' ')[1])
			argumentsParts = commandString.split(' ')[2:]
		except ValueError:
			self.index = -1   
			argumentsParts = commandString.split(' ')[1:]
		self.arguments = map(lambda part: self.getArgument(part), argumentsParts)
		
	def getArgument(self, text):
		argumentName = text.split('=')[0]
		argumentValue = text.split('=')[1]
		return(argumentName, argumentValue)

	def execute(self):
		if self.name == "":
			print constants.RED + "Command empty" + constants.RESET
			return
			print "Executing"
		if self.name == constants.ADD_TOPIC_COMMAND:
			return self.addTopic
		elif self.name == constants.REMOVE_TOPIC_COMMAND:
			return self.removeTopic
		elif self.name == constants.CHANGE_TITLE_COMMAND:
			return self.changeTitle
		elif self.name == constants.SHOW_ALL_TOPICS_COMMAND:
			return self.showAllData
		elif self.name == constants.SAVE_COMMAND:
			return self.saveData
		elif self.name == constants.ADD_LINK_COMMAND:
			return self.addLink
		elif self.name == constants.CHANGE_COMMENT_COMMAND:
			return self.changeComment
		elif self.name == constants.REMOVE_LINK_COMMAND:
			return self.removeLink
		elif self.name == constants.CHANGE_LINK_COMMAND:
			return self.changeLink
		elif self.name == constants.SHOW_TOPIC:
			return self.showTopic
		elif self.name == constants.SEARCH_TOPICS_COMMAND:
			return self.searchTopics
		elif self.name == constants.USE_DATASTORE_COMMAND:
			return self.useDatastore
		
	def addTopic(self, manager):
		newTopic = Topic.Topic()
		titleArg = filter(lambda argument: argument[0] == "title", self.arguments)
		if len(titleArg) > 0:
			newTopic.title = titleArg[0][1]
		else:
			 newTopic.title = "Default title"
		manager.add(newTopic)

	def removeTopic(self, manager):
		if self.index == -1:
			raise AssertionError("Index not found in command string")
		manager.remove(self.index)
		print "Len: " + str(len(manager))
		
	def changeTitle(self, manager):
		if self.index == -1:
			raise AssertionError("Index not found in command string")
		titleArg = filter(lambda argument: argument[0] == "title", self.arguments)
		if len(titleArg) > 0:
			topic = manager.get(self.index - 1)
			topic.title = titleArg[0][1]
		else:
			raise AssertionError("Title not found in command arguments")
	
	def addLink(self, manager):
		if self.index == -1:
			raise AssertionError("Index not found in command string")
		linkArg = filter(lambda argument: argument[0] == "link", self.arguments)
		if len(linkArg) > 0:
			topic = manager.get(self.index - 1)
			topic.links.append(linkArg[0][1])
		else:
			raise AssertionError("Link not found in command arguments")

	def changeComment(self, manager):
		if self.index == -1:
			raise AssertionError("Index not found in command string")
		topic = manager.get(self.index - 1)
		newComment = self.getStringArgument("comment")
		topic.comment = newComment


	def removeLink(self, manager):
		if self.index == -1:
			raise AssertionError("Index not found in command string")
		linkArg = filter(lambda argument: argument[0] == "link", self.arguments)
		if len(linkArg) > 0:
			topic = manager.get(self.index - 1)
			try:
				linkIndex = int(linkArg[0][1])
				del topic.links[linkIndex - 1]
			except TypeError:
				raise AssertionError("Link index could not be parsed")
		else:
			raise AssertionError("Link index not found in command arguments")        

	def changeLink(self, manager):
		if self.index == -1:
			raise AssertionError("Index not found in command string")
		linkArg = filter(lambda argument: argument[0] == "link", self.arguments)
		if len(linkArg) == 0:
			raise AssertionError("Link index not found in command string")
		newLinkArg = filter(lambda argument: argument[0] == "new", self.arguments)
		if len(newLinkArg) == 0:
			raise AssertionError("New link not found in command string")
		topic = manager.get(self.index - 1)
		try:
			linkIndex = int(linkArg[0][1])
		except ValueError:
			raise AssertionError ("Cannot parse index")
		if linkIndex < 1 or linkIndex > len(topic.links):
			raise AssertionError ("Index value not valid")
		topic.links[linkIndex - 1] = newLinkArg[0][1]

	def showTopic(self, manager):
		if self.index == -1:
			raise AssertionError("Index not found in command string")
		print manager.get(self.index - 1)

	def searchTopics(self, manager):
		query = self.getStringArgument("search")
		if len(manager) == 0:
			raise AssertionError("There are no topics available")
		print "\nFound:"
		for index in range(0, len(manager)):
			title = manager.get(index).title
			if title.find(query) != -1:
				print constants.BOLD +  str(index + 1) + ". " + constants.RESET + title

	def showAllData(self, manager):
		print "\nAll topics: "
		print manager

	def useDatastore(self, manager):
		jsonFileName = self.getStringArgument("db") + ".json"
		if not os.path.isfile(jsonFileName):
			open(jsonFileName, 'a').close()
		manager.fromFile(jsonFileName)
			

	def saveData(self, manager):
		jsonData = manager.toJson()
		fileName = manager.getSourceFileName()
		if fileName == "":
			fileName = constants.FILE_NAME
		print "Saving to " + fileName
		with open(fileName, 'w') as outfile:
			json.dump(jsonData, outfile)

	def getStringArgument(self, argumentName):
		requiredArg = filter(lambda argument: argument[0] == argumentName, self.arguments)
		if len(requiredArg) == 0:
			raise CustomErrors.ArgumentNotFound(argumentName)
		return str(requiredArg[0][1])

	def haveArgument(self, argumentName):
		requiredArg = filter(lambda argument: argument[0] == argumentName, self.arguments)
		return len(requiredArg) > 0

	def __str__(self):
		return "{ Name: " + self.name + " | " + "Index: " + str(self.index) + " | " + "Arguments: " + str(self.arguments) + " }"