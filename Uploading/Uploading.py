import os

download_script = "./download.sh"
upload_scipt = "./upload.sh"

apikey = "8a598b90e251b3edaed8860761b4852a5cbd1"
databaseName = "Topics-E26e"


def uploadJsons():
	print "Uploading to database"
	os.system(upload_scipt)

def downloadJsons():
	print "Downloading"
	os.system(download_script)

def clearDatabase():
	command = "restdb-cli --cmd clean --database " + databaseName + " --apikey " + apikey
	os.system(command)