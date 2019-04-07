#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:07:23 2019

@author: kartiktanksali
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
    
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def deleteFront(self):
        if self.head == None:
            print("No elements present to delete")
        elif self.head == self.tail:
            self.head = None
            print("Element deleted and also the linked list is empty")
        else:
            self.head = self.head.next
            self.tail.next = self.head
            print("Element Deleted")
    
    def deleteRear(self):
        if self.head == None:
            print("No elements present to delete")
        elif self.head == self.tail:
            self.head = None
            print("Element deleted and also the linked is empty")
        else:
            temp = self.head
            while(temp.next!=self.tail):
                temp = temp.next
            
            temp.next = self.head
            self.tail = temp
            self.tail.next = self.head
            print("Element Deleted")
       
    def insertPos(self,pos,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            temp = self.head
            for _ in range(pos):
                temp = temp.next
            
            if temp == self.tail:
                self.append(data)
            else:
                new_node.next = temp.next
                temp.next = new_node
                print("Element inserted")

                
            
    def printList(self):
        if self.head==None:
            print("No elements present to print")
        else:
            temp = self.head
            while(temp):
                print(temp.data)
                if temp.next==self.head:
                    return
                temp = temp.next
                
                
                
        
    
if __name__ == "__main__":
    
    llist = LinkedList()
    
    ch=0
    
    while(ch<7):
        print("1) Push an element")
        print("2) Append an element")
        print("3) Delete an element in the front")
        print("4) Delete an element from the rear")
        print("5) Insert at a position")
        print("6) Print list")
        
        ch = int(input("Enter your choice: "))
        print()
        
        if ch==1:
            ele = int(input("Enter the element you want to push: "))
            llist.push(ele)
        elif ch==2:
            ele = int(input("Enter the element you want to append: "))
            llist.append(ele)
        elif ch==3:
            llist.deleteFront()
        elif ch==4:
            llist.deleteRear()
        elif ch==5:
            ele = int(input("Enter the element to be inserted: "))
            pos = int(input("Enter the position: "))
            llist.insertPos(pos,ele)
        elif ch==6:
            llist.printList()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            