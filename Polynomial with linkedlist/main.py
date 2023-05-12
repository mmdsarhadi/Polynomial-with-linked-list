class Polynomial:
    class Node:
        def __init__(self, coef, exp, next=None):
            self.coef = coef
            self.exp = exp
            self.next = next

    def __init__(self):
        self.head = Polynomial.Node(None, None)
        self.tail = self.head

    def addTerm(self, coef, exp):
        if coef == 0:
            return False
        current = self.head.next
        previous = self.head
        while current is not None:
            if current.exp == exp:
                current.coef += coef
                if current.coef == 0:
                    previous.next = current.next
                    if current.next is None:
                        self.tail = previous
                return True
            elif current.exp < exp:
                node = Polynomial.Node(coef, exp, current)
                previous.next = node
                return True
            previous = current
            current = current.next
        node = Polynomial.Node(coef, exp)
        previous.next = node
        self.tail = node
        return True

    # def addTerm(self, coef, exp):
    #     if coef == 0:
    #         return False
    #     previous = self.head
    #     while previous.next is not None and previous.next.exp < exp:
    #         previous = previous.next
    #     if previous.next is not None and previous.next.exp == exp:
    #         previous.next.coef += coef
    #         if previous.next.coef == 0:
    #             if previous.next == self.tail:
    #                 self.tail = previous
    #             previous.next = previous.next.next
    #     else:
    #         node = Polynomial.Node(coef, exp, previous.next)
    #         previous.next = node
    #         if previous == self.tail:
    #             self.tail = node
    #     return True

    
    def removeTerm(self, exp):
        current = self.head.next
        previous = self.head
        while current is not None:
            if current.exp == exp:
                previous.next = current.next
                if current.next is None:
                    self.tail = previous
                return True
            previous = current
            current = current.next
        return False

    def add(self, other):
        result = Polynomial()
        node1 = self.head.next
        node2 = other.head.next
        while node1 is not None and node2 is not None:
            if node1.exp == node2.exp:
                result.addTerm(node1.coef + node2.coef, node1.exp)
                node1 = node1.next
                node2 = node2.next
            elif node1.exp > node2.exp:
                result.addTerm(node1.coef, node1.exp)
                node1 = node1.next
            else:
                result.addTerm(node2.coef, node2.exp)
                node2 = node2.next
        while node1 is not None:
            result.addTerm(node1.coef, node1.exp)
            node1 = node1.next
        while node2 is not None:
            result.addTerm(node2.coef, node2.exp)
            node2 = node2.next
        return result

    def sub(self, other):
        result = Polynomial()
        node1 = self.head.next
        node2 = other.head.next
        while node1 is not None and node2 is not None:
            if node1.exp == node2.exp:
                result.addTerm(node1.coef - node2.coef, node1.exp)
                node1 = node1.next
                node2 = node2.next
            elif node1.exp > node2.exp:
                result.addTerm(node1.coef, node1.exp)
                node1 = node1.next
            else:
                result.addTerm(node2.coef, node2.exp) # - 
                node2 = node2.next
        while node1 is not None:
            result.addTerm(node1.coef, node1.exp)
            node1 = node1.next
        while node2 is not None:
            result.addTerm(node2.coef, node2.exp) # - 
            node2 = node2.next
        return result

    def mult(self, other):
        result = Polynomial()
        node1 = self.head.next
        while node1 is not None:
            node2 = other.head.next
            while node2 is not None:
                exp = node1.exp + node2.exp
                coef = node1.coef * node2.coef
                result.addTerm(coef, exp)
                node2 = node2.next
            node1 = node1.next
        return result

    def print(self, f=None):
        node = self.head.next
        while node is not None:
            if node.coef == 1 and node.exp == 0:
                print('1', end='', file=f)
            elif node.coef == -1 and node.exp == 0:
                print('-1', end='', file=f)
            elif node.coef > 0:
                print(node.coef, end='', file=f)
            elif node.coef < 0:
                print('-', end='', file=f)
                print(abs(node.coef), end='', file=f)
            if node.exp > 0:
                print('x', end='', file=f)
                if node.exp > 1:
                    print('^' + str(node.exp), end='', file=f)
            if node.next is not None:
                if node.next.coef >= 0:
                    print(' + ', end='', file=f)
                else:
                    print(' ', end='', file=f)
            node = node.next
        print(file=f)


def main():
    p0 = Polynomial()
    p1 = Polynomial()

    with open('input.txt', 'r') as f:
        while True:
            polynomial_choice = f.readline().strip()
            if not polynomial_choice:
                break
            operation_choice = f.readline().strip()
            if polynomial_choice == "0":
                if operation_choice == "0":
                    coef = int(f.readline().strip())
                    exp = int(f.readline().strip())
                    p0.addTerm(coef, exp)
                elif operation_choice == "1":
                    exp = int(f.readline().strip())
                    p0.removeTerm(exp)
                elif operation_choice == "2":
                    p0 = p0.add(p1)
                elif operation_choice == "3":
                    p0 = p0.sub(p1)
                elif operation_choice == "4":
                    p0 = p0.mult(p1)
                elif operation_choice == "5":
                    p0.print()
            elif polynomial_choice == "1":
                if operation_choice == "0":
                    coef = int(f.readline().strip())
                    exp = int(f.readline().strip())
                    p1.addTerm(coef,  exp)
                elif operation_choice == "1":
                    exp = int(f.readline().strip())
                    p1.removeTerm(exp)
                elif operation_choice == "2":
                    p1 = p1.add(p0)
                elif operation_choice == "3":
                    p1 = p1.sub(p0)
                elif operation_choice == "4":
                    p1 = p1.mult(p0)
                elif operation_choice == "5":
                    p1.print()


if __name__ == "__main__":
    main()
