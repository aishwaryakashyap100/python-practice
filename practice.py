#example 1
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Fail")
#example 2
age = int(input("Enter age: "))
has_id = input("Do you have ID? (yes/no): ")

if age >= 18:
    if has_id == "yes":
        print("Entry allowed")
    else:
        print("ID missing")
else:
    print("Too young")
