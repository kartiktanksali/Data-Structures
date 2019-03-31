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
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        print("Element appended")
        
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
    while(ch<8):
        print("1) Push an element(Insert at front")
        print("2) Append an element(Insert at Rear")
        print("3) Insert at a position")
        print("4) Delete a key")
        print("5) Delete at a position")
        print("6) Print the List")
        print("7) Delete the LinkedList")
        print("Enter your choice: ")
        ch = int(input())
    
        
        
        if ch==1:
            ele = int(input("Enter the element to be pushed: "))
            llist.push(ele)
        elif ch==2:
            ele = int(input("Enter the element to be appended: "))
            llist.append(ele)
        elif ch==3:
            ele = int(input("Enter the element to be inserted: "))
            pos = int(input("Enter the position to be inserted: "))
            llist.insert(pos,ele)
        elif ch==4:
            ele = int(input("Enter the element to be deleted: "))
            llist.delete(ele)
        elif ch==5:
            pos = int(input("Enter the position from the element should be deleted: "))
            llist.deletePos(pos)
        elif ch==6:
            llist.PrintList()
        elif ch==7:
            llist.deleteList()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    