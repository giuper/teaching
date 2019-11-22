class Node:

    def __init__(self,v):
        self.data=v
        self.next=None
        

class Stack:

    def __init__(self):
        self.head=None
        self.len=0

    def __len__(self):
        return self.len

    def push(self,val):
        n=Node(val)
        n.next=self.head
        self.head=n
        self.len+=1

    def pop(self):
        if self.head is None:
            raise Exception('empty')
        n=self.head
        self.head=n.next
        self.len-=1
        return n.data

    def peek(self):
        if self.head is None:
            raise Exception('empty')
        return self.head.data

