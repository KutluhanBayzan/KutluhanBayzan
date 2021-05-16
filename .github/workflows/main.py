#who has the advantage in python?
#this is my code for check it!

import random

dc=6
#dice face quatient

number1=3000
#how many number do we check for

actions=[]                       #list of all actions

def dice():
    a0=random.randint(1,dc)     
    a1=random.randint(1,dc)
    a2=random.randint(1,dc)
    a3=random.randint(1,dc)
    a4=random.randint(1,dc)
    b=sorted([a0,a1,a2])
    c=sorted([a3,a4])
    protectorkill=0
			#in risk attacker throw 3 dice protector throw 2 dice, when dices sorted who play dice bigger he wons.
			#But if dices are same protector wins.
    			#example: A:2-3-5  P=4-3   --> 5>4: one protector died.  3=3:one attacker died, 1 to 1

    if c[1]>=b[2]:
        protectorkill+=1
    if c[0]>=b[1]:
        protectorkill+=1
    actions.append(protectorkill)
			#we append every move to actions then we will take the mean of it and we will see who has the advantege

i=1
while i<number1:
    i+=1
    dice()
            #number1 times playing game

sum=0
for number in actions:
    sum+=number
            #taking total
mean=sum/(number1)
            #mean is approximately how many person protector kill but we want to check for Attacker/Protector
ratio=(2-mean)/mean


k=1
t=ratio
while abs(t-int(t+1/2))>0.03:
    k+=1
    t=ratio*k
 				#this part is for rational approximation


                #printing values
print('#one protector killed approximately ' + str(mean) + ' attacker in one game.\n')

if mean<1/2:
    print('protector has advantage')
    print(str(k) + ' protector equavilent to '+ str(int(t)) + ' attacker.')
else:
    print('#Attacker has advantage!')
    print('#'+str(int(t)) + ' protector equavilent to '+ str(k) + ' Attacker.')

#conclusion: Attacker has bigger advantage and 7 protector about to be same as 6 attacker.
