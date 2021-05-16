try:
    name=input("Enter file name:")
    file=open(name,"r")
    read=file.read()
    print(read.upper())
except:
    print("File name doesn't exist in current directory!!!")