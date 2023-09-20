print("Enter min. investment:")
sum=int(input())
print("How much does Mike have?")
Mike=int(input())
print("How much does Ivan have?")
Ivan=int(input())

if (Mike>=sum) and (Ivan>=sum):

    print(2)

elif (Mike>=sum) and (Ivan<=sum):

    print("Mike")

elif (Mike<=sum) and (Ivan>=sum):

    print("Ivan")

elif (Mike<=sum) and (Ivan<=sum) and ((Mike+Ivan)>=sum):

    print(1)

elif (Mike<=sum) and (Ivan<=sum) and ((Mike+Ivan)<=sum):

    print(0)
