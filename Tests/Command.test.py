import sys
sys.path.append('./')

import Command

com = Command.Command()


def test1():
	com.parseCommandString("search abra")
	if com.parsedArguments[0][1] == "search" and com.parsedArguments[1][1] == "abra":
		print "Test1 OK"
	else:
		print "Test2 Failed"


test1()