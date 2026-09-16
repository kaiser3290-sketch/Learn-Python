'''
A Python program called notes-cleaner.py that works with a class notes file. PART 1 asks the student how many characters to preview and reads exactly that many. PART 2 loads all lines into a list and prints each one with its line number. PART 3 asks which subject to skip and prints keep or skip for every line. PART 4 copies only the odd-numbered lines into a brand new file. Two files are needed — class-notes.txt (given to students) and notes-cleaner.py (built during the activity).'''
characters= int(input("enter the number of characters u want to see from the notes"))
file1=open("C:/Users/dell/Desktop/Codingal/Learn-Python/LESSONS/FILE HANDLING/class_notes.txt","r")
print(file1.read(characters))
lines=file1.readlines()
total_lines=len(lines)

subject=input("enter the subject that you want to skip ")
for i in range(0,total_lines):
    if lines[i].startswith(subject):
        continue 
    else:
        print(i+1,lines[i])