#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 12:53:37 2019

@author: kartiktanksali
"""

#Implementation of Simple Stack

max_size=5
lst = [" "]*max_size
ch=0
top=-1


def push():
    global top
    global lst
    if top!=max_size-1:
        element = int(input("Enter the element to be entered: "))
        top+=1
        lst[top]=element
        return f"{element} Pushed"
    else:   
        return "Array is maxed out, cannot enter more elements"

def pop():
    global top
    global lst
    if top!=-1:
        element = lst[top]
        top-=1
        return f"{element} popped"
    else:
        return "Stack is empty, cannot pop"

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
        print("Stack is empty to be displayed")
        

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
        