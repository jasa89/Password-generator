import random

#A function do shuffle all the characters of a string
while True:
    toiminto = str(input("(g)generoi salasana, vai (e)Exit:")) # kysytään käyttäjältä toimintoa
    if toiminto=="e":
        break
    
    if toiminto=="g":
        
        def shuffle(string):
            tempList = list(string)
            random.shuffle(tempList)
            return ''.join(tempList)

#Main program starts here
    
    uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
    uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
    lowercaseLetter1 = chr(random.randint(ord('a'), ord('z'))) 
    lowercaseLetter2 = chr(random.randint(ord('a'), ord('z')))  
    digit1 = chr(random.randint(ord('0'), ord('9'))) 
    digit2 = chr(random.randint(ord('0'), ord('9'))) 
    punctuation1=chr(random.randint(ord('!'), ord('?')))
    punctuation2=chr(random.randint(ord('!'), ord('?')))
#Generate password using all the characters, in random order
    password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuation1 + punctuation2 # + ....
    password = shuffle(password)

#Ouput
    print(password)