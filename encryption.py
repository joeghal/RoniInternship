
def strToBinary(s):
    bin_conv = []
 
    for c in s:
        # convert each char to
        # ASCII value
        ascii_val = ord(c)
         
        # Convert ASCII value to binary
        binary_val = bin(ascii_val)
        bin_conv.append(binary_val[2:])
         
    return (' '.join(bin_conv))
def BinaryToString(binary_string):

    binary_values = binary_string.split()
    ascii_string = ""

    for binary_value in binary_values:
    # convert to int using int() with base 2
        an_integer = int(binary_value, 2)
    # convert to character using chr()
        ascii_character = chr(an_integer)
    # merge them all
        ascii_string += ascii_character
    return(ascii_string)
def Poly_alpha(message,key):
    M=[]
    z=[]
    shift=[]
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    for i in range(len(alpha)):
        z.append(i)
    c_map=dict(zip(alpha,z))
    cipher=""
    for char in message:
        M.append(char)
    for char in key:
        shift.append(c_map[char])
    
    for i in range(len(message)) :
        cipher=cipher+ShiftCipher(M[i],shift[i%len(key)])
     
    
     
    return cipher 
    
def OTP(message,key):
    m=""
    k=""
    m=strToBinary(message)
    k=strToBinary(key)
    cipher =""
    for i in range(len(m)):
        if m[i]==" ":
            cipher=cipher+" "
        elif m[i]==k[i%len(k)]:
            cipher=cipher+"0"
        else:
            cipher=cipher+"1"
    cipher=BinaryToString(cipher)
    return cipher
            
        
    



def ShiftCipher(message,shift):
    if shift==3:
        print("you have chosen a specific cipher formally known as the Caesar's Cipher")
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    c_map=dict(zip(alpha,ROTATE(alpha,27-shift)))
    cipher=""
    # cipher=numpy.zeros(len(message),int)
    
    for char in message:
        cipher=cipher + c_map[char]
        
    return cipher


def Mono_alpha(message):
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    cipher=""
    b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    random.shuffle(b)
    c_map=dict(zip(alpha,b))
   
    for char in message:
        cipher=cipher + c_map[char]
        
    return cipher

def ROTATE (lists, n): 
    output_list = [] 
    x= len(lists)
    for item in range(x - n, x): 
        output_list.append(lists[item])        
    for item in range(0, x - n):  
        output_list.append(lists[item]) 
    return output_list 


import random
"""
                    encryption program
"""

print("Welcome to my encryption program \n ")
message=str(input("please enter your message to encrypt:"))
message=message.lower()
print("please select an encryption methode from the choices below")

print("1.Shift cipher \n 2.Mono-alphabatic substitution \n 3.One Time Pad \n 4.polyalphabatic \n")
key=int()

choice=int(input("your choice"))

if choice==1:
    key=int(input("enter your key"))%27
    cipher=ShiftCipher(message,key)
elif choice==2:
    cipher=Mono_alpha(message)
elif choice==3:
    key=str(input("enter the key please"))
    cipher=OTP(message,key)
    
elif choice==4:
    
    key=str(input("please enter the key"))
    key=key.lower()
    cipher=Poly_alpha(message,key)
else:
    print("invalid choice")
print("cipher text is: ",cipher)
