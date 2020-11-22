# automation to open up all the neccesary website/text editor during a competitive programming competition

# TODO : Ask the user the name of the cpp file while whill be created as command line arguments
# TODO : currently I am assumning the file would be in current directory only will have to change it afterwords


import webbrowser,os,sys,subprocess

# find the url of the website (code forces) and open it in default webbrowser
webbrowser.open("https://codeforces.com/problemset?tags=900-900")

# check if the file already exists, if not then create one
file = open('test.cpp')
file.write("//cpp code goes here") 
file.close()

if sys.platform=='win32':
    os.startfile("test.cpp")

else:
    try:
        os.system("open test.cpp")
    except OSError:
    	raise Exception("Sorry, The program doesn't support your operating system right now.")