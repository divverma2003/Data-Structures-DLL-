# Node class to store contents of DLL
class Node(object):
    def __init__(self, data = None):
        self.prev = None
        self.data = data
        self.next = None


# DLL Class
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Function to check if class is empty
    def is_empty(self):
        return self.head is None

    # Function to add node to head
    def add_to_head(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = self.tail = newNode
        else:
            # Link Nodes
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    # Function to add node to tail
    def add_to_tail(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = self.tail = newNode
        else:
            # Link Nodes
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    # Function that determines if list contains a value
    def contains(self,val):
        if self.is_empty():
            return False
        # Traverses through list until value is found, or list ends
        current = self.head
        while current is not None and current.data != val:
            current = current.next
        return current is not None

    # Function that adds node after a specific element
    def add_after(self, val, data):
        # If value is located at tail, add it to tail
        if self.contains(val):
            if self.tail.data == val:
                self.add_to_tail(data)
                return
            newNode = Node(data)
            current = self.head
            # Otherwise, traverse through list until value is found, or list ends
            while current is not None and current.data != val:
                current = current.next
            # If value was found, link the nodes
            if current is not None:
                nextNode = current.next
                newNode.next = nextNode
                newNode.prev = current
                current.next = newNode
                # Check if nextNode is not None 
                if nextNode: 
                    nextNode.prev = newNode
        else: # If value wasn't found, output the following message
             print(str(val) + " is not in the list!")

    # Function that adds node before a specific element
    def add_before(self, val, data):
        # If value is located at head, add it to head
        if self.contains(val):
            if self.head.data == val:
                self.add_to_head(data)
                return
            newNode = Node(data)
            current = self.head
             # Otherwise, traverse through list until value is found, or list ends
            while current is not None and current.data != val:
                current = current.next
            # If value was found, link the nodes
            if current is not None:
                prevNode = current.prev
                newNode.prev = prevNode
                newNode.next = current
                current.prev = newNode
                if prevNode:  # Check if prevNode is not None 
                    prevNode.next = newNode
        else:  # If value wasn't found, output the following message
             print(str(val) + " is not in the list!")

    # Function to remove head from list
    def remove_head(self):
        if self.is_empty():
            print("List is already empty")
        else:
            deletedData = self.head.data
            # Head is set to the next element in list
            newHead = self.head.next

            # If the list has multiple elements
            # Removes head
            # Links the following nodes 
            if newHead:
                newHead.prev = None
                self.head.next = None
                self.head = newHead
            else:
                # If the list had only one element
                self.head = self.tail = None

            print("Removed Head: " + str(deletedData))
            return True
        return False

    def remove_tail(self):
        if self.is_empty():
            print("List is already empty")
        else:
            deletedData = self.tail.data
            # Head is set to the prev element in list
            newTail = self.tail.prev

            # If the list has multiple elements
            # Removes tail
            # Links the following nodes 
            if newTail:
                newTail.next = None
                self.tail.prev = None
                self.tail = newTail
            else:
                # If the list had only one element
                self.head = self.tail = None

            print("Removed Tail: " + str(deletedData))
            return True
        return False
 
    # Function to remove the first instance of an element
    def remove_element_from_front(self, val):
        if self.contains(val):
            current = self.head
            # Traverses through list until it finds a matching value, or the end of the list is reached
            while current is not None and current.data != val:
                current = current.next
            # If matching element is found
            if current is not None:
                # Link nodes
                deletedData = current.data
                if current.prev: # Ensures that current.prev is not None
                    current.prev.next = current.next
                else:
                    # If the element to be removed is the head
                    self.head = current.next

                if current.next: # Ensures that current.next is not None
                    current.next.prev = current.prev
                else:
                    # If the element to be removed is the tail
                    self.tail = current.prev

                print("Removed Value: " + str(deletedData))
                return True
        else:
            print("List doesn't contain value: " + str(val))
        return False

    # Function to remove the last instance of an element
    def remove_element_from_back(self, val):
        if self.contains(val):
            current = self.tail
            # Traverses through list until it finds a matching value, or the end of the list is reached
            while current is not None and current.data != val:
                current = current.prev
            # If matching element is found
            if current is not None:
                # Link nodes
                deletedData = current.data
                if current.prev: # Ensures that current.prev is not None
                    current.prev.next = current.next
                else:
                    # If the element to be removed is the head
                    self.head = current.next

                if current.next: # Ensures that current.next is not None
                    current.next.prev = current.prev
                else:
                    # If the element to be removed is the tail
                    self.tail = current.prev

                print("Removed Value: " + str(deletedData))
                return True
        else:
            print("List doesn't contain value: " + str(val))
        return False

    # Function to display entire list
    def display(self):
        if self.is_empty():
            print("List is empty!")
            return
        print("List: [", end = " ")
        current = self.head
        while(current is not None):
            if(current == self.tail):
                print(current.data, end = " " )
            else:
                print(current.data, end = ", ")
            current = current.next
        print(']', end = '\n')

    # Function to display entire list in reverse
    def display_reverse(self):
        if self.is_empty():
            print("List is empty!")
            return
        print("List: [", end = " ")
        current = self.tail
        while(current is not None):
            if(current == self.head):
                print(current.data, end = " " )
            else:
                print(current.data, end = ", ")
            current = current.prev
        print(']', end = '\n')
    
    def reverse_list(self):
        if self.is_empty():
            return
       
        # If the list contains more than one one node
        # Traverses through list and swaps next and prev
        if self.tail is not self.head:
            # Pointers
            temp = None
            current = self.tail
            # Swap next and prev of all nodes
            while current is not None:
                temp = current.next
                current.next = current.prev
                current.prev = temp
                current = current.next

            # Switch the placement of the pointers pointing to head and tail
            temp = self.tail
            self.tail = self.head
            self.head = temp



def main():
    print("Welcome to Doubly Linked List!")
    print("------------------------------")
    
    list1 = DoublyLinkedList()
    list2 = DoublyLinkedList()

    outerLoopAgain = True
    loopAgain = True
    while outerLoopAgain:
        print('\n' + "Please Select One of the Two Options Listed Below:")
        print("1. Create/Mutate List (Note: Creating a List will also create an accompanying reversed list!)")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            loopAgain = True
            while loopAgain:
                print('\n' + "Menu:")
                print("-----")
                print("1. Add to Head")
                print("2. Add to Tail")
                print("3. Add After Element (From Original List)")
                print("4. Add Before Element (From Original List)")
                print("5. Remove Head")
                print("6. Remove Tail")
                print("7. Remove Element")
                print("8. Display")
                print("9. Reverse List (USE THIS AFTER ADDING NODES)")
                print("10. Back to Main Menu")

                operation = input("Enter your choice (1-10): ")

                if operation == "1":
                    numData = int(input("How many elements would you like to add to head? "))
                    
                    while numData < 1:
                        print("This number must be positive")
                        numData = int(input("How many elements would you like to add to head? "))
                    
                    for i in range(0, numData):
                        elementData = input("Enter data " + str(i+1) + ": ")
                        list1.add_to_head(elementData)
                        list2.add_to_tail(elementData)
          
                    print('\n' + "Original List")
                    print("-------------")
                    list1.display()
                    print("Reversed List")
                    print("-------------")
                    list2.display()
                elif operation == "2":
                    numData = int(input("How many elements would you like to add to tail? "))
                    
                    while numData < 1:
                        print("This number must be positive")
                        numData = int(input("How many elements would you like to add to tail? "))
                    for i in range(0, numData):
                        elementData = input("Enter data " + str(i+1) + ": ")
                        list1.add_to_tail(elementData)
                        list2.add_to_head(elementData)
                 
                    print('\n' + "Original List")
                    print("-------------")
                    list1.display()
                    print("Reversed List")
                    print("-------------")
                    list2.display()
                elif operation == "3":
                    val = input("Enter the value after which to add: ")
                    data = input("Enter one data to add after " + val +  ": ")
                    list1.add_after(val, data)
                    list2.add_before(val, data)
                    
                    print('\n' + "Original List")
                    print("-------------")
                    list1.display()
                    print("Reversed List")
                    print("-------------")
                    list2.display()
                elif operation == "4":
                    val = input("Enter the value before which to add: ")
                    data = input("Enter one data to add before : " + val + ": ")
                    list1.add_before(val, data)
                    list2.add_after(val, data)

                    print('\n' + "Original List")
                    print("-------------")
                    list1.display()
                    print("Reversed List")
                    print("-------------")
                    list2.display()
                elif operation == "5":
                    list1.remove_head()
                    list2.remove_tail()

                    print('\n' + "Original List")
                    print("-------------")
                    list1.display()
                    print("Reversed List")
                    print("-------------")
                    list2.display()

                elif operation == "6":
                    list1.remove_tail()
                    list2.remove_head()

                    print('\n' + "Original List")
                    print("-------------")
                    list1.display()
                    print("Reversed List")
                    print("-------------")
                    list2.display()
                elif operation == "7":
                    val = input("Enter the value to remove: ")
                    list1.remove_element_from_front(val)
                    list2.remove_element_from_back(val)

                    print('\n' + "Original List")
                    print("-------------")
                    list1.display()
                    print("Reversed List")
                    print("-------------")
                    list2.display()
                elif operation == "8":
                    print('\n' + "Original List")
                    print("-------------")
                    list1.display()
                    print("Reversed List")
                    print("-------------")
                    list2.display()
                elif operation == "9":
                    list1.reverse_list()
                    list2.reverse_list()
                    print('\n' + "Original List (Reversed)")
                    print("------------------------")
                    list1.display()
                    print("Reversed List (Reversed)")
                    print("------------------------")
                    list2.display()
                elif operation == "10":
                    list1 = DoublyLinkedList()
                    list2 = DoublyLinkedList()
                    loopAgain = False
                else:
                    print("Invalid choice. Please enter a number from 1 to 10.")
        elif choice == "2":
            print('\n' + "Exiting the program!")
            outerLoopAgain = False
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == '__main__':
    main()


    


