# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 基于链表实现的栈。
# 功能：入栈、出栈。
#
# Author：Leo

from __future__ import print_function

class Node(object):
	"""
	定义Node类。
	"""
	def __init__(self, data, next=None):
		'''

		'''
		self.__data = data
		self.__next = next

	@property
	def data(self):
		'''
		获取节点数据。
		'''
		return self.__data

	@data.setter
	def data(self, data):
		'''
		设置节点数据。
		'''
		self.__data = data

	@property
	def next(self):
		'''
		获取下一个节点。
		'''
		return self.__next

	@next.setter
	def next(self, next):
		'''
		设置下一个节点。
		'''
		self.__next = next

class LinkedStack(object):
	"""
	定义基于链表的栈类。	
	"""
	def __init__(self, size):
		'''
		初始化。

		参数：
			size：栈元素的总个数。
		'''
		self.__count = 0 		#栈元素的实际个数。
		self.__size = size 		#栈元素的总个数。
		self.__head = None 		#链表头节点。

	def push(self, data):
		'''
		入栈操作。

		参数：
			data：待入栈的数据。
		返回：
			True或False。
		'''
		if self.__count == self.__size:	#栈已满，入栈失败返回False
			return False

		new_node = Node(data) 
		if self.__head == None:   		#链表为空
			self.__head = new_node 		#将第一个入栈的元素设为头节点
		else:
			new_node.next = self.__head #链表不为空，将新节点从头部插入
			self.__head = new_node 		#更新头节点
		
		self.__count += 1 				#栈元素个数加1

		return True

	def pop(self):
		'''
		出栈操作。

		返回：
			False：出栈失败。
			target：出栈元素。
		'''
		if self.__count == 0: 			#栈已空，出栈失败返回False
			print('栈已空!')
			return False

		target = self.__head 			#将头节点出栈
		self.__head = self.__head.next 	#更新头节点
		self.__count -= 1 				#栈元素个数减1

		return target

	def print_all(self):
		'''
		打印栈中所有元素。
		'''
		node = self.__head
		while node:
			print(str(node.data) + '->',end='')
			node = node.next
		print('\n')

if __name__ == '__main__':
	ls = LinkedStack(5)

	#test push
	ls.push('I')
	ls.push('am')
	ls.push('a')
	ls.push('student')
	ls.print_all()

	#test pop
	ls.push(4)
	ls.print_all()

	ls.pop()
	ls.print_all()

	ls.pop()
	ls.print_all()

	ls.pop()
	ls.print_all()

	ls.pop()
	ls.print_all()

	ls.pop()
	ls.print_all()

	ls.pop()
	ls.print_all()
