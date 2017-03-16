import json
import Topic
import constants
import editor
import Command
import CustomErrors


def saveData(data):
    with open(constants.FILE_NAME, 'w') as outfile:
        json.dump(data, outfile)


def loadData():
    with open(constants.FILE_NAME) as json_file:
        data = json.load(json_file)
    return data

def loadManager():
    try:
        with open(constants.FILE_NAME) as json_file:
            data = json.load(json_file)
            manager = Topic.TopicsManger()
            manager.fromJson(data)
            return manager
    except Exception as e:
        print "Failed to load manager. " + str(e)
        return Topic.TopicsManger()
        

def printAllData(manager):
    print "\nThis is all data in data.json file"
    print manager
    print "In total " + str(len(manager)) + " topice"

def addTopic():
    newTopic = Topic.Topic()
    newData = newTopic.getJsonString()
    data = loadData()
    data.append(newData)
    saveData(data)
    print "Added succesfuly"

def showTopic():
    index = int(raw_input("Index? "))
    topic = loadManager().get(index - 1)
    print topic

def showTopicAtIndex(index):
    data = loadData()
    topic = data[index]
    print "Topic " + topic['title']

def searchTopic():
    searchString = raw_input("Search string? ")
    data = loadData()
    manager = Topic.TopicsManger()
    manager.fromJson(data)
    indexes = []
    for index in range (len(manager)):
        topic = manager.get(index)
        if topic.title.find(searchString) != -1:
            indexes.append(index + 1)
    print "Found: "  +str(indexes)
            


def editTopic():
    while(1):
        printAllData()
        print("\n" + editor.getDocStrig())
        command = raw_input("Command> ")
        try:
            editor.editCommand(command)
        except EOFError as e:
            print constants.RED + "Failed: " + constants.RESET + str(e)
        ans = raw_input("Again? (y/n)")
        if ans != "y":
            return

def removeTopic():
    printAllData()
    index = int(raw_input("Index? "))
    manager = loadManager()
    manager.remove(index)
    jsonData = manager.toJson()
    saveData(jsonData)

    print "Removed"
    printAllData()

def runCommand():
    while (1):
        try: 
            command = raw_input("Command > ")
            if command == "exit":
                return
            com = Command.Command(command)
            com.execute()(manager)
        except AssertionError as e:
            print constants.WARNING + "Command failed" + constants.RESET + ". Reason: " + str(e)
        except CustomErrors.DataStoreError as e2:
            print constants.WARNING + "Command completed with problems" + constants.RESET + ". " + str(e2)

def showMenu():
    print ("Available options are")
    print("1. Show data")
    print("2. Add topic")
    print("3. Show topic")
    print("4. Edit topic")
    print("5. Search topic")
    print("6. Sterge topic")
    print("7. Run command")
    try:
        answer = int(raw_input("option: "))
    except ValueError:
        print "Invalid option chosen"
        return
    
    if answer == 1:
        printAllData(manager)
    if answer == 2:
        addTopic()
    if answer == 3:
        showTopic()
    if answer == 4:
        editTopic()
    if answer == 5:
        searchTopic()
    if answer == 6:
        removeTopic()
    if answer == 7:
        runCommand()
        

manager = loadManager()

while(1):
    showMenu()
    answer = raw_input("Continue?(y/n)")
    if answer == 'y':
        continue
    else:
        print("Exiting...")
        exit(0)

