
class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next =None

class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        if self.__head == None:
            return True
        else:
            return False


    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem,end=' ')
            cur = cur.next

    def add(self,item):
        New = Node(item)
        New.next = self.__head
        self.__head = New

    def append(self,item):
        cur = self.__head
        new = Node(item)
        if self.is_empty():
            self.__head = new
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next=new
            new.next = None

    def insert(self,pos,item):
        cur = self.__head
        node = Node(item)
        if pos == 0:
            self.add(item)
        elif pos == self.length():
            self.append(item)
        else:
            count = 0
            while count < pos-1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node


    def remove(self,item):
        pass

    def search(self,item):
        pass
if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.add(23)
    print(ll.length())
    ll.append(4)
    ll.insert(1,444)
    ll.insert(4,24)
    print(ll.travel())