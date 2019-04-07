#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 22:20:37 2019

@author: kartiktanksali
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
            
    def push(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next = self.head
            self.head = new_node
        print("Element Pushed")
        
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            print("Element Appended")
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        print("Element appended")
    
    def deleteFront(self):
        if self.head == None:
            print("No elements present to delete")
        else:
            temp = self.head.next
            self.head = temp
            print("Element deleted")
        
    def insert(self,pos,val):
        new_node = Node(val)
        temp = self.head
        prev = self.head
        for i in range(pos):
            prev = temp
            temp = temp.next
        prev.next = new_node
        new_node.next = temp
        print("Element inserted")
        
    def delete(self,key):
        if self.head==None:
            print("No elements to delete")
            return
        elif self.head.data == key:
            self.head = self.head.next
            return
        temp = self.head
        prev = self.head
        while(temp is not None):
            if temp.data==key:
                prev.next = temp.next
                print("Element Deleted")
                return
            else:
                prev = temp
                temp = temp.next
        print("Key not found")
        
        
        
    def deletePos(self,pos):
        if pos == 1:
            self.head = self.head.next
            print("Element Deleted")
            return
        temp = self.head
        prev = self.head
        for i in range(pos-1):
            prev = temp
            temp = temp.next
            
        prev.next = temp.next
        print("Element Deleted")
        
        
    def findLength(self):
        count=0
        if self.head==None:
            return 0
        if self.head.next==None:
            return 1
        
        temp = self.head
        while(temp):
            temp = temp.next
            count+=1
        return count
    
    def checkElement(self,key):
        if self.head==None:
            print("No element present to search")
        elif self.head==key:
            print("Element Found")
        else:
            temp = self.head
            while(temp):
                if temp.data==key:
                    print("Element Found")
                    return
                else:
                    temp = temp.next
            print("Element not Found")
        
    def PrintList(self):
        if self.head==None:
            print("No Linked List present to print")
        else:
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next
        
    def deleteList(self):
        if self.head==None:
            print("List if already null")
        else:
            temp = self.head
            self.head=None
            while(temp):
                prev = temp
                temp = temp.next
                del prev.data
            print("List Deleted")
            
    
    
        

if __name__ == "__main__":
    
    ch=0
    llist = LinkedList()
    while(ch<11):
        print("1) Push an element(Insert at front")
        print("2) Append an element(Insert at Rear")
        print("3) Delete an element from the front")
        print("4) Insert at a position")
        print("5) Delete a key")
        print("6) Delete at a position")
        print("7) Length of the List")
        print("8) Check for a element")
        print("9) Print the List")
        print("10) Delete the LinkedList")
        print("Enter your choice: ")
        ch = int(input())
    
        
        
        if ch==1:
            ele = int(input("Enter the element to be pushed: "))
            llist.push(ele)
        elif ch==2:
            ele = int(input("Enter the element to be appended: "))
            llist.append(ele)
        elif ch==3:
            llist.deleteFront()
        elif ch==4:
            ele = int(input("Enter the element to be inserted: "))
            pos = int(input("Enter the position to be inserted: "))
            llist.insert(pos,ele)
        elif ch==5:
            ele = int(input("Enter the element to be deleted: "))
            llist.delete(ele)
        elif ch==6:
            pos = int(input("Enter the position from the element should be deleted: "))
            llist.deletePos(pos)
        elif ch==7:
            res = llist.findLength()
            print("The length of the list: ",res)
        elif ch==8:
            ele = int(input("Enter an element to be searched: "))
            llist.checkElement(ele)
        elif ch==9:
            llist.PrintList()
        elif ch==10:
            llist.deleteList()
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    