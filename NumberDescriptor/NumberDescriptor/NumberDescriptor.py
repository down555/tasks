print("Enter a number to get it's description:")
number = int(input())
if number > 0 and number % 2 ==0:
    print("This is a positive odd number")
elif number < 0 and number % 2 ==0:
    print("This is a negative odd number")
    
if number % 2 !=0:
    print("Number is not odd")

if number == 0: 
    print("Number is zero")