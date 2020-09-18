"""
Write a program to create singly linked list and perform insert and delete operations
"""


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    def RemoveNode(self, RemoveKey):
        HeadVal = self.headval
        if HeadVal is not None:
            if HeadVal.dataval == RemoveKey:
                self.headval = HeadVal.nextval
                HeadVal = None
                return

        while HeadVal is not None:
            if HeadVal.dataval == RemoveKey:
                break
            preval = HeadVal
            HeadVal = HeadVal.nextval

        if HeadVal == None:
            return

        preval.nextval = HeadVal.nextval
        HeadVal = None


list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
#
# # Link first Node to second node
# list.headval.nextval = e2
#
# # Link second Node to third node
# e2.nextval = e3
# list.AtBegining("Sun")
# list.AtEnd("Sat")
# list.RemoveNode("Sun")
# list.listprint()

list.AtEnd("First name")
list.AtEnd("Middle name")
list.AtEnd("Last name")
list.listprint()
print("\n----\n")
list.RemoveNode("Middle name")
list.listprint()
