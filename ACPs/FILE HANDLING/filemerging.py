file1txt=" "
file2txt=" "

with open(r"C:\Users\dell\Desktop\Codingal\Learn-Python\ACPs\FILE HANDLING\english.txt","r") as file1:
    file1txt=file1.read()
with open(r"C:\Users\dell\Desktop\Codingal\Learn-Python\ACPs\FILE HANDLING\science.txt","r") as file2:
    file2txt=file2.read()

with open(r"C:\Users\dell\Desktop\Codingal\Learn-Python\ACPs\FILE HANDLING\all periods.txt","w") as file3:
    file3.write(file1txt+file2txt)