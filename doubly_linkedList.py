#python code to create , insert and delete in doubly linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    def createList(self,arr):
        n=len(arr)
        start = self.head
        temp = start
        i = 0
        while(i<n):
            newNode = Node(arr[i])
            if(i==0):
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i+=1
        self.head = start
        return start
    def countList(self):
        count = 0
        temp = self.head
        while(temp is not None):
            temp = temp.next
            count+=1
        return count
    def insertion(self,val,index):
        temp=self.head
        count = self.countList()
        #handling edge case if count is 5 and trying to insert at index 7
        if(count+1<index):
            return temp
        newNode = Node(val)
        if(index == 1):
            newNode.next = temp
            temp.prev = newNode
            self.head = newNode
            return self.head
        if(index==count+1):
            while(temp.next is not None):
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
            return self.head
        i=1
        while(i < index -1):
            temp = temp.next
            i+=1
        nodeAtTarget = temp.next
        newNode.next = nodeAtTarget
        nodeAtTarget.prev = newNode
        temp.next = newNode
        newNode.prev = temp
    def deleteAt(self,pos):
        temp = self.head
        if(temp.data == pos):
            self.head = temp.next
            temp = None
        while(temp.next.data != pos):
            temp=temp.next
        target_node = temp.next
        prev_node = temp
        next_node = target_node.next
        next_node.prev = prev_node
        prev_node.next = next_node

    def printList(self):
        temp = self.head
        dll = ""
        while(temp):
            dll+=(str(temp.data) + "<-->")
            temp=temp.next
        print(dll)

dll = DoublyLinkedlist()
arr=[66,55,33,22,44,89]
dll.createList(arr)
dll.insertion(43,4)
dll.deleteAt(33)
dll.printList()