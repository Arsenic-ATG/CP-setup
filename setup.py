# automation to open up all the neccesary website/text editor during a competitive programming competition

import webbrowser,os

# find the url of the website (code forces) and open it in webbrowser
webbrowser.open("https://codeforces.com/problemset?tags=900-900")

# open a .cpp file with text editor (sublime text)
os.popen('open test.cpp')