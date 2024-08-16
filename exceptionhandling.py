
try:
    number = 34
    print(number)
except:
    print("An error ocurred")

finally:
    print("success")

    x = 67
    y = 0
try:
    print(x / y)
except:
    print("Arithmetic error occurred")
finally:
    print("success")