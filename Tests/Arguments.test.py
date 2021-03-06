import sys
sys.path.insert(0, '../')
sys.path.append('./')

import Arguments
import CustomErrors

arguments = Arguments.Arguments()

def test1():
	arguments.parseCommandString("search")
	name = arguments.getStringArgument("name")
	if name == "search" and len(arguments.arguments) == 1:
		print "No1 OK"
	else:
		print "No1 Failed"
		print arguments.arguments

def test2():
	arguments.parseCommandString("search")
	try:
		arguments.getIntegerArgument("index")
	except CustomErrors.ArgumentNotFound:
		if len(arguments.arguments) == 1:
			print "No2 OK"
			return
	print "No2 Failed"
	print arguments.arguments

def test3():
	arguments.parseCommandString("search bla bla")
	args = arguments.getNoNameArguments()
	if (args[0][1] == "bla") and (args[1][1] == "bla") and (len(args) == 2) and len(arguments.arguments) == 3:
		print "No3 OK"
	else:
		print "No3 Failed"
		print arguments.arguments

def test4():
	arguments.parseCommandString("st t='ura'")
	val = arguments.getStringArgument('t')
	if val == 'ura' and len(arguments.arguments) == 2:
		print "No4 OK"
	else:
		print "NO4 Failed"
		print arguments.arguments

def test5():
	arguments.parseCommandString("st t='ura bora'")
	val = arguments.getStringArgument('t')
	if val == 'ura bora' and len(arguments.arguments) == 2:
		print "No5 OK"
	else:
		print "NO5 Failed"
		print arguments.arguments

def test6():
	arguments.parseCommandString("st t='ura' tt='bora'")
	val = arguments.getStringArgument('tt')
	if val == 'bora' and len(arguments.arguments) == 3:
		print "No6 OK"
	else:
		print "NO6 Failed"
		print arguments.arguments

def test7():
	arguments.parseCommandString("search 4")
	index = arguments.getIntegerArgument("index")
	if index == 4 and arguments.getStringArgument("name") == "search" and len(arguments.arguments) == 2:
		print "No7 OK"
	else:
		print "No7 Failed"
		print arguments.arguments

def test8():
	arguments.parseCommandString("tag 5 t='unu' t='doi'")
	tags = arguments.getMultipleArgumets("t")
	if len(tags) == 2 and tags[0] == "unu" and tags[1] == "doi" and len(arguments.arguments) == 4:
		print "No8 OK"
	else:
		print "No8 Failed"
		print arguments.arguments


def test9():
	arguments.parseCommandString("tag 5 t=unu t=doi")
	tags = arguments.getMultipleArgumets("t")
	if len(tags) == 2 and tags[0] == "unu" and tags[1] == "doi" and len(arguments.arguments) == 4:
		print "No9 OK"
	else:
		print "No9 Failed"
		print arguments.arguments


def test10():
	arguments.parseCommandString("tag 12 link=1 t=tutorial")
	tags = arguments.getMultipleArgumets("t")
	if len(tags) == 1 and tags[0] == "tutorial" and len(arguments.arguments) == 4:
		print "No10 OK"
	else:
		print "No10 Failed"
		print arguments.arguments


test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()