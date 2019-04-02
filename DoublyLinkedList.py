#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:33:31 2019

@author: kartiktanksali
"""

class Node:
   def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
        
class LinkedList:
   def __init__(self):
        self.head = None

   def push(self,data):
       new_node = Node(data)
       if self.head == None:
           self.head = new_node
           print("Element Pushed")
       else:
           new_node.next = self.head
           self.head.prev = new_node
           self.head = new_node
           print("Element Pushed")
           
   def append(self,data):
       new_node = Node(data)
       if self.head == None:
           self.head = new_node
           print("Element Appended")
       else:
           temp = self.head
           while(temp.next!=None):
               temp = temp.next
           temp.next = new_node
           new_node.prev = temp
           print("Element Appended")
               
   def deleteFront(self):
        if self.head == None:
            print("No element to delete")
        else:
            self.head = self.head.next
            print("Element Deleted")
        
   def deleteRear(self):
       if self.head==None:
           print("No element to delete")
       else:
           temp = self.head
           while(temp.next!=None):
               temp = temp.next
               
           if temp.prev == None:
               self.head = None
           else:
               temp.prev.next = None
               
        
           print("Element Deleted")
     
   def insertPos(self,pos,data):
       new_node = Node(data)
       if self.head == None:
           self.head = new_node
           print("Element Inserted")
       else:
           temp = self.head
           for i in range(1,pos):
               temp = temp.next
           if temp.next==None:
               temp.next = new_node
               new_node.prev = temp
           else:
               next_node = temp.next
               temp.next = new_node
               next_node.prev = new_node
               new_node.next = next_node
               new_node.prev = next_node
                
               print("Element inserted")
    
   def printList(self):
       temp = llist.head
       
       while(temp):
           print(temp.data)
           temp = temp.next
       


if __name__=="__main__":       
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
        