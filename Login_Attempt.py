#Step 1 Create a variable that store the correct password.
Password = "Hello_World"
counter = 0
#Step 2 Create a while loop that will validate with 3 trys an input using a counter. Print in each loop the oportunity to print the input to insert the password.
while counter < 3:
    Inserted_Password = (input("Insert password: "))
    if Inserted_Password == Password:
        print("Welcome to your account")
        break
    else:
        counter = counter + 1
        print("Incorrect Password: Remain tries avaliable " + str(3 - counter))
else: #Step 3 Use a break if the input and the validated password are the same.
    print("No more tries avaliable")
