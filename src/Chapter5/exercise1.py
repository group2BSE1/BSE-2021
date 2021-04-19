total=0
count=0
while True:
    try:
        num=input("Enter a number:")
        if num=="done":
            break  
        num1=int(num) 
        count=count+1
        total=total+num1   
    except:
        print("Invalid input")
        continue

print(total,count,total/count)
