Prerequisite : 
1.	Install python3.7.2 and add it into your environment variable path
2.	Open command prompt and run the following command:
	a.	pip install gitpython
	b.	pip install nose
3.	Extract the zip file and refer the ReadME.txt file.



Open conf.csv :

Naming convention for adding repository:
Refer acp-service-properties,

Folder Name : acp-accounts-service
	example : {Folder Name}-dev-next.properties

Git Clone: Git clone url

Branch : Branch name you want to checkout

FilePath : specify realive path where .env file is located

Needed : Keep it Yes for now

P.S: Please close conf.csv file before you run the python file 

Open caommand line and enter the following statement;
python Utility.py {env}
