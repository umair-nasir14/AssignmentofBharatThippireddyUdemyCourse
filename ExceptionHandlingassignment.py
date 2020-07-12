class InvalidPasswordException(Exception):
    pass


try:
    
    a = str(input("Enter the password\n"))
    b=len(a)
    if b <= 8:
        raise InvalidPasswordException
    else:
        print("Your password is generated")
        
except InvalidPasswordException:
    
    print("You must type a password more than 8 characters")
    
    
    