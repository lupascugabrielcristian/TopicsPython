import sys
sys.path.append('./')

import Topic
import Link
import Searching

manager = Topic.TopicsManger()
topic = Topic.Topic()
topic.title = "abracadabra"
link = Link.Link()
link.url = "link_ura"
link.tags.append("arad")
link.tags.append("iasi")
topic.links.append(link)
manager.add(topic)

def test1():
	queries = [('arg0', 'abra')]
	result = Searching.generalSearch(queries, manager)

	if result[0][0].title == "abracadabra":
		print "Test1 OK"
	else:
		print "Test1 Failed"

def test2():
	queries = [('arg0', 'ura')]
	result = Searching.generalSearch(queries, manager)
	links = result[1]
	if len(links) == 1 and links[0].url == "link_ura":
		print "Test2 OK"
	else:
		print "Test2 Failed"

def test3():
	queries = [('arg0', 'iasi')]
	result = Searching.generalSearch(queries, manager)
	links = result[1]
	if len(links) == 1 and links[0].url == "link_ura":
		print "Test3 OK"
	else:
		print "Test3 Failed"

def test4():
	queries = [('arg0', 'iasi'), ('arg1', 'abra')]
	result = Searching.generalSearch(queries, manager)
	links = result[1]
	topics = result[0]
	if len(links) == 1 and links[0].url == "link_ura" and len(topics) == 1:
		print "Test4 OK"
	else:
		print "Test4 Failed"

test1()
test2()
test3()
test4()