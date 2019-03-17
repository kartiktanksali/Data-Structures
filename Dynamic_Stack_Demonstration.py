#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:01:11 2019

@author: kartiktanksali
"""

#Demonstration of implmenting a dynamic stack
#Note: The list in pyhton are dynamic in their memory allocation, therefore this is a demonstration.


max_size=5
lst = [" "]*max_size
ch=0
top=-1


def push():
    global top
    global lst
    global max_size
    if top!=max_size-1:
        max_size = max_size*2
        lst.append(" "*max_size)
    element = int(input("Enter the element to be entered: "))
    top+=1
    lst[top]=element
    return f"{element} Pushed"
        

def pop():
    global top
    global lst
    if top!=-1:
        element = lst[top]
        top-=1
        return f"{element} popped"
    

def tops():
    global top
    global lst
    if top!=-1:
        return lst[top]
    else:
        return "No element present in the stack"
    
def display():
    global top
    global lst
    if top!=-1:
        for i in range(top+1):
            print(lst[i],end=" ")
    else:
        print("Stack is now empty")
        

while(ch<5):
    print("\n 1)Push \n 2)Pop \n 3)Top \n 4)Display \n 5)Exit \n")
    ch = int(input("Enter your choice: "))
    
    if ch==1:
        res = push()
        print(res)
        display()
    elif ch==2:
        res = pop()
        print(res)
        display()
    elif ch==3:
        res = tops()
        print(res)
    elif ch==4:
        display()
        