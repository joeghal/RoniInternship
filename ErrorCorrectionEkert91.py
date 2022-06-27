# -*- coding: utf-8 -*-
"""
Created on Fri Jun 2 00:06:33 2022

@author: Roni
"""




import numpy




from random import random,randint,choice

def XOR(A,B):
    if A==B:
        return 0
    else:
        return 1
def HammingEncoder(data):
    """in this encoder, we consider 4 bits of data input that we encode
    in 3 Parity Qubits to determine and correct any single errors that occured
    """
    P1=XOR(data[0],data[1])
    P1=XOR(P1,data[3])
    P2=XOR(data[0],data[2])
    P2=XOR(P2,data[3])
    P3=XOR(data[1],data[2])
    P3=XOR(P3,data[3])
    ParityQubits=[P1,P2,P3]
    return ParityQubits
def HammingCorrection(AliceParityQubits,BobParityQubits,BobDataQubits):
    E3=XOR(AliceParityQubits[2],BobParityQubits[2])
    E2=XOR(AliceParityQubits[1],BobParityQubits[1])
    E1=XOR(AliceParityQubits[0],BobParityQubits[0])
    ErrorLocation=E1+2*E2+4*E3
    if ErrorLocation==3:
        BobDataQubits[0]=(BobDataQubits[0]+1)%2
    elif ErrorLocation==5:
        BobDataQubits[1]=(BobDataQubits[1]+1)%2
    elif ErrorLocation==6:
        BobDataQubits[2]=(BobDataQubits[2]+1)%2
    elif ErrorLocation==7:
        BobDataQubits[3]=(BobDataQubits[3]+1)%2
    return BobDataQubits

def PrivacyAmplification(data):
    key=""
    """this is based on the Von Neumann randomness extractor
    this should be applied to both alice and bob to strengthen their keys and
    to remove Eave's knowledge that was leaked during the error correction phase
    """
    try:
        for i in range(0,len(data),2):
            if data[i]!=data[i+1]:
                key=key+str(data[i])
    except IndexError:
        return key
    return key
   
def EVE(val,qA,bA):
    
    """ we considered an adversary called Eve that can intercept the photons and 
    measure them in any basis, if the basis matched Alice's basis then Eve can 
    reproduce photons with the same polarization. In this case she will remain unnoticed,
    otherwise, Bob will have a 50% chance of obtaining a different result.
    Two strategies were studied:
        the first one consists of maximizing the information 
    gained by Eve while minimalizing the generated error.
        the second consists of randomly selectiong a basis and measuring the photons."""
   #Mod 1: Maximum eavesdropping strategy:
   #basis_Eve=4
   #Mod 2 :Random selection of basis
    basis_Eve=choice([0,4,2])
    if val=="True":
        if basis_Eve==bA:
            qB=1-qA
        else:
            qB=random()
    else:
        qB=1-qA
       
        
    return qB
RelativeError=numpy.zeros(50,float) 
ER=0     
for ErrorRate in range(0,50):
    for trial in range(100):
        
        error=0
        print("\n \t \b welcome to the BB84 simulation program \b  \n")

        n=1000 #Approximate key Length
        basis_A=numpy.zeros(4*n,int)
        common_bits=numpy.zeros(4*n,int)
        basis_B=numpy.zeros(4*n,int)
        state_A=numpy.zeros(4*n,int)
        state_B=numpy.zeros(4*n,int)
        qubit_A=numpy.zeros(4*n,float)
        qubit_B=numpy.zeros(4*n,float)
        
        k=0
        V="True"
        for i in range(0,4*n):
     
    
            basis_A[i]=choice([0,4,2])
            basis_B[i]=choice([4,2,3])
            qubit_A[i]=random()
            qubit_B[i]=1-qubit_A[i]
            
            if basis_A[i] ==0:
                if qubit_A[i]>0.5:
                    state_A[i]=1
                else:
                    state_A[i]=0
            elif basis_A[i]==4:
                if (qubit_A[i]>=0.25 and qubit_A[i]<0.5) or (qubit_A[i]>=0.75 and qubit_A[i]<1):
                    state_A[i]=1
                else:
                    state_A[i]=0
            elif basis_A[i]==2:
                if (qubit_A[i]>=0 and qubit_A[i]<0.125) or (qubit_A[i]>=0.25 and qubit_A[i]<0.375) or (qubit_A[i]>=0.5 and qubit_A[i]<0.625)or (qubit_A[i]>=0.75 and qubit_A[i]<0.875):
                    state_A[i]=1
                else:
                    state_A[i]=0
            
                
            
    
        for i in range(0,4*n,100):
            for j in range(ErrorRate):
                """ to implement a randomly distributed errors, we considered two
                scenarios, the first consits of an adversary Eve intercepting the 
                respective qubit while the other consits of flipping the respective 
                bit value"""
                try:
                    ZZ=randint(i, i+100)
                    #Mod1:Eavesdropping on the line causing the errors
                    qubit_B[ZZ]=EVE(V, qubit_A[ZZ],basis_A[ZZ])
                    #Mod 2: Bit-flip causing the errors
                    # qubit_B[ZZ]=(qubit_B[ZZ]+0.5)%1

                except IndexError:
                    continue
    
    
    
        for i in range(0,4*n):    
              
            if basis_B[i] ==4:
                # if qubit_B[i]>0.5:
                if (qubit_B[i]>=0.25 and qubit_B[i]<0.5) or (qubit_B[i]>=0.75 and qubit_B[i]<1):
                    state_B[i]=1
                else:
                    state_B[i]=0
            elif basis_B[i]==2:
                if (qubit_B[i]>=0 and qubit_B[i]<0.125) or (qubit_B[i]>=0.25 and qubit_B[i]<0.375) or (qubit_B[i]>=0.5 and qubit_B[i]<0.625)or (qubit_B[i]>=0.75 and qubit_B[i]<0.875):
                    state_B[i]=1
                else:
                    state_B[i]=0
            elif basis_B[i]==3:
                if (qubit_B[i]>=0 and qubit_B[i]<0.125) or (qubit_B[i]>=0.25 and qubit_B[i]<0.375) or (qubit_B[i]>=0.5 and qubit_B[i]<0.625)or (qubit_B[i]>=0.75 and qubit_B[i]<0.875):
                    state_B[i]=0
                else:
                    state_B[i]=1
        
       
        for i in  range(0,4*n):
            if state_B[i]==0:
                state_B[i]=1
                #Assuming that both qubits are perfectly anticorrelated then if
                #Alice measured 1 Bob should measure 0 in the same basis
                #To match both strings of bits, Bob should flip all his measured values
            else:
                state_B[i]=0
        
            if basis_B[i]==basis_A[i]:
                #In this part we're comparing all the measurement basis to determine
                #which qubits share the anticorrelation properties that are later 
                #used in key generation
                common_bits[k]=i
                k=k+1
                print("Qubit number,",i,"  shared the same basis")
        common_bits=common_bits[0:k]
        i=0
        CorrectedKey=[]
        while i <k:
           
            try:
                """in this part, we divided the key into 4-bits keys that we 
                encoded each of them into 3 parity using the Hamming code.
                Then comparing the Parity of the sent and recieved bits we 
                detected any emission errors and corrected them."""
                dataA=[state_A[common_bits[i]],state_A[common_bits[i+1]],state_A[common_bits[i+2]],state_A[common_bits[i+3]]]
                AliceParityQubits=HammingEncoder(dataA)
                dataB=[state_B[common_bits[i]],state_B[common_bits[i+1]],state_B[common_bits[i+2]],state_B[common_bits[i+3]]]
                BobParityQubits=HammingEncoder(dataB)
                dataB=HammingCorrection(AliceParityQubits,BobParityQubits,dataB)
                [state_B[common_bits[i]],state_B[common_bits[i+1]],state_B[common_bits[i+2]],state_B[common_bits[i+3]]]=[dataB[0],dataB[1],dataB[2],dataB[3]]
        
        
            except IndexError:
        
                common_bits=common_bits[0:i]
                break
            i=i+4

        print("half of these qubits values will be sent to BOB")
        """only half of the matching bits will be reveiled if there eist any bit that dont match the total with alice then there's eave dropping
        if there's eve then the probability of qubit B becomes random"""


 

        
        for i in range(0,int((len(common_bits)-len(common_bits)%2)/2)):
    
            if state_A[common_bits[i]]!=state_B[common_bits[i]]:
               
                error=error+1
        if error!=0:
            print("there's ",error,"qubits that didn't match, someone is eavesdropping on the line ")
        else:
            data=[]
            ER=ER+1
            print("the secret key in binary is ")
        for i in range(int((len(common_bits)-len(common_bits)%2)/2),len(common_bits)):
            data.append(state_A[common_bits[i]])
            print(state_A[common_bits[i]]," ")

            print("The Amplified Key is",PrivacyAmplification(data))
    RelativeError[ErrorRate]=ER
    
    ER=0