import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def getIdOf(filename):
	dataFileId = ""
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	for gfile in file_list:
		if gfile['title'] == filename:
			print ("ID: " + gfile['id'])
			dataFileId = gfile['id']
			return dataFileId
	raise AssertionError("file " + filename + " not found on drive")

def getId():
	dataFileId = ""
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	for gfile in file_list:
		if gfile['title'] == 'data.json':
			print ("ID: " + gfile['id'])
			dataFileId = gfile['id']
			return dataFileId
	raise AssertionError("file not found on drive")

def downloadJson():
	try:
		dataFileId = getId()
		googleDataFile = drive.CreateFile({'id': dataFileId})
		print ("Downloading content")
		googleDataFile.GetContentFile('data.json')
		if os.path.isfile('./data.json'):
			print ("Done")
	except AssertionError:
		print ("Failed")

def fileExists(fileName):
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	for gfile in file_list:
		if gfile['title'] == fileName:
			return True
	return False

def upload(jsonData, fileName):
	if fileExists():
		fid = getIdOf(fileName)
		f = drive.CreateFile({'title': fileName, 'id': fid})
	else:
		f = drive.CreateFile({'title': fileName})
	f.SetContentString(jsonData)
	f.Upload()
	print ("File" + fileName + " uploaded")

def downloadSpecificJson(fileName):
	try:
		dataFileId = getIdOf(fileName)
		googleDataFile = drive.CreateFile({'id': dataFileId})
		print ("Downloading content")
		googleDataFile.GetContentFile('data.json')
		if os.path.isfile('./data.json'):
			print ("Download succesfull")
	except AssertionError:
		print ("Download failed")
