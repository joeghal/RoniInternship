# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:59:34 2022
noise and noise cancellation
@author: Roni
"""
import numpy

import time
import math
from random import randint,random
Time=[]
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
def NoiseCancellation(qubitsA,Time,QubitsB,stateA,stateB,basis_A,basis_B):
    T=[];error=0;trial=10000
    #cahnging the trial number will increase the accuracy of the cancellation
    #however, the required computational increases 
    for i in range(len(qubitsA)):
        if stateA[i]==stateB[i]:
            T.append(i)
        else:
            error=error+1
    if( T[0]+T[1]<=T[-1]+T[-2]+5) and( T[0]+T[1]>=T[-1]+T[-2]-5) :
        Period=list(range(T[-1]+T[-2]+T[-3]+T[-4]-5),T[-1]+T[-2]+T[-3]+T[-4]+5,0.01)
        #the easiest noise to identify is the periodic noise, since if it was periodic then 
        #certain qubits must remain unaffected, which we can use to determine the w coefficient
        w=sum(Period)/len(Period)
        w=math.pi*2/w
        for l in range(0,1570):
            error=0
            B=l/1000
            for i in range(len(qubitsA)):
                QubitsB[i]=(QubitsB[i]-math.sin(w*Time[i]+B))%1
            for i in range(len(qubitsA)):
                if basis_A[i] ==1:
                    if qubit_A[i]>0.5:
                        state_A[i]=1
                    else:
                        state_A[i]=0
                elif basis_A[i]==2:
                    if (qubit_A[i]>=0.25 and qubit_A[i]<0.5) or (qubit_A[i]>=0.75 and qubit_A[i]<1):
                        state_A[i]=1
                    else:
                        state_A[i]=0             
                if basis_B[i]==1:
                    if qubit_B[i]>0.5:
                        state_B[i]=0
                    else:
                        state_B[i]=1
                else:
                    if (qubit_B[i]>=0.25 and qubit_B[i]<0.5) or (qubit_B[i]>=0.75 and qubit_B[i]<1):
                        state_B[i]=0
                    else:
                        state_B[i]=1
                if stateA[i]!=stateB[i]:
                    error=error+1
            if (error/len(qubitsA)<=0.11):
                return QubitsB
    
        
    while (error/len(qubitsA)>=0.50) and (trial>0):
        error=0
        A=5*random()
        B=4*random()
        #next we considered exp noise, since it would generate the most errors
        for i in range(0,len(qubitsA)):
            QubitsB[i]=(QubitsB[i]+math.exp(A*Time[i]+B))%1
        for k in range(len(qubitsA)):
            if basis_A[i] ==1:
                if qubit_A[i]>0.5:
                    state_A[i]=1
                else:
                    state_A[i]=0
            elif basis_A[i]==2:
                if (qubit_A[i]>=0.25 and qubit_A[i]<0.5) or (qubit_A[i]>=0.75 and qubit_A[i]<1):
                    state_A[i]=1
                else:
                    state_A[i]=0             
            if basis_B[i]==1:
                if qubit_B[i]>0.5:
                    state_B[i]=0
                else:
                    state_B[i]=1
            else:
                if (qubit_B[i]>=0.25 and qubit_B[i]<0.5) or (qubit_B[i]>=0.75 and qubit_B[i]<1):
                    state_B[i]=0
                else:
                    state_B[i]=1
            if stateA[i]!=stateB[i]:
                error=error+1
        trial=trial -1
        if error/len(qubitsA)<=0.13:
            return QubitsB
    trial=10000
    while (error/len(qubitsA)>=0.20) and (trial>0):
        error=0
        A=5*random()
        B=4*random()
        for i in range(0,len(qubitsA)):
            QubitsB[i]=(QubitsB[i]+(A*Time[i]+B))%1
        for k in range(len(qubitsA)):
            if basis_A[i] ==1:
                if qubit_A[i]>0.5:
                    state_A[i]=1
                else:
                    state_A[i]=0
            elif basis_A[i]==2:
                if (qubit_A[i]>=0.25 and qubit_A[i]<0.5) or (qubit_A[i]>=0.75 and qubit_A[i]<1):
                    state_A[i]=1
                else:
                    state_A[i]=0             
            if basis_B[i]==1:
                if qubit_B[i]>0.5:
                    state_B[i]=0
                else:
                    state_B[i]=1
            else:
                if (qubit_B[i]>=0.25 and qubit_B[i]<0.5) or (qubit_B[i]>=0.75 and qubit_B[i]<1):
                    state_B[i]=0
                else:
                    state_B[i]=1
            
            if stateA[i]!=stateB[i]:
                error=error+1
        trial=trial -1
        if error/len(qubitsA)<=0.13:
            return QubitsB
    
def Noise(qubits,NoiseType,Time):
    
    if NoiseType=="Linear":
        A=5*random()
        B=4*random()
        #note: these factors included in A and B could be changed  according to the user's wishes
        for i in range(0,len(qubits)):
            qubits[i]=(qubits[i]+A*Time[i]+B)%1
            #this is the linear distrubance in the probability distribution of qubits
    elif NoiseType=="Periodic":
        A=2*math.pi/(sum(Time)*random())
        B=math.pi*random()/2
        #we assumed that the noise must have at most a period less than the total simulation time
        for i in range(0,len(qubits)):
            qubits[i]=(qubits[i]+math.sin(A*Time[i]+B))%1
            #this is the periodic distrubance in the probability distribution of qubits
    elif NoiseType=="Exponential":
        A=5*random()
        B=4*random()
        #note: these factors included in A and B could be changed  according to the user's wishes
        for i in range(0,len(qubits)):
            qubits[i]=(qubits[i]+A*math.exp(B*Time[i]))%1
            #this is the exponential distrubance in the probability distribution of qubits
    return qubits









   
def EVE(val,qA,bA):
    #if we include Eve, we would be able to simulate Eavesdropping in a noisy channel    
    basis_Eve=randint(1, 2)
    if val=="True":
        if basis_Eve==bA:
            qB=1-qA
        else:
            qB=random()
    else:
        qB=1-qA
       
        
    return qB
        

start_time = time.time()    
error=0
print("\n \t \b welcome to the BB84 simulation program in a noisy channel \b  \n")
n=int(input("please enter the key length:"))
basis_A=numpy.zeros(4*n,int)
common_bits=numpy.zeros(4*n,int)
basis_B=numpy.zeros(4*n,int)
state_A=numpy.zeros(4*n,int)
state_B=numpy.zeros(4*n,int)
qubit_A=numpy.zeros(4*n,float)
qubit_B=numpy.zeros(4*n,float)
k=0
V=str(input("enter True to Include Eve and False to exclude her"))
for i in range(0,4*n):
     
    
    basis_A[i]=randint(1, 2)
    qubit_A[i]=random()
    
    qubit_B[i]=EVE(V, qubit_A[i],basis_A[i])
    Time.append(time.time()-start_time)
print("three types of noises exist, Exponential, Periodic and Linear \n")
NoiseType=str(input("Please enter the noise type:"))
qubit_B=Noise(qubit_B,NoiseType,Time)
for i in range(0,4*n):    
    
    basis_B[i]=randint(1, 2)
    if basis_A[i] ==1:
        if qubit_A[i]>0.5:
            state_A[i]=1
        else:
            state_A[i]=0
    elif basis_A[i]==2:
        if (qubit_A[i]>=0.25 and qubit_A[i]<0.5) or (qubit_A[i]>=0.75 and qubit_A[i]<1):
            state_A[i]=1
        else:
            state_A[i]=0             
    if basis_B[i]==1:
        if qubit_B[i]>0.5:
            state_B[i]=1
        else:
            state_B[i]=0
    else:
        if (qubit_B[i]>=0.25 and qubit_B[i]<0.5) or (qubit_B[i]>=0.75 and qubit_B[i]<1):
            state_B[i]=1
        else:
            state_B[i]=0
        
print("All Qubits were succefully recieved \n your basis have been publically transmitted to Bob")
print("initializing basis comparasion")        
"""we will know reverse the qubit values of B"""  
for i in  range(0,4*n):
    if state_B[i]==0:
        state_B[i]=1
    else:
        state_B[i]=0
for i in range(0,4*n):
    if basis_B[i]==basis_A[i]:
      
        common_bits[k]=i
        k=k+1
        print("Qubit number,",i,"  shared the same basis")
common_bits=common_bits[0:k]
print("half of these qubits values will be sent to BOB")
"""only half of the matching bits will be reveiled if there eist any bit that dont match the total with alice then there's eave dropping
if there's eve then the probability of qubit B becomes random"""


 

print("These are half of the qubits that shared the same basis the other half will be used as a key \n")
for i in range(0,int((len(common_bits)-len(common_bits)%2)/2)):
    
    print("qubit A value",state_A[common_bits[i]]," qubit B value",state_B[common_bits[i]])
    if state_A[common_bits[i]]!=state_B[common_bits[i]]:
        error=error+1
qubit_B=NoiseCancellation(qubit_A,Time,qubit_B,state_A,state_B,basis_A,basis_B)
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
if error!=0:
    print("there's ",error,"qubits that didn't match, someone is eavesdropping on the line ")
else:
    print("the secret key in binary is ")
    for i in range(int((len(common_bits)-len(common_bits)%2)/2),len(common_bits)):
        
        print(state_A[common_bits[i]]," ")



