# -*-coding:utf-8 -*-
# Author:王茂波
# function:二叉树
class Node:
    def __init__(self, item):
        self.elem = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:  # queue不为null
            cur_node = queue.pop(0)
            if cur_node.left is None:  # 左为null就添加
                cur_node.left = node
                return
            else:  # 左不为null就加入队列
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    # 广度遍历-横向
    def breadth_travel(self):
        print('====广度遍历====')
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    # 深度（相对于根的顺序所说的）遍历-先序-中序-后序
    # 先序-根，左，右
    # 中序-左，根，右
    # 后序-左，右，根
    # 思路-从下往上，只看父子节点

    def deepth_travel_pre(self, root_node):
        # print('====深度遍历-先序====')
        if root_node is None:
            return
        print(root_node.elem, end=' ')
        self.deepth_travel_pre(root_node.left)
        self.deepth_travel_pre(root_node.right)

    def deepth_travel_mid(self, root_node):
        if root_node is None:
            return
        self.deepth_travel_mid(root_node.left)
        print(root_node.elem, end=' ')
        self.deepth_travel_mid(root_node.right)

    def deepth_travel_post(self, root_node):
        if root_node is None:
            return
        self.deepth_travel_post(root_node.left)
        self.deepth_travel_post(root_node.right)
        print(root_node.elem, end=' ')


def main():
    bt = BinaryTree()
    bt.add(0)
    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.add(6)
    bt.add(7)
    bt.add(8)
    bt.add(9)

    # bt.breadth_travel()
    bt.deepth_travel_pre(bt.root)
    print('')
    bt.deepth_travel_mid(bt.root)
    print('')
    bt.deepth_travel_post(bt.root)


if __name__ == '__main__':
    main()
