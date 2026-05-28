import random
try:
    all_chars = r"""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+-={}[]|\:;"'<>,.?/`"""

    n = int(input("Enter How Many Characters You Want in Your Password: "))
    password = ""
    for i in range(n):
        password += random.choice(all_chars)
    print(password)
except ValueError:
    print("Enter Integer Value Only.")