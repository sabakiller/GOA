num1 = int(input("please enter your first number:"))
num2 = int(input("please enter your secccond number:"))

print(num1 + num2)
print(num1 * num2)
print(num1 / num2)
print(num1 - num2)

#2

#პირველი ადამიანის ასაკის შეყვანა
age1 = int(input("შეიყვანეთ პირველი ადამიანის ასაკი: "))

#მეორე ადამიანის ასაკის შეყვანა
age2 = int(input("შეიყვანეთ მეორე ადამიანის ასაკი: "))

#ორი ასაკის შედარება და შემოწმება
if age1 > age2:
    print("პირველი ადამიანი უფროსია")
elif age2 > age1:
    print("მეორე ადამიანი უფროსია")
else:
    print("ორივე ადამიანი ტოლია ასაკში")

#2


#3 


# ცვლადების მაგალითი
name = "saba"  # ტექსტური ტიპი
age = 14  # მთელი რიცხვის ტიპი
height = 1.75  # წინამდები წიმის ტიპი
is_student = True  # ლოგიკური (boolean) ტიპი

# დაბეჭდვა
print("name:", type(name))
print("age:", type(age))
print("height:", type(height))
print("is_student:", type(is_student))