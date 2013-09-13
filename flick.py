import tkinter as tk
import re
##import urllib.request
##import urllib.parse
import os

root = tk.Tk()
root.withdraw()

def do():
##    print("In directory " + os.getcwd())
    for file in os.listdir('.'):
        if os.path.isdir(file):
            os.chdir(file)
            do()
##        if os.stat(file).st_size >= 50*1024*1024:
            print("File: " + file )
            fn = re.sub(r'[^a-zA-Z0-9]', ' ',file[:-4])
            print(fn)
##            response = urllib.request.urlopen('http://www.omdbapi.com/?t=Inception')
##                        #            print(urllib.parse.quote(fn))
##            omdb = response.read()
##            omdb = omdb.decode("utf-8")
##            om = omdb.split("\"imdbRating\":\"",1)
##            print(om[1][:3])
##
##        print(re.sub(r'[^a-zA-Z0-9]', ' ',os.getcwd()))
##        print(re.sub(r'[^a-zA-Z0-9]', ' ',dir))
        if re.sub(r'[^a-zA-Z0-9]', ' ',os.getcwd()) != re.sub(r'[^a-zA-Z0-9]', ' ',dir):
                os.chdir('..')
            
    return

dir = tk.filedialog.askdirectory()

os.chdir(dir)
do()
