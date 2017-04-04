import CustomErrors

class Arguments:

	def __init__(self):
		self.arguments = []
		self.command = ""

	def parseCommandString(self, commandString):
		self.arguments = []
		self.command = commandString
		self.getName(self.command)
		self.getIndex(self.command)
		self.getArgumentsWithName(self.command)
		self.getArgumentsWithoutName(self.command)
		return self.arguments
		

	def getName(self, commandString):
		if len(commandString) == 0:
			raise CustomErrors.CommandInvalid()
		if len(commandString.split(' ')) > 1:
			name = commandString.split(' ')[0]
			self.arguments.append(("name", name))
			self.command = commandString[len(name):]
		else:
			name = commandString
			self.arguments.append(("name", name))
			self.command = ""

	def getIndex(self, commandString):
		allParts = commandString.split(' ')
		index = -1
		for part in allParts:
			try:
				index = int(part)
				allParts.remove(part)
				self.command = " ".join(allParts)
				break
			except ValueError:
				continue
		self.arguments.append(("index", index))

	def getArgumentsWithName(self, commandString):
		# name='dfsd dfa'

		while 1:
			index = commandString.find('=')
			if index == -1:
				break
			name = self.getNameBeforeEquals(commandString, index)
			value = self.getValueAfterEquals(commandString, index)
			toRemoveFrom = index - len(name)
			toRemoveTo = value[1]
			self.arguments.append((name, value[0]))
			toReplace = commandString[toRemoveFrom: toRemoveTo + 1]
			self.command = self.command.replace(toReplace, '')
			commandString = commandString[index + len(name) + len(value[0]) + 1:]


	def getArgumentsWithoutName(self, commandString):
		# command name args1 arg1 arg1
		parts = commandString.split(' ')
		parts = filter(lambda part: len(part) > 0, parts)
		for i in range(0, len(parts)):
			self.arguments.append(("arg" + str(i), parts[i]))


	def getValueAfterEquals(self, commandString, index):
		part = commandString[index + 1:]
		if part[0] != '\'':
			return self.getWordAfterEquals(commandString, index)
		endArgIndex = part[1:].find('\'')
		if endArgIndex == -1:
			raise CustomErrors.CommandInvalid("Missing character ' at the end of argument")
		argumentValue = part[1:endArgIndex + 1]
		return (argumentValue, index + len(argumentValue) + 1)

	def getWordAfterEquals(self, commandString, index):
		part = commandString[index + 1:]
		endArgIndex = part[1:].find(' ')
		if endArgIndex == -1:
			endArgIndex = len(commandString) - 1
		argumentValue = part[0:endArgIndex + 1]
		return (argumentValue, index + len(argumentValue))

	def getNameBeforeEquals(self, commandString, index):
		before = commandString[0:index]
		allParts = before.split(' ')
		if len(allParts) > 0:
			return allParts[len(allParts) - 1]
		else:
			return before

	def getArgument(self, text):
		argumentName = text.split('=')[0]
		argumentValue = text.split('=')[1]
		return(argumentName, argumentValue)

	def getStringArgument(self, argumentName):
		if len(argumentName) == 0:
			return ""
		if argumentName == None:
			return self.arguments
		requiredArg = filter(lambda argument: argument[0] == argumentName, self.arguments)
		if len(requiredArg) == 0:
			raise CustomErrors.ArgumentNotFound(argumentName)
		if len(requiredArg[0][1]) < 1:
			raise AssertionError("Argument " + argumentName + " has no value")
		return str(requiredArg[0][1])

	def getIntegerArgument(self, argumentName):
		requiredArg = filter(lambda argument: argument[0] == argumentName, self.arguments)
		if len(requiredArg) == 0:
			raise CustomErrors.ArgumentNotFound(argumentName)
		try:
			linkIndex = int(requiredArg[0][1])
			return linkIndex
		except TypeError:
			raise AssertionError("Link index could not be parsed")

	def getNoNameArguments(self):
		return filter(lambda argument: argument[0].find('arg') == 0, self.arguments)

	def getMultipleArgumets(self, argumentName):
		requiredArgs = filter(lambda argument: argument[0] == argumentName, self.arguments)
		if len(requiredArgs) == 0:
			raise CustomErrors.ArgumentNotFound(argumentName)
		return map(lambda argPair: argPair[1], requiredArgs)

	def haveArgument(self, argumentName):
		requiredArg = filter(lambda argument: argument[0] == argumentName, self.arguments)
		return len(requiredArg) > 0