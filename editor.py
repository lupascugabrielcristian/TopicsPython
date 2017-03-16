import constants
import json
import Topic

def loadFile():
    with open(constants.FILE_NAME) as json_file:
        data = json.load(json_file)
    return data

def saveFile(data):
    with open(constants.FILE_NAME, 'w') as outfile:
        json.dump(data, outfile)

def getDocStrig():
    documentation = "Options: al - add link, cl - change link\n"
    documentation += "ct - change title, cc - change comment\n\n"
    documentation += "[topic number] [command option] [value] ex: 2 ct New_title\n"
    return documentation


def editCommand(command):
    #print "Editing command " + constants.OKBLUE + command + constants.RESET
    commandParts = command.split(' ')
    index = int(commandParts[0]) - 1
    value = commandParts[2]
    option = commandParts[1]
    # Get topic
    jsonData = loadFile()
    mangager = Topic.TopicsManger()
    topics = mangager.fromJson(jsonData)
    topic = topics[index]
    # Action from command
    if option ==  "ct":
        topic.title = value
        print "Changind title to " + value
    elif option == "al":
        topic.links.append(value)
        print "Adding link " + value
    elif option == "cc":
        topic.comment = value
        print "Changing comment to " + value
    #Save new data
    jsonData = mangager.toJson()
    saveFile(jsonData)


