print("Please enter a number")
x = int(input())
if x >2e9:
    print('Number is too big')
if x == 1:
    d = 1 # d - количество делителей x
else:
    d = 2
    for i in range(2, int((x/2) + 1)):
        if x % i == 0:
            d += 1
print(d)