while True:
    try:
        n = int(input("Enter Your Number: "))
        temp = n
        reverse = 0
        while n > 0:
            a = n % 10
            reverse = reverse * 10 + a
            n = n // 10
        if reverse == temp:
            print(f"{temp} is palindrome no.")
        else:
            print(f"{temp} is not a palindrome no.")
    except ValueError:
        print("Enter Integer Value")