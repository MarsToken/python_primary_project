# -*-coding:utf-8 -*-
# Author:王茂波
# function:各种排序

# bubble sort
def bubble_sort(src):
    n = len(src)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if src[j] > src[j + 1]:
                src[j], src[j + 1] = src[j + 1], src[j]


# select sort
def select_sort(src):
    n = len(src)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if src[i] > src[j]:
                src[i], src[j] = src[j], src[i]


# insert sort
def insert_sort(src):
    n = len(src)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if src[j] < src[j - 1]:
                src[j], src[j - 1] = src[j - 1], src[j]
            else:
                break


# shell sort
def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n // 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j > 0:
                if alist[j - gap] > alist[j]:
                    alist[j - gap], alist[j] = alist[j], alist[j - gap]
                    j -= gap
                else:
                    break
        # 得到新的步长
        gap = gap // 2


def shell(src):
    n = len(src)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and src[j - gap] > src[j]:
                src[j - gap], src[j] = src[j], src[j - gap]
                j -= gap
        gap = gap // 2


# 快速排序
def quick_sort(src, start, end):
    if start >= end:
        return
    mid = src[start]
    low = start
    high = end
    while low < high:
        while low < high and src[high] >= mid:
            high -= 1
        src[low] = src[high]
        while low < high and src[low] < mid:
            low += 1
        src[high] = src[low]
    src[low] = mid
    quick_sort(src, start, low - 1)
    quick_sort(src, low + 1, end)


# 归并排序
def merge_sort(src):
    if len(src) <= 1:
        return src
    cur = len(src) // 2
    left = merge_sort(src[:cur])
    right = merge_sort(src[cur:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    src = [11, 2, 3, 556, 4, 1]
    # bubble_sort(src)
    # select_sort(src)
    # insert_sort(src)
    # shell_sort(src)
    # quick_sort(src, 0, len(src) - 1)
    src = merge_sort(src)
    print(src)
