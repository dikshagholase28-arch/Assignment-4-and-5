for i in range(1,4):
    user_id=input("Enter user_id:")
    password=input("Enter password")

    if user_id =="diksha" and password =="1234":
         print("Login sucessful")
         break
    else:
         print("Invalid user_id or Password")

    if i==3:
        print("Maximum Attempts Reached")

