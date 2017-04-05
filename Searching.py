def generalSearch(queries, manager):
	topics = []
	links = []
	for i in range(0, len(manager)):
		topic = manager.get(i)
		if lookForQueriesInTitle(queries, topic):
			topics.append(topic)

		for link in topic.links:
			if lookForQueriesInLink(queries, link):
				links.append(link)
			if lookForQueriesInTags(queries, link):
				links.append(link)
	return (topics, links)

def lookForQueriesInTitle(queries, topic):
	queriesFoundInName = filter(lambda query: topic.title.find(query[1]) != -1, queries)
	if len(queriesFoundInName) > 0:
		return True
	else:
		return False


def lookForQueriesInLink(queries, link):
	queriesFoundInLinks = filter(lambda query: link.url.find(query[1]) != -1, queries)
	if len(queriesFoundInLinks) > 0:
		return True
	else:
		return False


def lookForQueriesInTags(queries, link):
	for tag in link.tags:
		queriesFoundInTag = filter(lambda query: tag.find(query[1]) != -1, queries)
		if len(queriesFoundInTag) > 0:
			return True
	return False