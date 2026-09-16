file1=open ("C:/Users/dell/Desktop/Codingal/Learn-Python/LESSONS/FILE HANDLING/demo.txt","r")
print(file1.read())
file1.close()

file1=open("C:/Users/dell/Desktop/Codingal/Learn-Python/LESSONS/FILE HANDLING/demo.txt","a")
file1.write("Hi i am deleted ")
file1.write("\n i am second line")
file1.close()

file1=open("C:/Users/dell/Desktop/Codingal/Learn-Python/LESSONS/FILE HANDLING/demo.txt","r")
file1.read()
print(file1.readlines()[2])