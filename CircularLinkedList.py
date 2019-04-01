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
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            
    def append(self,data):
        new_node = Node(data)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    
    def deleteFront(self):
        if self.head == None and self.tail == None:
            print("No elements to delete")
        else:
            temp = self.head.next
            self.head = temp
            self.tail.next = self.head
            print("Element deleted from front")
            
    def deleteRear(self):
        if self.head == None and self.tail == None:
            print("No elements to delete")
        else:
            temp = self.head
            while(temp.next!=self.tail):
                temp = temp.next
            temp.next = self.head
            print("Element deleted from rear")
            
            
       
    
            
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
    while(ch<5):
        print("1) Push a Node")
        print("2) Append a Node")
        print("3) Delete a node from front")
        print("4) Delete a node from end")
        print("5) Print the List")
    
        ch = int(input("Enter your choice: "))
        
        if ch==1:
            ele = int(input("Enter an element to be pushed "))
            llist.push(ele)
        elif ch==2:
            ele = int(input("Enter an element to be appended: "))
            llist.append(ele)
        elif ch==3:
            llist.deleteFront()
        elif ch==4:
            llist.printList()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            