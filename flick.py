import tkinter as tk
import os
import re
import urllib.request
import urllib.parse


root = tk.Tk()
root.withdraw()

def do():
    print("In directory " + os.getcwd())
    for file in os.listdir('.'):
        if os.path.isdir(file):
            os.chdir(file)
            do()
        elif os.stat(file).st_size >= 50*1024*1024:
#            print("File: " + file )
            fn = re.sub(r'[^a-zA-Z0-9]', ' ',file[:-4])
            print(fn)
            response = urllib.request.urlopen('http://www.omdbapi.com/?t=' + urllib.parse.quote(fn))
            print(urllib.parse.quote(fn))
            omdb = response.read()
            omdb.decode('utf-8')
#            om = omdb.split("\"imdbRating\":\"",1)
            print(omdb)

        if os.getcwd() == dir:
            os.chdir('..')
    return

dir = tk.filedialog.askdirectory()

os.chdir(dir)
do()
