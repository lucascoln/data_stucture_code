class Node(object):
    def __init__(self, item):
        self.elem = item
        self.pre = None
        self.next = None

class DoubleLinkList(object):
    def __init__(self,node=None):
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
        self.__head.pre = New
        New.pre = None
        self.__head = New

    def append(self,item):
        cur = self.__head
        new = Node(item)
        if self.is_empty():
            self.__head = new
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = new
            new.pre = cur
            new.next = None

    def insert(self,pos,item):
        cur = self.__head
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > self.length()-1:
            self.append(item)
        else:
            count = 0
            while count < pos-1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next.pre = node
            node.pre = cur
            cur.next = node


    def remove(self,item):
        pos = self.search(item)
        cur = self.__head
        count = 0
        if pos == 0 :
            if pos is not False:
                self.__head = cur.next
                cur.next.pre = None
            else:
                return False
        if pos:
            while count < pos - 1:
                count += 1
                cur = cur.next
            if pos == self.length()-1:
                cur.next = None
                return
            else:
                cur.next = cur.next.next
                cur.next.next.pre = cur
        else:
            return False

    def search(self,item):
        cur = self.__head
        count = 0
        while cur != None:
            if cur.elem == item:
                return count
            else:
                count += 1
                cur = cur.next
        return False

if __name__ == '__main__':
    ll = DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    print(ll.length())
    ll.add(23)
    print(ll.length())
    ll.append(4)
    ll.insert(1,444)
    ll.insert(4,24)
    print(ll.travel())
    print(ll.search(5))
    ll.remove(2)
    print(ll.travel())