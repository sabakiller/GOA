for i in range(2, 51, 4):
    print(i)



for i in range(10):
    print(str(i) + " --------- GOA")



print("Even numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


print("Odd numbers:")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)


target_number = 7

print("გამოცანე რიცხვი, რომელიც მე ვფიქრობ: ")

while True:

    guess = int(input("შეიტანეთ რიცხვი: "))

    if guess == target_number:
        print("თქვენ სწორად გამოიცანით რიცხვი!")
        break 
    else:
        print("არასწორი რიცხვი, სცადეთ კიდევ ერთხელ.")