import os

path = ""

for x in os.listdir():
    if x.endswith(".txt"):
        # Prints only text file present in My Folder
        print(x)