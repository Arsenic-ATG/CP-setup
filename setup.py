# automation to get my pc ready for a competitve programming cometition 
import webbrowser,os, sys

# TODO : Ask the user the name of the cpp file while whill be created as command line arguments

# find the url of the website (code forces) and open it in webbrowser
webbrowser.open("https://codeforces.com")

try:
  filename = sys.argv[1]
except:
  raise RuntimeError("Please enter the filename as command argument")


# this is the place where your file will be saved, change if you want to save it somewhere else
if not os.path.exists("../cp"):
  os.mkdir("../cp")
pathStr = '../cp/%s.cpp' % filename

cprogram = open("reference.cpp").read()

# check if the file already exists
if os.path.exists(pathStr) == False:
	file = open(pathStr, "w") 
	# add all the initial boiler plate in the file already
	file.write(cprogram) 
	file.close() 

# open the .cpp file with the system's default text editor (sublime text)
os.system('open ' + pathStr)
