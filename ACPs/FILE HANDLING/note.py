characters= int(input("enter the number of characters u want to see from the notes"))
file1=open("C:/Users/dell/Desktop/Codingal/Learn-Python/ACPs/FILE HANDLING/todo.txt","r")
print(file1.read(characters))
lines=file1.readlines()
total_lines=len(lines)

thing=input("enter the thing that you want to skip ")
for i in range(0,total_lines):
    if lines[i].startswith(thing):
        continue 
    else:
        print(i+1,lines[i])