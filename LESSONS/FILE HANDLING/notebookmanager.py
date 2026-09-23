with open("C:/Users/dell/Desktop/Codingal/Learn-Python/LESSONS/FILE HANDLING/class_notes.txt","r") as file:
    print(file.read())

import os
if os.path.exists("C:/Users/dell/Desktop/Codingal/Learn-Python/LESSONS/FILE HANDLING/class_notes.txt"):
    print("true")
else:
    print("false")
os.mkdir("C:/Users/dell/Desktop/Codingal/Learn-Python/LESSONS/FILE HANDLING/dummy")