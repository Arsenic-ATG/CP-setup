# automation to open up all the neccesary website/text editor during a competitive programming competition
import webbrowser,os

# find the url of the website (code forces) and open it in webbrowser
webbrowser.open("https://codeforces.com/problemset?tags=900-900")

# check if the file already exists
if os.path.isfile('./test.cpp'):
	print("it does")

else:
	file = open("test.cpp", "w") 
	file.write("//let's do this") 
	file.close() 
	print("now it does")

# open the .cpp file with the system's default text editor (sublime text)
os.system('open test.cpp')
