# automation to open up all the neccesary website/text editor during a competitive programming competition
import webbrowser,os

# TODO : Ask the user the name of the cpp file while whill be created as command line arguments
# TODO : currently I am assumning the file would be in current directory only will have to change it afterwords

# find the url of the website (code forces) and open it in webbrowser
webbrowser.open("https://codeforces.com/problemset?tags=900-900")

# check if the file already exists
if !os.path.isfile('./test.cpp'):
	file = open("test.cpp", "w") 
	file.write("//let's do this") 
	file.close() 

# open the .cpp file with the system's default text editor (sublime text)
os.system('open test.cpp')
