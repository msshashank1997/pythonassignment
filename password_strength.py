# In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength of the password. 
def check_password_strength(password):
    specal_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', ',','.','/',';','[',']']
    # check is password length is less then 8
    if len(password) < 8: 
        return ("Password is weak, minimum length should be 8 characters")
    # Checks if any Contains at least one digit (0-9)
    elif not any(char.isdigit() for char in password):   
        return ("password is week, it should content atlist a digit from 0-9")
    # Checks Contains both uppercase and lowercase letters
    elif not any(char.isupper() for char in password):
        return("password is week, it should content atlist one upper case letter")
    elif not any(char.islower() for char in password):
        return("password is week, it should content atlist one lower case letter")
    # Checks Contains at least one special character !@#$%^&*()_-+=,./;[]
    elif not any(char in specal_char for char in password):
        return("password is week, it should content atlist one special character !@#$%^&*()_-+=,./;[]")
    else:
        return("Password is strong")
    
print(check_password_strength("passwor"))
print(check_password_strength("password"))
print(check_password_strength("Password123"))
print(check_password_strength("password123"))
print(check_password_strength("PASSWORD123@"))
print(check_password_strength("Password123@#"))