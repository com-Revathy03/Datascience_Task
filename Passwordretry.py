correct_password = "openAI123";
user_input = input("Enter password: ");
for attempt in range(3):
    if user_input == correct_password:
        print("Login Successful");
        break;
    else:
        if attempt < 2:
            print("Incorrect password", "Try again.");
            user_input = input("Re-enter password: ");
        else:
            print("Account Locked");

