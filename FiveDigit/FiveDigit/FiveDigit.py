print("Enter 5 digit number")
number = int(input())
units = number % 10 # �������
dozens = number % 100 // 10 # �������
hundreds = number % 1000 // 100 # �����
thousands = number % 10000 // 1000 # ������
dozens_of_thousands = number // 10000 # ������� �����
result=((dozens ** units) * hundreds / (dozens_of_thousands - thousands))
print("The result is:", result, sep='')

