# Practice isX() by checking password strength.

def isStrongPassword(text):
    if len(text) < 8:
        return False
    
    elif text.isupper() ==True or text.islower() == True:
        return False

    elif text.isdecimal() == True:
        return False
    
    elif text.isalpha() == True:
        return False

    else:
        return True

print(isStrongPassword('Abcdef12'))
print(isStrongPassword('abcdef12'))
print(isStrongPassword('ABCDEF12'))
print(isStrongPassword('Abcdefgh'))
print(isStrongPassword('abc'))
