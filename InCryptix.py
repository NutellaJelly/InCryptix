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

def addExtractionKey(encoded, key, extraction, extractionkey):
    i = key//10
    j = key%10

    extractionkey = random.randint(0,9)
    i += extractionkey
    j += extractionkey

    i = str(i).zfill(2)
    j = str(j).zfill(2)
    
    extraction = i+'0'+encoded
    extraction = extraction+'0'
    extraction = extraction+j
    extraction = extraction+'0'
    extraction = extraction+str(extractionkey)
    #print(extraction)

    return(extraction)

def main():
    message = ''
    key = 0
    encoded = ''
    extraction = ''
    extractionkey = 0
    message = GetMessage(message)
    key = SetKey(key)
    encoded = CeaserEncode(message, key, encoded)
    extraction = addExtractionKey(encoded, key, extraction, extractionkey)
    print("Extracted message is: ",extraction)
    print("Encoded message is ",encoded)

main()

# def DeCode():
#     message = '11.QZFGT.14.9'
#     temp = ''
#     l = len(message)
#     counter = 0
#     extractionkey = message[-1]
#     i,j = '',''
#     encoded = ''
#     j = message[]
#     for a in message:
#         temp += a
#         if(a == '.' and counter <= 2):
#             i = temp
#         counter += 1

#         if(a == '.' and counter <= l-)

#     j = message[l-4:l-2]
#     encoded = message[l-len(i)+1:]
#     print("i = ",i)
#     print("j = ",j)
#     print("extractionkey = ",extractionkey)
#     print("encoded = ",encoded)          
        
    
    # l = len(message)
    # extractionkey = message[-1]
    # i = message[0:2]
    # message = message[]
    # print(message)    

# DeCode()