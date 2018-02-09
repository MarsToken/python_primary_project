# -*-coding:utf-8 -*-
# Author:王茂波
# description:
# function:
import time


# a^2+b^2=c^2,a+b+c=1000

def main():
    # 最笨的方法，循环次数最多-73s
    # print('started')
    # start_time = time.time()
    # for a in range(0, 1001):
    #     for b in range(0, 1001):
    #         for c in range(0, 1001):
    #             if a + b + c == 100 and a ** 2 + b ** 2 == c ** 2:
    #                 print('a=%d,b=%d,c=%d' % (a, b, c))
    # end_time = time.time()
    # print("result=%d" % (end_time - start_time))
    # print('finished')
    # 减少一个循环-1s
    print('started')
    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print('a=%d,b=%d,c=%d' % (a, b, c))
    end_time = time.time()
    print("result=%d" % (end_time - start_time))
    print('finished')
    # python_list_test
    if 1 in range(0, 1000):
        print('1111111111111111')


if __name__ == '__main__':
    main()
