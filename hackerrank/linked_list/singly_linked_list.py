class SinglyLinkedListNode():

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtHead(self, data):
        # Write your code here
        new_head = SinglyLinkedListNode(data)
        new_head.next = self.head
        
        self.head = new_head

    def insertNodeAtTail(self, data):
        if self.head is not None:
            curr = self.head
            while curr.next is not None:
                curr = curr.next

            curr.next = SinglyLinkedListNode(data)

    def deleteNodeAtPos(self, pos):
        if pos == 0:
            self.head = self.next

        i = 1
        curr = self.head
        while curr is not None and i < pos:
            curr = curr.next

            i += 1

        curr.next = curr.next.next


    def __str__(self):
        ans = ""
        curr = self.head
        while curr is not None:
            ans = ans + str(curr.data) + " --> "
            curr = curr.next

        return ans



def main():
    llist = SinglyLinkedList()
    h1 = SinglyLinkedListNode(2)

    llist.head = h1
    llist.insertNodeAtHead(1)
    llist.insertNodeAtHead(2)

    print(llist)

    print("deleting position 2")
    llist.deleteNodeAtPos(2)
    print(llist)

    #print("deleting position 2")
    #llist.deleteNodeAtPos(2)
    #print(llist)




    print()
if __name__ == '__main__':
    main()