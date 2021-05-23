file=open("romeo.txt")
unique=[]
for line in file:
    words=line.split()
    for word in words:
        if not(word in unique):
            unique.append(word)
unique.sort()
print(unique)