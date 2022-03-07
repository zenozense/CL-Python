user_input = input("Username: ")
pass_input = input("Password: ")
user1_user = "admin"
user1_pass = "1234"
while user_input != user1_user or pass_input != user1_pass:
    print("Password incorrect!")
    user_input = input("Username: ")
    pass_input = input("Password: ")
print("Success!")