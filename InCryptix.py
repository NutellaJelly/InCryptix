# Code to encrypt any given message in Ceaser Cipher (For Now):
import random

def GetMessage(message):
    print("Enter the message you want to encode: ")
    message = input()

    if(message == None):
        print("You message must contain atleast 1 character!")
        message = ''
        GetMessage(message)

    return message

def SetKey(key):
    key = random.randint(1,25)
    #print(key)

    return key

def CeaserEncode(message, key, encoded):
    for i in range(len(message)):
        checker = message[i]

        if checker == ' ':
            encoded += checker
            continue

        if checker.isupper():
            encoded += chr(((ord(checker) + key-65)%26)+65)

        if checker.islower():
            encoded += chr(((ord(checker) + key-97)%26)+65)

        if checker.isnumeric():
            encoded += chr(((ord(checker) + key-48)%10)+48)

    return encoded

def main():
    message = ''
    key = 0
    encoded = ''
    message = GetMessage(message)
    key = SetKey(key)
    encoded = CeaserEncode(message, key, encoded)
    print("Encoded message is ",encoded)
    print("Your key is ",key,". Remember it! You will need it do decode any message." )

main()