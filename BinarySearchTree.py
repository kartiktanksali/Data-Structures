#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:24:56 2019

@author: kartiktanksali
"""



class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

        
class Tree:
    
    def __init__(self):
        self.root = None
        

    
    def getRoot(self):
        return self.root
    
    
    
    def insertNode(self,root,node):
        if root == None:
            self.root = node
        else:
            if node.data <= root.data:
                if root.left == None:
                    root.left = node
                    print("Node Inserted")
                else:
                    self.insertNode(root.left,node)
            elif node.data > root.data:
                if root.right == None:
                    root.right = node
                    print("Node Inserted")
                else:
                    self.insertNode(root.right,node)
                    
                    
    def minimum(self,root):
        if root == None:
            print("No tree present")
        else:
            temp = root
            while(temp.left != None):
                temp = temp.left
        
        print("Minimum Value is ",temp.data)
        return temp
        
        
    def deleteNode(self,root,data):
        if root == None:
            print("No elements to delete")
                
        if data < root.data:
            root.left = self.deleteNode(root.left,data)
        elif data > root.data:
            root.right = self.deleteNode(root.right,data)
        elif data == root.data:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.minimum(root.right)
            
            root.data = temp.data
            
            root.right = self.deleteNode(root.right,temp.data)
            
        return root
                    
                    
                
            
    def search(self,root,data):
        if root is None or root.data == data:
            return root
        else:
            if data <= root.data:
                return self.search(root.left,data)
            elif data > root.data:
                return self.search(root.right,data)
            
            
            
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            
            
            
            
        
        
        
tree = Tree()
print("\n 1) Insert Node \n 2) Search Node \n 3) Find Minimum Value \n 4) Delete Node \n 5) InOrder Traversal")

ch=0

while(ch<6):
    ch = int(input("Enter your choice: "))
    if ch==1:
        ele = int(input("Enter the element to be inserted in tree: "))
        root = tree.getRoot()
        node = Node(ele)
        tree.insertNode(root,node)
    elif ch==2:
        ele = int(input("Enter the element to be searched: "))
        root = tree.getRoot()
        res = tree.search(root,ele)
        if res:
            print("Element present")
        else:
            print("Element not present")
    elif ch==3:
        root = tree.getRoot()
        tree.minimum(root)
    elif ch==4:
        ele = int(input("Enter the element to be deleted: "))
        root = tree.getRoot()
        tree.deleteNode(root,ele)
        
    elif ch==5:
        root = tree.getRoot()
        tree.inorder(root)


