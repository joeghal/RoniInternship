# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 22:44:52 2022

@author: Roni
""" 
import numpy

from random import random,randint
error=0
print("\n \t \b welcome to the BB84 simulation program \b  \n")
n=int(input("please enter the number of qubits:"))
basis_A=numpy.zeros(4*n,int)
common_bits=numpy.zeros(4*n,int)
basis_B=numpy.zeros(4*n,int)
state_A=numpy.zeros(4*n,int)
state_B=numpy.zeros(4*n,int)
qubit=numpy.zeros(4*n,float)
qubit_B=numpy.zeros(4*n,float)
k=0
print("you're playing as Alice, for each qubit enter the number 1 for |V>|H> Basis and 2 for |+>|-> basis")
for i in range(0,4*n):
    
    basis_A[i]=int(input("bASIS for qubit():"))
    qubit[i]=random()
    if str(input("do you want to eve to recieve this qubit?"))=="yes":
        qubit_B[i]=random()
    else:
        qubit_B[i]=1-qubit[i]
    basis_B[i]=randint(1, 2)
    if basis_A[i] ==1:
        if qubit[i]>0.5:
            state_A[i]=1
        else:
            state_A[i]=0
    elif basis_A[i]==2:
        if (qubit[i]>=0.25 and qubit[i]<0.5) or (qubit[i]>=0.75 and qubit[i]<1):
            state_A[i]=1
        else:
            state_A[i]=0
    else:
        print("please select a basis between 1 and 2")
              
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
        
print("All Qubits were succefully sent \n your basis have been publically transmitted to Bob")
print("initializing basis comparasion")        
"""we will know reverse the qubit values of B"""  
for i in range(0,4*n):
    if basis_B[i]==basis_A[i]:
        if state_B[i]==0:
            state_B[i]=1
        else:
            state_B[i]=0
        common_bits[k]=i
        k=k+1
        print("the qubit number,",i,"  used in common")
common_bits=common_bits[0:k]
print("half of these qubits values will be sent to BOB")
"""only half of the matching bits will be reveiled if there eist any bit that dont match the total with alice then there's eave dropping
if there's eve then the probability of qubit B becomes random"""



print("These are half of the bits that shared the same basis the other half will be used as a key \n")
for i in range(0,int((len(common_bits)-len(common_bits)%2)/2)):
    
    print("qubit A value",state_A[i]," qubit B value",state_B[i])
    if state_A[i]!=state_B[i]:
        error=error+1
if error!=0:
    print("there's ",error,"qubits that didn't match, someone is eavesdropping on the line ")
else:
    print("the secret key in binary is ")
    for i in range(int((len(common_bits)-len(common_bits)%2)/2),len(common_bits)):
        
        print(state_A[i]," ")


