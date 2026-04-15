#Step 1 : Create an input print for the user to insert his username and store it.
import string

Validated_Username = (input("Insert your desire username: "))

#Step 2: Use elseif the username have to be 4 to 15 letters long give the user the error if not and why the error
if len(Validated_Username) < 4 and len(Validated_Username) > 15:
    print("Error: The inserted username has to have 4 to 15 letters") 
elif Validated_Username[0] in string.digits: #Step 3 : Start building an if where validate if the user use numbers at the start print error and why the error
    print("Error: The username cant have a number at the start.")
elif " " in Validated_Username:  #Step 4 : Use elseif the username have space give the user an error and why the error
    print("Error: No spaces allowed in the username.")
elif any(c in string.punctuation for c in Validated_Username): #Step 5 : The user cant use special caracters and if he use print the error and why
    print("Error: No special caracters allowed in the username.")
else: #Step 6 : Use else if every requirement is validate and good to go just print the username is created.
    print("Username validated.")


