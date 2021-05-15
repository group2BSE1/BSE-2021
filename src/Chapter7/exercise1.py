try:
    name=input("Enter file name:")
    file=open(fr"C:\Users\DELL\Desktop\BSE_Group2\BSE-2021\src\Files\{name}","r")
    read=file.read()
    print(read.upper())
except:
    print("File name doesn't exist in current directory!!!")