import git 
import os
from git.test.lib.helper import with_rw_directory
from git import Repo
import string
import sys


env = sys.argv[1]
print(env)


path=os.getcwd()

def createMissedProp():
	try:
		fmissed = open(path+"\\MissedPropFromDeploy.properties","x")
	except:
		os.remove(path+"\\MissedPropFromDeploy.properties")
		fmissed = open(path+"\\MissedPropFromDeploy.properties","x")
	
	fmissed.close()

def cloning():
	print('Cloning')
	
	fileNameList = []
	filePathList = []
	ignore=True
	listOfFile = os.listdir(path)
	
	with open("conf.csv","r+") as fread:
		for line in fread:
			if(ignore):
				ignore=False
				continue
			data = line.split(",")
			print(data)
				
			if(data[0]=='config'):
				configFilePath='\\config'
			else:
				fileNameList.append(data[0])
				filePathList.append(data[3])
			
			repo = git.Repo.clone_from(data[1],path+'\\'+data[0],branch=data[2])
			
	print('Cloning finished')
	
	return fileNameList,filePathList,configFilePath
	

	
def readFile(fileName,filePath,env,configFilePath):

	print("Reading props")
	os.chdir(path+configFilePath)
	
	
	Dict = {}
	with open(path+'\\'+fileName+filePath+env+'.env',"r+") as fdeploy:
		for line in fdeploy :
			if line.find("=") != -1:
				prop1 = line.split("=")[0]
				value2 = line.split("=")[1]
				Dict[prop1]=value2
			
	newLine = []
	with open(fileName+".properties", 'r+') as fconfig:
		for line in fconfig:
			if line.find("=") != -1:
				prop = line.split("=")[0]
				value = line.split("=")[1]
				if prop in Dict:
					newLine.append(line.replace(value,Dict[prop]))
					Dict.pop(prop,None)
				else:
					newLine.append(line.replace(value,"(Replace_me)\n"))
			else:
				newLine.append(line)
				
	
	print("writing props")
	with open(fileName+".properties", 'w+') as f:
		for line in newLine:
			f.write(line)
	
	if(len(Dict)!=0):
		with open(path+"\\MissedPropFromDeploy.properties", 'a') as fmissed:
			fmissed.write('\n-----------------'+fileName+'\n')
			for prop in Dict:
				fmissed.write(prop+'='+Dict[prop]+'\n')
	
		
		

def main():
	createMissedProp()
	fileNameList,filePathList,configFilePath = cloning()
	for i in range(len(fileNameList)):
		readFile(fileNameList[i],filePathList[i],env,configFilePath)
	print("Done")
	
if __name__== "__main__" :
	main()
	
