try:
    mylist=[]
    name=input("Enter file name:")
    file=open(fr"C:\Users\DELL\Desktop\BSE_Group2\BSE-2021\src\Files\{name}","r")
    count=0
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            count+=1
            trim=line.find(":")
            extract=float(line[trim+1:])
            mylist.append(extract)
    print("Average spam confidence:",(sum(mylist))/count)
except:
    print("File name doesn't exist in current directory!!!")