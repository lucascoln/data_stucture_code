
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.next =None

class SingleCycleLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        if self.__head == None:
            return True
        else:
            return False


    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem,end=' ')
            cur = cur.next
        print(cur.elem)

    def add(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    def append(self,item):
        cur = self.__head
        new = Node(item)
        if self.is_empty():
            self.__head = new
        else:
            while cur.next is not self.__head:
                cur = cur.next
            cur.next=new
            new.next = self.__head

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
            cur.next = node


    def remove(self,item):
        pos = self.search(item)
        cur = self.__head
        count = 0
        if pos == 0 :
            if pos is not False:
                if self.length()==1:
                    self.__head = None
                else:
                    self.__head = cur.next
                    cur.next.next=self.__head
            else:
                return False
        if pos:
            while count < pos - 1:
                count += 1
                cur = cur.next
            cur.next = cur.next.next
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
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())
  #  ll.append(2)
    ll.add(23)
    ll.remove(23 )
    ll.travel()

    ll.add(0)
    ll.travel()

    ll.append(3333)

   # ll.remove(23)
    ll.travel()
    #print(ll.length())
    '''
    ll.append(4)
    ll.insert(1,444)
    ll.insert(4,24)
    print(ll.travel())
    print(ll.search(5))
    ll.remove(6)
    print(ll.travel())
    '''