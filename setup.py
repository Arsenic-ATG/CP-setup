# automation to open up all the neccesary website/text editor during a competitive programming competition
import webbrowser,os

# find the url of the website (code forces) and open it in default webbrowser
webbrowser.open("https://codeforces.com/problemset?tags=900-900")

# check if the file already exists, if not then create one
file = open("test.cpp", "w") 
file.write("//cpp code goes here") 
file.close()

# open the .cpp file with the system's default text editor (sublime text)
os.system('open test.cpp')
