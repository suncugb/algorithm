# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 双向循环链表。
# 头插、尾插、中间插、按值查找、按索引查找、查找中间节点、按节点删除、反转。
# Author：Leo

from __future__ import print_function

class Node(object):
	"""
	定义双向循环链表的Node节点类。
	"""
	def __init__(self, data, prev=None, next=None):
		'''
		初始化。

		参数：
			data：存储的数据。
			prev：当前节点的前一个节点地址。
			next：当前节点的后一个节点地址。
		'''
		self.__data = data
		self.__prev = prev
		self.__next = next

	@property
	def data(self):
		'''
		获取节点存储的数据。
		'''
		return self.__data

	@data.setter
	def data(self, data):
		'''
		设置节点存储的数据。
		'''
		self.__data = data

	@property
	def prev(self):
		'''
		获取前一个节点地址。
		'''
		return self.__prev

	@prev.setter
	def prev(self, prev):
		'''
		设置前一个节点地址。
		'''
		self.__prev = prev

	@property
	def next(self):
		'''
		获取后一个节点地址。
		'''
		return self.__next

	@next.setter
	def next(self, next):
		'''
		设置后一个节点地址。
		'''
		self.__next = next

class DoubleCircularLinkedList(object):
	"""
	定义双向循环链表类。
	"""
	def __init__(self):
		self.__head = None

	@property
	def head(self):
		'''
		获取head节点。

		返回：
			head节点。
		'''
		return self.__head

	@head.setter
	def head(self, head):
		'''
		设置head节点。

		参数：
			head：待设置的节点。
		'''
		self.__head = head

	def is_empty(self):
		'''
		判断链表是否为空。
		'''
		return self.__head is None

	def add(self, data):
		'''
		从头部添加节点。

		参数：
			data：待插入节点存储的数据。
		'''
		node = Node(data)
		#如果链表为空，则node的next和prev都指向自己(因为是双向循环)，head指向node
		if self.is_empty():
			self.__head = node
			node.next = node
			node.prev = node
		 #否则链表不空
		else: 
			node.next = self.__head
			node.prev = self.__head.prev
			self.__head.prev.next = node
			self.__head.prev = node
			self.__head = node 

	def append(self, data):
		'''
		从尾部添加节点。

		参数：
			data：待插入节点存储的数据。
		'''
		node = Node(data)
		#如果当前链表是空的 那就调用头部插入方法
		if self.is_empty():
			self.add(data)
		#否则链表不为空
		else:
			node.next = self.__head
			node.prev = self.__head.prev
			self.__head.prev.next = node
			self.__head.prev = node

	def insert_before(self, node, data):
		'''
		插入存储指定数据data的节点到指定node节点之前。

		参数：
			node：指定节点。
			data：待插入节点存储的数据。
		'''
		if self.__head == None or node == None:
			return

		new_node = Node(data)
		node.prev.next = new_node
		new_node.next = node
		node.prev = new_node

	def insert_after(self, node, data):
		'''
		插入存储指定数据data的节点到指定node节点之后。

		参数：
			node：指定节点。
			data：待插入节点存储的数据。
		'''
		if self.__head == None or node == None:
			return

		new_node = Node(data)
		node.next = new_node
		new_node.next = node.next
		new_node.prev = node
		node.next.prev = new_node

	def find_by_index(self, index):
		'''
		根据指定索引查找节点。

		参数：
			inde：指定索引。
		返回：
			Node节点。
		'''
		cur = self.__head
		pos = 0
		while cur:
			if pos == index:
				break
			else:
				cur = cur.next
				pos += 1

		return cur

	def find_by_value(self, data):
		'''
		根据指定数据查找节点。
	
		参数：
			data：指定数据。
		返回：
			Node节点。
		'''
		cur = self.__head
		while cur:
			if cur.data == data:
				break
			else:
				cur = cur.next
		return cur

	def find_middle_node(self):
		'''
		查找中间节点。

		思路：
			把双向循环链表变成双向链表，简化处理。
		'''
		if self.is_empty():
			return

		#把双向循环链表变成双向链表，去掉头和尾的连接关系
		head = self.__head
		tail = self.__head.prev
		tail.next = None
		head.prev = None

		slow = self.__head
		fast = self.__head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next

		head.prev = tail
		tail.next = head
		return slow

	def delete_by_node(self, node):
		'''
		删除指定节点。

		参数：
			node：待删除节点。
		'''
		if self.is_empty() or node == None:
			return

		node.prev.next = node.next
		node.next.prev = node.prev

	def reversed(self):
		'''
		链表反转：非递归方式。

		思路：
			把双向循环链表变成双向链表，简化处理。
		'''
		if self.is_empty():
			return

		#把双向循环链表变成双向链表，去掉头和尾的连接关系
		self.__head.prev.next = None
		self.__head.prev = None

		prev = self.__head
		cur = self.__head.next
		temp = self.__head.next.next
		while cur:
			temp = cur.next			
			cur.next = prev
			prev.prev = cur
			prev = cur
			cur = temp

		self.__head.next = prev
		prev.prev = self.__head
		self.__head = prev

	def print_all(self):
		'''
		打印链表的所有节点数据。
		'''
		if self.is_empty():
			print('当前链表没有数据！')
			return 

		node = self.__head
		while node:
			if node.next == self.__head and self.__head.prev == node:
				print(str(node.data) + '->',end='')
				break
			else:
				print(str(node.data) + '->',end='')
				node = node.next

		print('\n')

if __name__ == '__main__':
	l = DoubleCircularLinkedList()

	#test add 
	l.add('I')
	l.add('am')
	l.add('a')	
	l.add('student')
	l.print_all()

	# test append
	l.append(29)
	l.append(33)
	l.print_all()

	#test find
	node = l.find_by_value('a')
	print(node.data)

	node = l.find_by_index(2)
	print(node.data)

	node = l.find_by_value(33)
	print(node.data)
	print(node.next.data)

	node = l.find_middle_node()
	print(node.data)

	# test insert
	l.insert_before(node,77)
	l.print_all()

	#test delete
	l.delete_by_node(node)
	l.print_all()

	#test reversed
	l.reversed()
	l.print_all()
