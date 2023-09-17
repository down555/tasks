print("Enter 5 digit number")
number = int(input())
units = number % 10 # единицы
dozens = number % 100 // 10 # дес€тки
hundreds = number % 1000 // 100 # сотни
thousands = number % 10000 // 1000 # тыс€чи
dozens_of_thousands = number // 10000 # дес€тки тыс€ч
result=((dozens ** units) * hundreds / (dozens_of_thousands - thousands))
print("The result is:", result, sep='')

