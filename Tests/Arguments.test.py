import sys
sys.path.insert(0, '../')

import Arguments
import CustomErrors

arguments = Arguments.Arguments()
arguments.parseCommandString("search")
name = arguments.getStringArgument("name")
if name == "search":
	print "No1 OK"
else:
	print "No1 Failed"

arguments.parseCommandString("search")
index = arguments.getIntegerArgument("index")
if index == -1:
	print "No2 OK"
else:
	print "No2 Failed"

arguments.parseCommandString("search bla bla")
args = arguments.getNoNameArguments()
if (args[0][1] == "bla") and (args[1][1] == "bla") and (len(args) == 2):
	print "No3 OK"
else:
	print "No3 Failed"
	print args

arguments.parseCommandString("st t='ura'")
val = arguments.getStringArgument('t')
if val == 'ura':
	print "No4 OK"
else:
	print "NO4 Failed"
	print val

arguments.parseCommandString("st t='ura bora'")
val = arguments.getStringArgument('t')
if val == 'ura bora':
	print "No5 OK"
else:
	print "NO5 Failed"
	print val

arguments.parseCommandString("st t='ura' tt='bora'")
val = arguments.getStringArgument('tt')
if val == 'bora':
	print "No6 OK"
else:
	print "NO6 Failed"
	print val

arguments.parseCommandString("search 4")
index = arguments.getIntegerArgument("index")
if index == 4 and arguments.getStringArgument("name") == "search":
	print "No7 OK"
else:
	print "No7 Failed"