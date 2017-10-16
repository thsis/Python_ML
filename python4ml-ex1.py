# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:16:37 2017

@author: paulina
"""
#Exercise 1
#Classifying a single instance (15 P)
x=('yes',31,'good')#defining a tuple
Create a function that takes as input a tuple containing values for attributes (smoker,age,diet), and computes
the output of the decision tree.

def classifier(x):
    if x[0]=='yes': 
        if x[1]>29.5:
            z=(x,'more')
        else:
            z=(x,'less')    
    elif x[0]=='no':
        if x[2]=='poor':
            z=(x,'more')
        else:
            z=(x,'less') 
    return z

print(classifier(x))#testing the function

#Reading a dataset from a text file (10 P)
file=open('health-test.txt','r')
my_list_of_tuple=[]
for line in file:
    tmp1=line.strip()
    tmp2=tmp.split(',')
    t= (tmp2[0], int(tmp2[1]),tmp2[2])
    my_list_of_tuple.append(t)
print ( my_list_of_tuple)
    
   
    
     
    


