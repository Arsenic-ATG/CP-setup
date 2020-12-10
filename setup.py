# this version is customised to work specifically on Arsenic's machine, if you are looking for a more generalised approach then check out master branch
import webbrowser,os

# TODO : Ask the user the name of the cpp file while whill be created as command line arguments
# TODO : currently I am assumning the file would be in current directory only will have to change it afterwords

# find the url of the website (code forces problem set page) and open it in webbrowser
 webbrowser.open("https://codeforces.com/problemset?tags=900-900")

# this is the place where your file will be saved, change if you want to save it somewhere else
pathStr = '../cp/test.cpp'

# check if the file already exists
if os.path.exists(pathStr) == False:
	file = open(pathStr, "w") 
	# add all the initial boiler plate in the file already
	file.write("//let's do this") 
	file.close() 

# open the .cpp file with the system's default text editor (sublime text)
os.system('open ' + pathStr)
