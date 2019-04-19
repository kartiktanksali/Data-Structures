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
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            
            
            
    def search(self,root,data):
        if root is None or root.data == data:
            return root
        else:
            if data <= root.data:
                return self.search(root.left,data)
            elif data > root.data:
                return self.search(root.right,data)
            
        
        
        
tree = Tree()
print("\n 1) Insert Node \n 2) Search Node \n 3) InOrder Traversal")

ch=0

while(ch<4):
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
        tree.inorder(root)


