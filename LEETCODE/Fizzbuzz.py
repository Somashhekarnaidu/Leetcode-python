nums=list(map(int,input("Enter the numbers:").split()))
for i in nums:
    if i%3==0 & i%5==0:
        print("Fizzbuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
    print(end=" ")