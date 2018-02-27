# -*-coding:utf-8 -*-
# Author:王茂波
# function:双向链表
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.pre = None


class DoubleLinkedList:
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            cur = cur.next
            print(cur.elem, end=' ')
        print('')

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
        # changed1
        node.next.pre = node

    def append(self, item):
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            # changed2
            node.pre = cur

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            # changed3
            count = 0
            cur = self.__head
            while count < pos:
                count += 1
                cur = cur.next
            # 退出循环，cur指向pos位置
            node = Node(item)
            node.next = cur
            node.pre = cur.pre
            cur.pre.next = node
            cur.pre = node

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.pre = None
                else:
                    cur.pre.next = cur.next
                    if cur.next:
                        cur.next.pre == cur.pre
                break
            else:
                cur = cur.next


def main():
    dll = DoubleLinkedList()


if __name__ == '__main__':
    main()
