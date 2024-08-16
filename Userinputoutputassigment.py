first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
third = int(input("Enter third number : "))
forth = int(input("Enter forth number : "))

if first < second and first< third and first < forth :
    print(first, "is the smallest number")
elif second < first and second<third and second < forth :
    print(second, "is the smallest number")
elif third < first and third< second and third < forth :
    print(third, "is the smallest number")
else:
    print(forth,"is the smallest number")