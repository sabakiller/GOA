email = input("Enter your email: ")
password = input("Enter your password: ")

if '@' in email and '.' in email and len(password) >= 8:
    print(True)
else:
    print(False)


