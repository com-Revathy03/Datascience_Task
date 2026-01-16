user_input = int(input("Enter the Withdrawal Amount: "))
if user_input % 100 ==0:
    print("Dispensing", user_input)
else:
    print("Invalid Amount")