# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:57:15 2019

@author: qinzhen
"""

class Heap():
    def __init__(self, Type):
        '''
        type定义堆类型，x=1表示最小堆, x=0表示最大堆
        '''
        #堆的索引从1开始，堆守存放一个无用的元素
        self.heap = [-1]
        self.len = 0
        #type定义堆类型，x=1表示最小堆, x=0表示最大堆
        self.type = Type
    
    def insert(self, x):
        '''
        插入
        '''
        #进入数组
        self.heap.append(x)
        #更新长度
        self.len += 1
        #索引
        i = self.len
        #最小堆
        if self.type == 1:
            while (i >= 2):
                #不满足最小堆的定义时交换父子
                if self.heap[i] < self.heap[i // 2]:
                    self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                    i = i // 2
                else:
                    break
        #最大堆
        elif self.type == 0:
            while (i >= 2):
                #不满足最大堆的定义时交换父子
                if self.heap[i] > self.heap[i // 2]:
                    self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
                    i = i // 2
                else:
                    break
    
    def peek(self):
        #返回最小值（最大值），不删除
        return self.heap[1]

    def extract(self):
        '''
        弹出最小值（最大值）
        '''
        #交换元素
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        #目标元素
        a = self.heap[-1]
        #删除元素
        del self.heap[-1]
        #索引
        i = 1
        #更新长度
        self.len -= 1
        n = self.len
        #最小堆
        if self.type == 1:
            while (i <= n / 2):
                #左节点的位置
                j = 2 * i
                #找到更小的子节点
                if (j + 1 <= n and self.heap[j + 1] < self.heap[j]):
                    j += 1
                #不满足最小堆的定义时交换父子
                if self.heap[i] > self.heap[j]:
                    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                    i = j
                else:
                    break
        #最大堆
        elif self.type == 0:
            while (i <= n / 2):
                    #左节点的位置
                    j = 2 * i
                    #找到更小的子节点
                    if (j + 1 <= n and self.heap[j + 1] > self.heap[j]):
                        j += 1
                    #不满足最大堆的定义时交换父子
                    if self.heap[i] < self.heap[j]:
                        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                        i = j
                    else:
                        break
        return a