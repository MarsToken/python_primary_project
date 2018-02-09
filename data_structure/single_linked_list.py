# -*-coding:utf-8 -*-
# Author:王茂波
# function:data structure
# 单向链表
class Node:
    def __init__(self, elem):
        # 数据区和下个节点的位置-插入原则从右往左
        self.elem = elem
        self.next = None


class SingleLinkedList:
    def __init__(self, node=None):
        # 头节点
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        # current 当前游标，count记录数量
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next

    # 头插法-注意
    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    # 尾插法
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            # 非头部
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            print('头插法')
            self.add(item)
        elif pos > self.length() - 1:
            print('尾插法')
            self.add(item)
        else:
            pre = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # 是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next
        return False

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


def main():
    print('test_start')
    single_liked_list = SingleLinkedList()
    print(single_liked_list.length())
    print(single_liked_list.is_empty())

    single_liked_list.append(1)
    print(single_liked_list.is_empty())

    print(single_liked_list.length())
    single_liked_list.append(2)
    single_liked_list.append(3)
    single_liked_list.append(4)
    single_liked_list.append(5)
    single_liked_list.append(6)

    single_liked_list.add(0)
    single_liked_list.insert(3, 'a')
    single_liked_list.travel()

    print(single_liked_list.search('a'))

    single_liked_list.remove('a')
    single_liked_list.travel()

    print('test_end')


if __name__ == '__main__':
    main()
