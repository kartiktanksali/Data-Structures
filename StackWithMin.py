#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:05:24 2019

@author: kartiktanksali
"""



#Implementation of Simple Stack with min stack implementation

max_size=5
lst = [" "]*max_size
ch=0
top=-1
topm=-1
minStack = []


def push():
    global top
    global lst
    global minStack
    global topm
    if top!=max_size-1:
        element = int(input("Enter the element to be entered: "))
        top+=1
        lst[top]=element
        if len(minStack)==0:
            minStack.append(element)
            topm+=1
        if element<minStack[topm]:
            minStack.append(element)
            topm+=1
        return f"{element} Pushed"
    else:   
        return "Array is maxed out, cannot enter more elements"

def pop():
    global top
    global topm
    global lst
    global minStack
    if top!=-1:
        element = lst[top]
        if topm!=-1:
            if element == minStack[topm]:
                minStack.pop()
                topm-=1
        else:
            print("No elements present")
        top-=1
        return f"{element} popped"
    else:
        print("Stack is empty")
    

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

def retMin():
    global minStack
    global topm
    if topm!=-1:
        return f"Minimum element present in the stack is {minStack[topm]}"
    else:
        return "Stack empty"
        

while(ch<6):
    print("\n 1)Push \n 2)Pop \n 3)Top \n 4)Return Min \n 5)Display \n 6)Exit \n")
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
        res = retMin()
        print(res)
    elif ch==5:
        display()
        