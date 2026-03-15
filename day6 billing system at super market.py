#Billing system

while True:
    name=input("Enter customer's name:")
    total=0

    while True:
        print("Enter the amount and quantity")
        amount=float(input("Enter amount:"))
        quantity=float(input("Enter quantity:"))
        total+=amount*quantity
        repeat=input("Do you want to add more item? (yes/no):")
        if repeat=="no" or repeat=="No":
            break
    print("-"*50)
    print("Name:",name)
    print("Amount to be paid:",total)
    print("-"*50)

    print("**********Happy Shopping**********")

    repeat1=input("Do you want to go to next customer? (yes/no):")
    if repeat1=="no" or repeat1=="No":
        break
