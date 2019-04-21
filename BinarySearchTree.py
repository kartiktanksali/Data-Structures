#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:24:56 2019

@author: kartiktanksali
"""
count = 0


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
    
    
    def maximum(self,root):
        if root == None:
            print("No tree present")
            return 0
        else:
            temp = root
            while(temp.right!=None):
                temp = temp.right
        print("Maximum Value is ",temp.data)
        return temp
        
        
    def deleteNode(self,root,data):
        if root == None:
            print("No elements to delete")
            return root
                
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
        
    
    
    def getCount(self,root):
        if root == None:
            return 0
        else:
            return self.getCount(root.left) + self.getCount(root.right) + 1
        
    def getHeight(self,root):
        if root == None:
            return -1
        else:
            return max(self.getHeight(root.left),self.getHeight(root.right)) + 1
                    
            
    def search(self,root,data):
        if root is None or root.data == data:
            return root
        else:
            if data <= root.data:
                return self.search(root.left,data)
            elif data > root.data:
                return self.search(root.right,data)
            
    def breadthFirstSearch(self,root):
        if root == None:
            return 
        else:
            queue = []
            queue.append(root)
            while(len(queue)>0):
                current = queue[0]
                print(current.data)
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
                queue.pop(0)
                            
            
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
            
            
            
            
        
        
        
tree = Tree()

ch=0

while(ch<10):
    print("\n 1) Insert Node")
    print("2) Search Node")
    print("3) Find Minimum Value")
    print("4) Find Maximum Value")
    print("5) Number of Nodes")
    print("6) Delete Node")
    print("7) Find height of the tree")
    print("8) BFS - Traversal")
    print("9) InOrder Traversal")
    
    
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
        root = tree.getRoot()
        tree.maximum(root)
    elif ch==5:
        root = tree.getRoot()
        res = tree.getCount(root)
        print("Number of nodes present in tree: ",res)
    elif ch==6:
        ele = int(input("Enter the element to be deleted: "))
        root = tree.getRoot()
        tree.deleteNode(root,ele)
    elif ch==7:
        root = tree.getRoot()
        res = tree.getHeight(root)
        print("The height of the tree is: ",res)
    elif ch==8:
        root = tree.getRoot()
        tree.breadthFirstSearch(root)
    elif ch==9:
        root = tree.getRoot()
        tree.inorder(root)


