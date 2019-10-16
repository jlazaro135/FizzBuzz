ans=int(input ("introduce un número del 1 al 100: "))

for ans in range(1, ans+1):
    if ans % 3 == 0:
        if ans % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif ans % 5 == 0:
        print("Buzz")
    else:
        print(ans)




