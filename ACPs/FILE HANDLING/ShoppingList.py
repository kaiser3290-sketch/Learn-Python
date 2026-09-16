file1=open("C:/Users/dell/Desktop/Codingal/Learn-Python/ACPs/FILE HANDLING/demo.txt","w")
file1.write("clock")
file1.write("\n etc.")
file1.close()

file1=open("C:/Users/dell/Desktop/Codingal/Learn-Python/ACPs/FILE HANDLING/demo.txt","r")
print(file1.readlines()[0])
