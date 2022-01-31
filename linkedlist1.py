#python code linkedlist
class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        linked_list = " "
        while(temp):
            linked_list+= (str(temp.data) + "-->")
            temp = temp.next
        print(linked_list)
    def insertNode(self,val,pos):
        target = Node(val)
        if(pos==0):
            target.next=self.head
            self.head=target
            return
        def getPrev(pos):
            temp = self.head
            count = 1
            while (count < pos):
                temp = temp.next
                count += 1
            return temp
        prev = getPrev(pos)
        nextNode = prev.next
        prev.next = target
        target.next = nextNode
    def deleteNode(self,val):
        temp=self.head
        if(temp.data == val):
            self.head=temp.next
            temp = None
            return
        while(temp.next.data!=val):
            temp=temp.next
        target_node = temp.next
        temp.next = target_node.next
        target_node.next = None

ll = linkedlist()
ll.head = Node(4)
second=Node(6)
third = Node(9)
ll.head.next=second
second.next = third
ll.insertNode(77,1)
ll.deleteNode(6)
ll.printList()
