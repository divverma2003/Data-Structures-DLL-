# Node class to hold coefficient, and exponent for each term
class Node(object):
    def __init__(self, coefficient=0, exponent=0):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

# Polynomial class to link different terms
class Polynomial(object):
    def __init__(self):
        self.head = None

    # Checks if polynomial is empty
    def is_empty(self):
        return self.head is None
    
    # Appends node onto Polynomial, given the exponent is not negative 
    def append_node(self, inputCoefficient =0, inputExponent =0):
        if inputExponent < 0:
            raise ValueError("Exponent must be non-negative.")

        term = Node(inputCoefficient, inputExponent)
        
        # If the polynomial is empty, the new term is set equal to the head
        if self.is_empty():
            self.head = term
        else:
            # Flag variables to test conditions
            sameExponent = False
            insertAfter = False
            insertBefore = False
            current = self.head
            prev = None

            while current is not None and not sameExponent and not insertAfter and not insertBefore:
                # If current exponent is greater than term exponenet, check if term is smaller than the following term.
                # If so, insert it in between the two nodes
                # Set the flag to true
                # Traverse through list
                if current.exponent > term.exponent:
                    prev = current
                    if current.next is not None:
                        if current.next.exponent < term.exponent:
                            insertAfter = True 
                    
                # If current exponent is equal to term exponent, set the flag to true
                elif current.exponent == term.exponent:
                    prev = current
                    sameExponent = True 
                # If current exponent is less than term exponent, set the flag to true
                # Traverse through list
                elif current.exponent < term.exponent:   
                    prev = current
                    insertBefore = True 
                # Traverse through list
                # prev = current
                current = current.next
            
            # If exponents match, add their coefficients
            if sameExponent:
                prev.coefficient += term.coefficient
            # Otherwise, insert the term in between, before, or after the appropriate node
            # This ensures the nodes are ordered in descending order
            elif insertAfter:
                term.next = prev.next
                prev.next = term
            elif insertBefore:
                term.next = prev
                self.head = term
            else:
                prev.next = term
    
    # Function to display the polynomial
    def display(self):
        if self.is_empty():
            print("Empty Polynomial!")
        else:
            # Traverse through list, and print current term
            current = self.head
            while current is not None:
                print(str(current.coefficient) + "x^" + str(current.exponent), end = " ")
                if(current.next is not None):
                    print("+", end = " ")
                current = current.next
            print(end = '\n')

# Function to add polynomials
# Assuming they're sorted in descending order
def add_polynomial(poly1, poly2):
    # Polynomial to store result into
    result = Polynomial()
    # Pointers
    poly1current = poly1.head
    poly2current = poly2.head

    # Traverse through both polynomials
    while poly1current is not None and poly2current is not None:
        # If poly1's current exponent is smaller than poly2, append poly2 into result
        if poly1current.exponent < poly2current.exponent:
            result.append_node(poly2current.coefficient, poly2current.exponent) 
            poly2current = poly2current.next
        # If poly2's current exponent is equal to poly1, sum the coefficients
        elif poly1current.exponent == poly2current.exponent:
            resultCoefficient = poly1current.coefficient + poly2current.coefficient
            result.append_node(resultCoefficient, poly1current.exponent)
            poly1current = poly1current.next
            poly2current = poly2current.next
        # Otherwise, append poly1 into result 
        else:
            result.append_node(poly1current.coefficient, poly1current.exponent)
            poly1current = poly1current.next
     
    return result
    


def main():
    # Variables to store polynomials
    poly1 = Polynomial()
    poly2 = Polynomial()
   
    repeatLoop = True
   
    # Function to allow user to input polynomials and see their sum
    while repeatLoop:
        choice = int(input("Enter your choice (1 or 2): "))
        
        if choice == 1:
            
            print('\n' + "Format Rules:")
            print("-------------")
            print("1. Order of terms doesn't matter.")
            print("2. Multiple terms with the same coefficient are allowed.")
            print("3. Negative exponents are not allowed.")
            print("4. Terms without exponents must be formatted like this: {number}x^0")
            print("4. White spaces between terms are allowed." + '\n')
            print("Examples of Acceptable Formats:")
            print("Ex1: 1x^3 + 6x^7 + 2x^2 + 4x^2 + 4x^0 + 5x^1")
            print("Ex2: 8x^3+10x^5+3x^2" + '\n')

            polyString1 = input("Enter the first polynomial: ")
            polyString2 = input("Enter the second polynomial: ")
            
            # Parse and add terms to polynomials
            parse_polynomial(polyString1, poly1)
            parse_polynomial(polyString2, poly2)

            # Display input polynomials
            print("First Polynomial:")
            poly1.display()
            print("Second Polynomial:")
            poly2.display()

            # Add polynomials and display result
            result = add_polynomial(poly1, poly2)
            print("Result Polynomial:")
            result.display()

            # Clear polynomials for next input
            poly1 = Polynomial()
            poly2 = Polynomial()

        elif choice == 2:
            print("Exiting the program!")
            repeatLoop = False

        else:
            print("Invalid choice. Please enter 1 or 2.")

def parse_polynomial(polyString, poly):
    # Split the input string by '+' to get individual terms
    terms = polyString.split('+')
    
    for term in terms:
        # Creates a array of size two to store coefficient and exponent
        # Remove whitespace and split by 'x^' to get coefficient and exponent
        term = term.strip().split('x^')
      
        # Convert coefficient and exponent to integers
        # Given there's no emptyspace where they should be
        coefficient = 1
        exponent = 0
        if term[0] != '':
            coefficient = int(term[0])
        if term[1] != '':
            exponent = int(term[1])

        # Append the term to the polynomial
        poly.append_node(coefficient, exponent)

if __name__ == '__main__':
    print("Welcome to Polynomial Adder!")
    print("----------------------------")
    print('\n' + "Please Select One of the Two Options Listed Below:")
    print("1. Add 2 Polynomials Together")
    print("2. Quit")

    main()

    








       






