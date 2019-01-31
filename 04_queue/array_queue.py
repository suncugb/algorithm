# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 基于数组实现的队列。
# 功能：入队、出队。
#
# Author：Leo

from __future__ import print_function

class ArrayQueue(object):
	"""
	定义基于数组的队列类。
	"""
	def __init__(self, capacity):
		'''
		初始化。
		'''
		self.__items = []			#定义数组（使用list）
		self.__capacity = capacity 	#定义数组最大长度
		self.__head = 0				#保存对头位置	
		self.__tail = 0 			#保存队尾位置

	def enqueue(self, item):
		'''
		入队。
		'''
		if self.__tail == self.__capacity:							#tail指向队尾
			if self.__head == 0:									#队列已满，则无法插入直接返回
				return False
			else:													#队列未满，则进行数据搬迁
				len = self.__tail - self.__head
				for i in range(0,len):
					self.__items[i] = self.__items[self.__head + i]

				self.__head = 0
				self.__tail = len
		
		if self.__items.__len__() > self.__capacity - 1:			#控制List长度不能超过capacity
			del self.__items[self.__capacity - 1]

		self.__items.insert(self.__tail,item)
		self.__tail += 1

		return True

	def dequeue(self):
		'''
		出队。
		'''
		if self.__head == self.__tail:
			return

		item = self.__items[self.__head]
		self.__head += 1
		return item
			
	def print_all(self):
		'''
		打印队列所有元素。
		'''
		for item in self.__items:
			print(str(item) + ',',end='')

		print('\n')

if __name__ == '__main__':
	queue = ArrayQueue(5)

	#test enqueue
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	queue.enqueue(4)
	queue.enqueue(5)

	#test capacity
	queue.enqueue(6)
	queue.print_all()

	#test dequeue
	queue.dequeue()
	queue.dequeue()
	queue.dequeue()

	#test enqueue
	queue.enqueue('leo')
	queue.print_all()

	queue.enqueue('hello')
	queue.print_all()
	
	queue.enqueue('world')
	queue.print_all()

	#test capacity
	queue.enqueue('xxxx')
	queue.print_all()
