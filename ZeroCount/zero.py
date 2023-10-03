print("Please enter some numbers to check if they are zero:")
n = int(input())
count=0
for i in range(n):
    num = int(input())
    if num == 0:
        count+=1
    else:
        count+=0
print(f"There are {count} numbers that are zero.")