# Encryption & Decryption
random1 = "poijnbvfesdxcvgyukfcvqazxsedcfrtgbhgbjk"
random2 = "mloiuhvcxsergbnjkoiuytrdsxcfvghjkm"
random3 = "gtrdfyukiuhnbtrdpoiytresxghjnbvc"

def encryption(x):
    EncryptionMessage = random1 + x[::-1] + random2
    return EncryptionMessage

def decryption(x):
    sort1= x.removeprefix(random1)
    predecryption = sort1.removesuffix(random2)
    DecryptionMessage = predecryption[::-1]
    return DecryptionMessage

def Encryptionspace(x):
    large = x.replace(' ',random3)
    return large

def Decriptionspace(x):
    large = x.replace(random3[::-1],' ')
    return large
    
txt = input("Enter your message below:\n")
choice = input("""Which Operation do you want to Perform
1. Encryption
2. Decryption
Enter 1 rather 2:
""")
print(f"Cross Check Your message:\n{txt}\n")

match choice:
    case '1': # Encryption
        if (len(txt) < 10):
            print(f'The encrypted message is: {encryption(txt)}')
        elif(len(txt)>10):
            sentences = Encryptionspace(encryption(txt)) 
            print(f'The Encrypeted sentence is: {sentences}')
        else:
            print("No string was encrypted")
            
    case '2': # Decryption
        if (len(txt) < 10):
            print(f'The Decrypted message is: {decryption(txt)}')
        elif(len(txt)>10):
            sentences = Decriptionspace(decryption(txt))
            print(f'The Decrypted sentence is {sentences}')
        else:
            print(f'No string was Decrypted')